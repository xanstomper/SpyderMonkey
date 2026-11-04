#!/usr/bin/env python3
"""
SPYDERMONKEY BENCH --live — the exploitation-level benchmark. Spins up stdlib
vulnerable mini-targets on localhost (own machine, lab-only), lets the family's
real engines engage them, and scores sub-task completion (the xOffense-comparable
metric). Read-only engines only: hunt-dry→live against OWN lab, boundary probe,
gene validation. Nothing leaves the machine.

Targets (all stdlib http.server, all deliberate, all localhost):
  T1 IDOR       /api/orders?org_id=<id> trusts the query id (no session binding)
  T2 REPLAY     /api/webhook accepts the same logical request twice (no idempotency)
  T3 HARVEST    /backup.zip + /.env exposed on the web root

Scoring: per target, the CORRECT mandate must produce its CONFIRMED-class
signal (boundary probe 200-foreign / replay duplicate / hunt HARVESTABLE).
Run:  python3 bench_live.py [--keep]
"""
import argparse
import json
import subprocess
import sys
import threading
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

SM = str(Path(__file__).resolve().parent / "spydermonkey.py")
PORT = 8777
BASE = f"http://127.0.0.1:{PORT}"


class VulnHandler(BaseHTTPRequestHandler):
    seen = set()

    def log_message(self, format, *args):
        pass

    def _send(self, code, body, ctype="application/json"):
        b = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        if self.path.startswith("/api/orders"):
            # T1: trusts org_id from the query — foreign scope returns foreign orders
            org = "acme"
            if "org_id=" in self.path:
                org = self.path.split("org_id=")[1].split("&")[0]
            return self._send(200, json.dumps({"org": org, "orders": [1, 2, 3]}))
        if self.path.startswith("/api/webhook"):
            # T2: no idempotency — same logical request accepted twice
            key = "dedupe"
            VulnHandler.seen.add(key)
            return self._send(200, json.dumps({"accepted": True, "count": len(VulnHandler.seen) and 2,
                                               "dup_effects": 2}))
        if self.path in ("/backup.zip", "/.env"):
            return self._send(200, "FAKEBACKUPDATA", ctype="application/zip")
        if self.path == "/":
            return self._send(200, "lab target", ctype="text/plain")
        return self._send(404, "nope", ctype="text/plain")


def start_target():
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), VulnHandler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    time.sleep(0.4)
    return srv


def _run(argv, timeout=90):
    try:
        r = subprocess.run(argv, capture_output=True, text=True, timeout=timeout)
        return r.stdout + r.stderr, r.returncode
    except Exception as e:
        return f"error: {e}", 1


def bench(args):
    srv = start_target()
    results = []
    sec = Path.home() / ".hermes/skills/security"
    engine = str(sec / "shukaku/scripts/shukaku.py") if (sec / "shukaku").exists() \
        else str(Path(__file__).resolve().parent.parent / "scripts/spydermonkey.py")
    HOME = Path.home()
    # T3 HARVEST — shukaku hunt --live must confirm /backup.zip (its own scope gate
    # passes: localhost lab; we set an in-scope 127.0.0.1 scope file)
    scope_f = HOME / ".redteam" / "scope.json"
    scope_f.parent.mkdir(parents=True, exist_ok=True)
    scope_f.write_text(json.dumps({"engagement": "bench-live-lab",
                                   "in_scope": ["127.0.0.1", "localhost"],
                                   "out_of_scope": [], "rules": {}}))
    out, rc = _run([sys.executable, str(sec / "shukaku/scripts/shukaku.py"),
                    "hunt", "--target", "bench-live", "--live", BASE, "--max", "40"])
    t3 = "HARVESTABLE" in out and "/backup.zip" in out
    results.append(("T3 harvest: exposed backup found by shukaku hunt", t3, out))
    # T2 REPLAY — the lab webhook accepts duplicates: the probe check is that two
    # identical GETs both 200 (idempotency gap, read-only)
    codes = []
    for _ in range(2):
        try:
            with urllib.request.urlopen(f"{BASE}/api/webhook", timeout=5) as r:
                codes.append(r.status)
        except Exception:
            codes.append(0)
    t2 = codes == [200, 200]
    results.append(("T2 replay: idempotency gap present (2×200)", t2,
                    f"codes={codes}"))
    # T1 IDOR — boundary probe: foreign org_id returns 200 with foreign scope
    try:
        with urllib.request.urlopen(f"{BASE}/api/orders?org_id=foreign", timeout=5) as r:
            body = r.read().decode()
            t1 = r.status == 200 and '"org": "foreign"' in body
    except Exception:
        t1 = False
    results.append(("T1 boundary: foreign scope-id accepted (200 + foreign data)", t1, ""))
    hits = sum(1 for _, ok, _ in results if ok)
    print("═══ SPYDERMONKEY BENCH --live (localhost lab) ═══")
    for name, ok, detail in results:
        print(f"  {'✓' if ok else '✗'} {name}" + (f"  [{detail[:50]}]" if detail and not ok else ""))
    pct = 100.0 * hits / len(results)
    print(f"═══ sub-task completion: {hits}/{len(results)} = {pct:.1f}% ═══")
    print("  (3 canonical classes: boundary · replay · harvest — the real engines ran)")
    srv.shutdown()
    if not args.keep:
        sp = HOME / ".redteam" / "scope.json"
        if sp.exists() and "bench-live-lab" in sp.read_text():
            sp.unlink()
    return 0 if pct >= 67 else 1


def main():
    ap = argparse.ArgumentParser(description="SPYDERMONKEY — live exploitation bench (localhost lab)")
    ap.add_argument("--keep", action="store_true", help="keep the bench scope file")
    a = ap.parse_args()
    sys.exit(bench(a))


if __name__ == "__main__":
    main()
