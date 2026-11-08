#!/usr/bin/env python3
"""SpyderMonkey scope gateway — transport-level estate enforcement.

A local forward proxy on 127.0.0.1 (default 8898). EVERY request through it
(CONNECT tunnels for https, absolute-URI forwards for http) is checked against
the shared scope authority before it can leave the box: out-of-estate targets
are refused at the transport layer with a 403 + audit record. The model and
its tools cannot talk their way past a network gate — this is enforcement
below the prompt and below the hook.

`smk gateway start|stop|status [--port N]`
`smk gateway netdist --target T [--iface IF] [--dry-run]` — nftables egress
ruleset generator (kernel-depth; explicitly opt-in, never auto-applied).

Honest ceiling: the gateway enforces what ROUTES THROUGH IT. The nftables
egress layer (`netdist`) is the forcing function that makes the whole host
respect the estate; the hook gate catches direct-connect attempts. Defense
in depth: contract → hook → proxy → kernel rules.
"""

import argparse
import http.client
import json
import os
import signal
import socket
import socketserver
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import scope_authority as sa  # noqa: E402

DEFAULT_PORT = 8898
PIDFILE = Path.home() / ".redteam" / "gateway.pid"
LOGFILE = Path.home() / ".redteam" / "gateway.log"

_decisions = {"ok": 0, "deny": 0}


def _check(host: str) -> tuple[bool, str]:
    ok, reason, _ = sa.check(host, strict=True, audit=True, allow_lab=True)
    _decisions["ok" if ok else "deny"] += 1
    return ok, reason


class _Handler(socketserver.BaseRequestHandler):
    def handle(self):  # CONNECT and absolute-URI forwards over one socket
        try:
            data = self.request.recv(65536)
        except OSError:
            return
        if not data:
            return
        head = data.split(b"\r\n\r\n", 1)[0].decode("latin-1", "replace")
        lines = head.split("\r\n")
        if not lines:
            return
        method, target, _ = lines[0].split(" ", 2)
        host, port = self._target_host_port(method, target)
        if host is None:
            self._reply(b"HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n")
            return
        ok, reason = _check(host)
        if not ok:
            body = json.dumps({"gate": "spydermonkey", "denied": host,
                               "reason": reason}).encode()
            self._reply(b"HTTP/1.1 403 Forbidden\r\nContent-Type: application/json\r\n"
                        + f"Content-Length: {len(body)}\r\n\r\n".encode() + body)
            _log(f"DENY  {method} {host}:{port} — {reason}")
            return
        _log(f"OK    {method} {host}:{port}")
        if method == "CONNECT":
            self._tunnel(host, port, data)
        else:
            self._forward(host, port, data)

    @staticmethod
    def _target_host_port(method: str, target: str) -> tuple[str | None, int]:
        if method == "CONNECT":
            h, _, p = target.partition(":")
            return h, int(p or 443)
        # absolute-URI: http://host[:port]/path
        if "://" in target:
            from urllib.parse import urlparse
            u = urlparse(target)
            return u.hostname, u.port or 80
        return None, 0

    def _reply(self, raw: bytes) -> None:
        try:
            self.request.sendall(raw)
        except OSError:
            pass

    def _tunnel(self, host: str, port: int, first: bytes) -> None:
        try:
            up = socket.create_connection((host, port), timeout=15)
        except OSError as e:
            self._reply(b"HTTP/1.1 502 Bad Gateway\r\nContent-Length: 0\r\n\r\n")
            _log(f"TUNNEL FAIL {host}:{port} — {e}")
            return
        self._reply(b"HTTP/1.1 200 Connection established\r\n\r\n")
        if first.split(b"\r\n\r\n", 1)[0] != first or len(first) > len(head := first.split(b"\r\n\r\n", 1)[0]) + 4:
            up.sendall(first.split(b"\r\n\r\n", 1)[1] if b"\r\n\r\n" in first else b"")
        self.request.settimeout(60)
        up.settimeout(60)
        import threading
        stop = threading.Event()
        def pump(src, dst):
            try:
                while not stop.is_set():
                    chunk = src.recv(65536)
                    if not chunk:
                        break
                    dst.sendall(chunk)
            except OSError:
                pass
            finally:
                stop.set()
        t = threading.Thread(target=pump, args=(self.request, up), daemon=True)
        t.start()
        pump(up, self.request)
        stop.set()
        try:
            up.close()
        except OSError:
            pass

    def _forward(self, host: str, port: int, data: bytes) -> None:
        try:
            conn = http.client.HTTPConnection(host, port, timeout=30)
            head, _, body = data.partition(b"\r\n\r\n")
            head = head.replace(b"Proxy-Connection", b"X-Proxy-Connection")
            method, target, _ = head.decode("latin-1").split(" ", 2)
            from urllib.parse import urlparse
            path = urlparse(target).path or "/"
            q = urlparse(target).query
            path = path + (f"?{q}" if q else "")
            conn.request(method, path, body=body or None,
                         headers={"Host": host})
            r = conn.getresponse()
            payload = r.read()
            head = f"HTTP/1.1 {r.status} {r.reason}\r\n"
            for k, v in r.getheaders():
                if k.lower() in ("transfer-encoding", "connection"):
                    continue
                head += f"{k}: {v}\r\n"
            head += f"Content-Length: {len(payload)}\r\n\r\n"
            self._reply(head.encode("latin-1") + payload)
            conn.close()
        except OSError as e:
            _log(f"FORWARD FAIL {host}:{port} — {e}")
            self._reply(b"HTTP/1.1 502 Bad Gateway\r\nContent-Length: 0\r\n\r\n")


