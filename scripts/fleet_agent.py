#!/usr/bin/env python3
"""SPYDERMONKEY FLEET AGENT — the node-side runner of THE FLEET LANE (v7.5).

A real agent ↔ controller loop: a node runs this agent, the controller queues
tasks, the agent executes them in a NODE-LOCAL SPYDERMONKEY_HOME and returns
results in the kernel result schema. Two modes:

  fleet_agent.py agent    --controller URL [--token T] [--interval 30]
                          beacon mode: poll /task?node=N, run, POST /result
  fleet_agent.py agent    --serve PORT [--token T]
                          listener mode: wait for POST /task, run, POST back
  fleet_agent.py controller --port P --node-dir DIR [--token T]
                          the control plane: task queue + result store.

WALLS: the agent REFUSES to run without a node scope (--home must contain
scope.json), every task executes with that node-local home, and every family
engine re-checks the shared scope authority at execution — belt and braces.
stdlib only; tasks are the dispatcher's own argv, results are absorb-ready.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import threading
import time
import urllib.request
import urllib.error
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

DISPATCHER = Path(__file__).resolve().parent / "spydermonkey.py"


def _http_json(url: str, payload=None, token: str | None = None,
               timeout: int = 30) -> dict:
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data,
                                 method="POST" if data else "GET")
    req.add_header("Content-Type", "application/json")
    if token:
        req.add_header("X-Fleet-Token", token)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def _run_task(home: Path, task: dict, timeout: int = 600) -> dict:
    """Execute ONE queued task under the node home. The task command is the
    dispatcher's argv WITHOUT the interpreter prefix; results match the
    kernel result schema (absorb ingests them)."""
    cmd = task.get("command") or task.get("cmd") or []
    if not isinstance(cmd, list) or not cmd:
        return {"task_id": task.get("id", "?"), "ok": False, "rc": 2,
                "output": "task carries no command list"}
    env = {**os.environ, "SPYDERMONKEY_HOME": str(home)}
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, str(DISPATCHER)] + cmd,
                           capture_output=True, text=True, timeout=timeout,
                           env=env)
        out = r.stdout + r.stderr
        rc = r.returncode
    except subprocess.TimeoutExpired:
        out, rc = f"task timed out after {timeout}s", 1
    except Exception as e:
        out, rc = f"task crashed: {e}", 1
    return {"task_id": task.get("id", "?"), "node": task.get("node", ""),
            "command": cmd, "ok": rc == 0, "rc": rc, "output": out[:200_000],
            "elapsed": round(time.time() - t0, 2)}


class _Controller(BaseHTTPRequestHandler):
    def _reply(self, code: int, payload: dict):
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _auth(self) -> bool:
        tok = getattr(self.server, "token", None)
        if not tok:
            return True
        return self.headers.get("X-Fleet-Token", "") == tok

    def do_GET(self):
        if not self._auth():
            return self._reply(403, {"error": "bad token"})
        if self.path.startswith("/task"):
            node = self.path.split("?", 1)[1].split("=")[1] if "=" in self.path else ""
            qd = self.server.queue
            nxt = None
            with self.server.lock:
                if qd and (not node or node in str(qd[0].get("node", ""))):
                    nxt = qd.pop(0)
            if nxt:
                nxt["state"] = "taken"
                self.server.inflight.append(nxt)
            return self._reply(200, nxt or {})
        if self.path.startswith("/status"):
            return self._reply(200, {"queue": len(self.server.queue),
                                     "inflight": len(self.server.inflight)})
        return self._reply(404, {"error": "unknown route"})

    def do_POST(self):
        if not self._auth():
            return self._reply(403, {"error": "bad token"})
        ln = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(ln).decode("utf-8", "replace"))
        except Exception:
            return self._reply(400, {"error": "bad json"})
        if self.path.startswith("/task"):
            node = body.get("node", "")
            if not body.get("command"):
                return self._reply(400, {"error": "task needs a command"})
            with self.server.lock:
                self.server.queue.append({"id": body.get("id") or f"T{len(self.server.queue)+1}",
                                          "node": node, "command": body["command"],
                                          "state": "queued"})
            return self._reply(201, {"queued": True, "queue": len(self.server.queue)})
        if self.path.startswith("/result"):
            node = body.get("node", "")
            with self.server.lock:
                self.server.inflight[:] = [t for t in self.server.inflight
                                           if t.get("id") != body.get("task_id")]
            outdir = Path(self.server.node_dir) / (node or "anon")
            outdir.mkdir(parents=True, exist_ok=True)
            f = outdir / f"{body.get('task_id', 'result')}.json"
            f.write_text(json.dumps(body, indent=2) + "\n")
            return self._reply(200, {"saved": str(f)})
        return self._reply(404, {"error": "unknown route"})


def cmd_controller(args):
    node_dir = Path(args.node_dir)
    node_dir.mkdir(parents=True, exist_ok=True)
    srv = ThreadingHTTPServer(("127.0.0.1", args.port), _Controller)
    srv.queue, srv.inflight, srv.lock = [], [], threading.Lock()
    srv.node_dir, srv.token = str(node_dir), args.token
    print(f"▸ fleet controller on 127.0.0.1:{args.port} · queue in {node_dir}",
          flush=True)
    if args.once:
        srv.handle_request()
        return 0
    srv.serve_forever()


def cmd_agent(args):
    home = Path(args.home or "~/.redteam-node").expanduser()
    home.mkdir(parents=True, exist_ok=True)
    if not (home / "scope.json").exists():
        print("✗ REFUSED — node has no scope authority; the agent never runs "
              "ungated (copy the node's scope.json into the node home first)",
              file=sys.stderr)
        return 1
    if args.serve:
        srv = ThreadingHTTPServer(("127.0.0.1", args.serve), _Controller)
        srv.queue, srv.inflight, srv.lock = [], [], threading.Lock()
        srv.node_dir, srv.token = str(home), "node-local"
        print(f"▸ fleet agent (serve) on 127.0.0.1:{args.serve} · home {home}",
              flush=True)
        # standalone node: the listener queues, this loop executes
        def _self_poll():
            base = f"http://127.0.0.1:{args.serve}"
            while True:
                try:
                    task = _http_json(f"{base}/task?node={home.name}",
                                      timeout=5)
                    if task and task.get("command"):
                        result = _run_task(home, task)
                        result["node"] = home.name
                        try:
                            _http_json(f"{base}/result", payload=result,
                                       timeout=10)
                            print(f"✓ {result['task_id']} rc={result['rc']}",
                                  flush=True)
                        except Exception as e:
                            print(f"✗ result post failed: {e}", flush=True)
                except Exception:
                    pass
                time.sleep(1)
        threading.Thread(target=_self_poll, daemon=True).start()
        srv.serve_forever()
        return 0
    url = args.controller.rstrip("/")
    print(f"▸ fleet agent (beacon) → {url} · interval {args.interval}s · "
          f"home {home}", flush=True)
    while True:
        try:
            task = _http_json(f"{url}/task?node={home.name}", token=args.token,
                              timeout=10)
            if task and task.get("command"):
                result = _run_task(home, task)
                result["node"] = home.name
                try:
                    _http_json(f"{url}/result", payload=result,
                               token=args.token, timeout=15)
                    print(f"✓ {result['task_id']} rc={result['rc']} "
                          f"({result['elapsed']}s)", flush=True)
                except Exception as e:
                    print(f"✗ result post failed: {e}", flush=True)
        except Exception:
            time.sleep(args.interval)
            continue
        time.sleep(args.interval)


def main() -> int:
    ap = argparse.ArgumentParser(prog="fleet_agent", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("controller", help="the control plane (task queue + results)")
    c.add_argument("--port", type=int, default=9440)
    c.add_argument("--node-dir", default=str(Path.home() / ".redteam" / "fleet-nodes"))
    c.add_argument("--token")
    c.add_argument("--once", action="store_true", help="handle ONE request then exit (tests)")
    a = sub.add_parser("agent", help="the node-side runner")
    a.add_argument("--controller", help="beacon mode: controller base URL")
    a.add_argument("--serve", type=int, help="listener mode: local port")
    a.add_argument("--token")
    a.add_argument("--interval", type=int, default=30)
    a.add_argument("--home")
    args = ap.parse_args()
    if args.cmd == "controller":
        return cmd_controller(args)
    return cmd_agent(args)


if __name__ == "__main__":
    sys.exit(main())