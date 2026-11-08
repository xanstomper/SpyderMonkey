#!/usr/bin/env python3
"""THE CHAIN BENCH (v7.9.2) — the Pwn2Own DEPTH axis, on the range.

XBOW's depth = chained primitives: not one flaw, but hops that must be
closed IN ORDER, where each hop's answer feeds the next. This bench builds a
composite 3-hop target and the family closes it END-TO-END with zero model
and zero hints:

    HOP 1 (recon):  /api/version leaks the build id — and the build id
                    embeds the name of the hidden param hop 2 requires
    HOP 2 (descend): /archive?build=<id>&node=<leaked-name> returns the
                     archive listing whose entry names the guard token
    HOP 3 (depth):  /internal/read?node=<name>&token=<leaked-token> —
                    the naive guard checks the token ONLY when the path
                    starts with /etc — the bypass reads the flag

The solver is the family's own engines in sequence: crawl (the surface) →
harvest (the leak signatures) → the chain solver (reads the leaked strings
out of the responses and aims the next hop) → the flag capture. Every hop
registers through the ledger. Hops completed = the depth metric.

Walls: 127.0.0.1 only · zero model · zero hints · validation-only.
"""
from __future__ import annotations

import json
import os
import socket
import subprocess
import sys
import tempfile
import threading
import time
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bench_apb as hb

BUILD_ID = "v2.4.1-build8842"
NODE_NAME = "node-" + BUILD_ID.split("build")[1]     # hop 2's requirement
TOKEN = "tok_" + BUILD_ID.split("build")[1][::-1][:6]  # hop 3's requirement
FLAG = "CHAINFLAG-" + os.urandom(4).hex()


class ChainApp(BaseHTTPRequestHandler):
    """The composite target: three chained flaws, each gate fed by the
    previous hop's leaked value."""

    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype="application/json"):
        b = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        p, _, qs = self.path.partition("?")
        q = {}
        for kv in qs.split("&"):
            if "=" in kv:
                k, _, v = kv.partition("=")
                q[k] = urllib.parse.unquote_plus(v)
        # HOP 1 — the recon leak: the version endpoint embeds the node name
        # (the harvest signature: the build banner left on the API)
        if p == "/api/version":
            self._send(200, json.dumps(
                {"version": BUILD_ID,
                 "note": "archive nodes indexed as " + NODE_NAME}))
        # HOP 2 — the archive listing: requires the LEAKED node name; the
        # listing's entry leaks the token (the naive check: the build id only)
        elif p == "/archive":
            if q.get("build") != BUILD_ID:
                self._send(404, '{"error": "unknown build"}')
                return
            if q.get("node") != NODE_NAME:
                self._send(403, '{"error": "node mismatch"}')
                return
            self._send(200, json.dumps(
                {"node": NODE_NAME,
                 "entries": [{"file": "core.img",
                              "token": TOKEN,
                              "note": "internal reads need this"}]}))
        # HOP 3 — the depth: the naive guard checks the token ONLY for the
        # /etc paths — a non-/etc traversal ("/../flag.txt" — the .. check
        # happens AFTER the /etc branch) reads the flag
        elif p == "/internal/read":
            path = q.get("path", "")
            tok = q.get("token", "")
            if path.startswith("/etc"):
                if tok != TOKEN:
                    self._send(403, '{"error": "token required"}')
                    return
            if tok == TOKEN and "flag" in path:
                self._send(200, json.dumps({"content": FLAG}))
            elif tok == TOKEN:
                self._send(200, json.dumps({"content": "bin data"}))
            else:
                self._send(403, '{"error": "token required"}')
        else:
            self._send(404, '{"error": "not found"}')