def _log(line: str) -> None:
    try:
        with LOGFILE.open("a", encoding="utf-8") as f:
            f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%S%z')} {line}\n")
    except OSError:
        pass


class _Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def _serve(port: int) -> None:
    _log(f"GATEWAY UP on 127.0.0.1:{port} — every request is scope-checked")
    with _Server(("127.0.0.1", port), _Handler) as srv:
        srv.serve_forever()


def cmd_gateway(args) -> int:
    action = args.action
    port = args.port

    if action == "start":
        if PIDFILE.exists():
            try:
                os.kill(int(PIDFILE.read_text().strip()), 0)
                print(f"✗ gateway already running (pid {PIDFILE.read_text().strip()})")
                return 1
            except (OSError, ValueError):
                PIDFILE.unlink(missing_ok=True)
        logf = LOGFILE.open("a", encoding="utf-8")
        p = subprocess.Popen(
            [sys.executable, str(Path(__file__).resolve()), "--serve", str(port)],
            stdout=logf, stderr=logf, start_new_session=True,
            stdin=subprocess.DEVNULL)
        PIDFILE.write_text(str(p.pid), encoding="utf-8")
        print(f"⚙ gateway up — 127.0.0.1:{port} (pid {p.pid})")
        print("  route probes through it: export http_proxy/https_proxy "
              f"http://127.0.0.1:{port}")
        return 0

    if action == "stop":
        if not PIDFILE.exists():
            print("✗ gateway not running")
            return 1
        pid = int(PIDFILE.read_text().strip())
        try:
            os.kill(pid, signal.SIGTERM)
        except OSError:
            pass
        PIDFILE.unlink(missing_ok=True)
        print(f"⚙ gateway stopped (pid {pid})")
        return 0

    if action == "status":
        running = False
        if PIDFILE.exists():
            try:
                pid = int(PIDFILE.read_text().strip())
                os.kill(pid, 0)
                running = True
            except (OSError, ValueError):
                running = False
        print(f"  gateway:    {'RUNNING' if running else 'stopped'}"
              + (f" (pid {PIDFILE.read_text().strip()})" if running else ""))
        print(f"  port:       {port}")
        print(f"  decisions:  ok={_decisions['ok']} deny={_decisions['deny']} "
              f"(since process start; log: {LOGFILE})")
        return 0

    if action == "netdist":
        return _netdist(args)

    return 2


def _netdist(args) -> int:
    """Generate an nftables egress ruleset from scope.json (kernel depth).

    Opt-in by design: prints the ruleset; apply it yourself with
    `nft -f file` on the right host/interface. Never auto-applied.
    """
    scope = sa.load_scope()
    if not scope:
        print("✗ no scope authority — netdist needs scope.json", file=sys.stderr)
        return 1
    rules = scope.get("rules", {})
    entries = []
    for e in rules.get("allow", []):
        entries.append(e)
    for e in scope.get("assets", []) if isinstance(scope.get("assets"), list) else []:
        entries.append(e)
    iface = args.iface or "lo"
    print(f"# SpyderMonkey netdist — egress estate ruleset (scope: {scope.get('engagement')})")
    print(f"# Apply:  sudo nft -f {args.out or 'netdist.rules'}   (never auto-applied)")
    print("table inet smk_egress {")
    print("  chain out {")
    print(f"    type filter hook output priority 0; policy drop;")
    print("    # loopback + LAN management always allowed")
    print("    ip daddr 127.0.0.0/8 accept")
    print("    ip6 daddr ::1/128 accept")
    print("    # declared estate egress")
    for e in entries:
        print(f"    ip daddr {e} accept")
    print("    # everything else: refused at kernel level")
    print("    log prefix \"SMK-EGRESS-BLOCK \" counter drop")
    print("  }")
    print("}")
    print(f"# {len(entries)} estate entr{'y' if len(entries) == 1 else 'ies'} · "
          "estates must be IP/CIDR for nft (resolve domains before applying)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(prog="smk gateway")
    sub = ap.add_subparsers(dest="action")
    for a in ("start", "stop", "status"):
        p = sub.add_parser(a)
        p.add_argument("--port", type=int, default=DEFAULT_PORT)
    nd = sub.add_parser("netdist")
    nd.add_argument("--target")
    nd.add_argument("--iface", default=None)
    nd.add_argument("--out", default="netdist.rules")
    ap.add_argument("--port", type=int, default=DEFAULT_PORT)
    ap.add_argument("--serve", type=int, default=0, help=argparse.SUPPRESS)
    args = ap.parse_args()
    if args.serve:
        _serve(args.serve)
        return 0
    if not args.action:
        ap.print_help()
        return 2
    if args.action != "netdist":
        args.port = args.port
    default_args = argparse.Namespace(action=args.action, port=args.port,
                                      target=getattr(args, "target", None),
                                      iface=getattr(args, "iface", None),
                                      out=getattr(args, "out", "netdist.rules"))
    return cmd_gateway(default_args)


if __name__ == "__main__":
    sys.exit(main())