"""Tests for the industrial ops extensions: jail security, scope gateway,
density scorecard, ticket interface. All offline/lab — nothing leaves the
box and nothing real is touched (scratch HOME throughout).
"""

import json
import os
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _run(args, env=None, cwd=None, inp=None, timeout=120):
    return subprocess.run([sys.executable, str(ROOT / "scripts" / "spydermonkey.py")]
                          + args, capture_output=True, text=True,
                          cwd=cwd or ROOT, stdin=subprocess.DEVNULL,
                          timeout=timeout, env=env, input=inp)


class JailTests(unittest.TestCase):
    def test_jail_arm_check_roundtrip_and_tamper(self):
        home = tempfile.mkdtemp(prefix="sm-jail-")
        env = dict(os.environ)
        env["HOME"] = home  # supervised ~/.claude paths resolve to scratch
        try:
            r = _run(["jail", "arm"], env=env)
            self.assertEqual(r.returncode, 0, r.stderr)
            r = _run(["jail", "check"], env=env)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            # tamper: create a supervised file that was absent at arm time
            fake = Path(home) / ".claude" / "settings.json"
            fake.parent.mkdir(parents=True)
            fake.write_text("{}", encoding="utf-8")
            r = _run(["jail", "check"], env=env)
            self.assertEqual(r.returncode, 1, "tamper must be detected")
            self.assertIn("TAMPERED", r.stdout)
        finally:
            import shutil
            shutil.rmtree(home, ignore_errors=True)


class GatewayTests(unittest.TestCase):
    def test_gateway_blocks_out_of_estate_at_transport(self):
        home = tempfile.mkdtemp(prefix="sm-gw-")
        env = dict(os.environ)
        env["SPYDERMONKEY_HOME"] = home
        r = _run(["scope", "init", "--engagement", "gw",
                  "--in-scope", "example.com"], env=env)
        self.assertEqual(r.returncode, 0, r.stderr)
        port = 8921
        # reliability: ephemeral port — fixed ports flake under parallel load
        probe = socket.socket()
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
        probe.close()
        srv = subprocess.Popen(
            [sys.executable, str(ROOT / "scripts" / "scope_gateway.py"),
             "--serve", str(port)],
            env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL)
        try:
            import time
            time.sleep(1.0)
            # out-of-estate CONNECT → 403
            code, body = self._connect(port, "evil.example", 443)
            self.assertEqual(code, 403)
            # in-estate CONNECT → 200 (tunnel allowed; no real TLS needed)
            code, body = self._connect(port, "example.com", 443)
            self.assertEqual(code, 200)
        finally:
            srv.terminate()
            srv.wait(timeout=10)
            import shutil
            shutil.rmtree(home, ignore_errors=True)

    @staticmethod
    def _connect(port, host, hport):
        s = socket.create_connection(("127.0.0.1", port), timeout=5)
        s.sendall(f"CONNECT {host}:{hport} HTTP/1.1\r\nHost: {host}:{hport}\r\n\r\n"
                  .encode())
        data = b""
        while b"\r\n\r\n" not in data:
            chunk = s.recv(512)
            if not chunk:
                break
            data += chunk
        s.close()
        line = data.split(b"\r\n", 1)[0].decode("latin-1", "replace")
        return int(line.split(" ")[1]), data


class TicketTests(unittest.TestCase):
    def test_ticket_dry_run_lists_only_confirmed(self):
        home = tempfile.mkdtemp(prefix="sm-tkt-")
        camp = Path(home) / "campaigns" / "demo"
        camp.mkdir(parents=True)
        rows = [
            {"id": "001", "title": "IDOR", "asset": "https://demo.test/p",
             "status": "CONFIRMED", "severity": "high", "class": "BOUNDARY"},
            {"id": "002", "title": "Open redirect", "asset": "https://demo.test/r",
             "status": "hypothesis", "severity": "medium", "class": "REDIRECT"},
        ]
        (camp / "ledger.jsonl").write_text(
            "\n".join(json.dumps(r) for r in rows), encoding="utf-8")
        env = dict(os.environ)
        env["SPYDERMONKEY_HOME"] = home
        r = _run(["ticket", "--target", "demo", "--dry-run"], env=env)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("SPY-001", r.stdout)
        self.assertNotIn("SPY-002", r.stdout)


class DensityTests(unittest.TestCase):
    def test_density_scorecard_parses(self):
        r = _run(["density", "--json"], timeout=300)
        self.assertEqual(r.returncode, 0, r.stderr)
        d = json.loads(r.stdout)
        self.assertIn("findings_per_hour", d)
        self.assertIn("confirmed", d)
        self.assertGreaterEqual(d["total"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)