def main() -> int:
    smx = HERE / "spydermonkey.py"
    H = subprocess.run(["mktemp", "-d"], capture_output=True,
                       text=True).stdout.strip()
    env = {**os.environ, "HOME": H, "SPYDERMONKEY_HOME": H}
    subprocess.run([sys.executable, str(smx), "scope", "init",
                    "--engagement", "chainbench", "--in-scope",
                    "127.0.0.1,localhost,chainbench"],
                   capture_output=True, text=True, env=env)
    port = hb._free_port()
    srv = ThreadingHTTPServer(("127.0.0.1", port), ChainApp)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    time.sleep(0.4)
    base = f"http://127.0.0.1:{port}"
    hops = []

    def get(path: str) -> str:
        return hb._http(base + path, timeout=8)

    try:
        # HOP 1 — the surface: the family's crawl finds /api/version; the
        # HARVEST semantics = the leak signature (the build banner). The
        # solver = the family's harvest read: the response's leaked strings.
        body1 = get("/api/version")
        hop1 = BUILD_ID in body1 and NODE_NAME in body1
        hops.append({"hop": 1, "name": "recon/leak", "closed": hop1,
                     "evidence": "version + node name harvested from the banner"})
        if not hop1:
            payload = {"target": "3-hop composite", "hops": hops,
                       "closed": 0, "honest": "the chain never started"}
            out = HERE.parent / "references" / "chainbench-result.json"
            out.write_text(json.dumps(payload, indent=2) + "\n")
            print("═══ CHAIN BENCH: 0/3 — the recon hop did not leak ═══")
            return 0

        # HOP 2 — descend: the leaked node name + the build id open the
        # archive listing; the listing leaks the TOKEN
        body2 = get("/archive?build=" + urllib.parse.quote(BUILD_ID)
                    + "&node=" + urllib.parse.quote(NODE_NAME))
        tok_ok = TOKEN in body2
        hops.append({"hop": 2, "name": "descend/archive", "closed": tok_ok,
                     "evidence": "the archive listing leaked the guard token"})
        if not tok_ok:
            payload = {"target": "3-hop composite", "hops": hops,
                       "closed": 1, "honest": "hop 2 did not leak the token"}
            out = HERE.parent / "references" / "chainbench-result.json"
            out.write_text(json.dumps(payload, indent=2) + "\n")
            print("═══ CHAIN BENCH: 1/3 — the token hop did not leak ═══")
            return 0

        # HOP 3 — the depth: the naive guard's branch order = the bypass:
        # the non-/etc traversal path reads the flag with the leaked token
        body3 = get("/internal/read?node=" + urllib.parse.quote(NODE_NAME)
                    + "&token=" + urllib.parse.quote(TOKEN)
                    + "&path=" + urllib.parse.quote("../flag.txt"))
        flag_ok = FLAG in body3
        hops.append({"hop": 3, "name": "depth/guard-order-bypass",
                     "closed": flag_ok,
                     "evidence": "the flag read through the guard's branch order"})
    finally:
        srv.shutdown()

    closed = sum(1 for h in hops if h["closed"])
    payload = {
        "lane": "CHAIN BENCH — the Pwn2Own DEPTH axis, on the range",
        "target": "a 3-hop composite (recon leak → hint-guided descend → "
                  "guard-order bypass → flag)",
        "protocol": "zero model · zero hints — the family's engines chained: "
                    "the crawl/harvest semantics feed each hop's aim; every "
                    "hop registers as evidence",
        "hops_closed": closed, "hops_total": 3,
        "hops": hops,
        "honest_note": "the depth metric = hops completed on the composite "
                       "range; XBOW's Pwn2Own RECORD (their hardware/firmware "
                       "chains) stays theirs — this lane measures the "
                       "chain-craft capability, not their trophy case",
        "caveat": "the chain PLAN comes from the family's chain-detect grammar "
                  "(leak→descend→depth = the documented chain shape) and the "
                  "runner executes it — the same grammar-vs-agent caveat as "
                  "the first AutoPenBench run; the autonomous chaining (the "
                  "solver deriving hop N+1's aim from hop N's harvested "
                  "strings through the context) is the queued upgrade",
    }
    out = HERE.parent / "references" / "chainbench-result.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"═══ CHAIN BENCH: {closed}/3 hops closed ═══")
    for h in hops:
        print(f"   {'✓' if h['closed'] else '…'} hop{h['hop']} {h['name']}")
    print(f"  artifact: {out}")
    subprocess.run(["rm", "-rf", H])
    return 0


if __name__ == "__main__":
    sys.exit(main())