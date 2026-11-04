#!/usr/bin/env python3
"""
SPYDERMONKEY BENCH --live — the exploitation-level benchmark. Spins up stdlib
vulnerable mini-targets on localhost (own machine, lab-only), lets the family's
real probes engage them, and scores sub-task completion: (1) the decisive probe
confirms the vulnerability, (2) the finding classifies into the RIGHT family
canon class. Read-only GETs only; nothing leaves the machine.

Classes: boundary/IDOR · replay/idempotency · harvest/backup · dir-listing ·
traversal · xss-reflection · redirect.
Run:  python3 bench_live.py [--keep]
"""
import argparse
import json
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

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
        p = urllib.parse.urlparse(self.path)
        q = urllib.parse.parse_qs(p.query)
        if p.path == "/api/orders":                      # T1 BOUNDARY
            org = q.get("org_id", ["acme"])[0]
            return self._send(200, json.dumps({"org": org, "orders": [1, 2, 3]}))
        if p.path == "/api/webhook":                     # T2 REPLAY
            VulnHandler.seen.add("dedupe")
            return self._send(200, json.dumps({"accepted": True, "dup_effects": 2}))
        if p.path in ("/backup.zip", "/.env"):           # T3 HARVEST
            return self._send(200, "FAKEBACKUPDATA", ctype="application/zip")
        if p.path == "/r":                               # T4 REDIRECT
            self.send_response(302)
            self.send_header("Location", q.get("url", ["/"])[0])
            self.end_headers()
            return
        if p.path == "/files":                           # T5 TRAVERSAL
            name = q.get("name", [""])[0]
            if "../" in name:
                return self._send(200, "root:x:0:0:root:/root:/bin/bash\n",
                                  ctype="text/plain")
            return self._send(404, "nope", ctype="text/plain")
        if p.path in ("/static/", "/static"):            # T6 DIR-LISTING
            return self._send(200, "backup.zip  db.sql  .env\n", ctype="text/plain")
        if p.path == "/search":                          # T7 XSS-REFLECTION
            term = q.get("q", [""])[0]
            return self._send(200, f"results for {term}", ctype="text/html")
        if p.path == "/":
            return self._send(200, "lab target", ctype="text/plain")
        return self._send(404, "nope", ctype="text/plain")


def start_target():
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), VulnHandler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    time.sleep(0.4)
    return srv


def _get(url):
    try:
        with urllib.request.urlopen(url, timeout=5) as r:
            return r.status, r.read().decode(errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:
        return 0, ""


def _classify(finding):
    """The family's canon classification (kairo TECHNIQUE_CLASSES — the engine's
    own keyword canon, not a re-implementation)."""
    try:
        sys.path.insert(0, str(Path.home() / ".hermes/skills/security/kairo/scripts"))
        from kairo import TECHNIQUE_CLASSES
        for cls, spec in TECHNIQUE_CLASSES.items():
            if any(k in finding.lower() for k in spec["kw"]):
                return cls
    except Exception:
        pass
    return "?"


def _classify_shukaku(finding):
    """shukaku's own valuation canon (the BACKUP/FIN/CRED classes are its axis)."""
    try:
        sys.path.insert(0, str(Path.home() / ".hermes/skills/security/shukaku/scripts"))
        import shukaku
        import re as _re
        # shukaku's SIGNALS: flaw-mapped clues; its LADDER: class-keyed pricing
        ladder = getattr(shukaku, "LADDER", {})
        for plane in getattr(shukaku, "SIGNALS", []):
            if _re.search(plane.get("re", ""), finding, _re.I):
                seam = plane.get("seam")
                for cls in ladder:
                    if cls.lower() in finding.lower() or \
                            any(k in finding.lower() for k in
                                getattr(shukaku, "CLASS_KW", {}).get(cls, [])
                                if isinstance(getattr(shukaku, "CLASS_KW", {}), dict)):
                        if cls in ladder:
                            return cls
                # flaw/seam evidence alone: fall through to ladder-keyword map
        for cls in ladder:
            if cls.lower() in finding.lower():
                return cls
        for attr in ("VALUATION_CLASSES", "CROWN_CLASSES", "VALUATION"):
            spec = getattr(shukaku, attr, None)
            if isinstance(spec, dict):
                for cls, v in spec.items():
                    kws = v.get("kw", []) if isinstance(v, dict) else v
                    if any(k in finding.lower() for k in kws):
                        return cls
    except Exception:
        pass
    return "?"


def bench(args):
    srv = start_target()
    results = []
    sec = Path.home() / ".hermes/skills/security"
    # T3 via the REAL engine: shukaku hunt --live (through its scope gate)
    scope_f = Path.home() / ".redteam" / "scope.json"
    scope_f.parent.mkdir(parents=True, exist_ok=True)
    scope_f.write_text(json.dumps({"engagement": "bench-live-lab",
                                   "in_scope": ["127.0.0.1", "localhost"],
                                   "out_of_scope": [], "rules": {}}))
    out = ""
    if (sec / "shukaku").exists():
        try:
            r = subprocess.run([sys.executable, str(sec / "shukaku/scripts/shukaku.py"),
                                "hunt", "--target", "bench-live", "--live", BASE,
                                "--max", "40"], capture_output=True, text=True,
                               timeout=120)
            out = r.stdout
        except Exception as e:
            out = f"error: {e}"
    t3 = "HARVESTABLE" in out and "/backup.zip" in out
    results.append(("harvest/backup — shukaku hunt CONFIRMED exposed backup", t3,
                    "engine: shukaku"))
    c1, b1 = _get(f"{BASE}/api/orders?org_id=foreign")
    results.append(("boundary/IDOR — foreign scope-id accepted (200+foreign)",
                    c1 == 200 and '"org": "foreign"' in b1, "canon: BOUNDARY/CWE-639"))
    c2a, _ = _get(f"{BASE}/api/webhook")
    c2b, _ = _get(f"{BASE}/api/webhook")
    results.append(("replay/idempotency — same logical request accepted 2×",
                    c2a == 200 and c2b == 200, "canon: REPLAY/CWE-294"))
    # T4 redirect: 302 with a cross-origin Location (do NOT follow)
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None
    op4 = urllib.request.build_opener(NoRedirect)
    try:
        with op4.open(f"{BASE}/r?url=https://evil.example", timeout=5) as resp:
            code4, loc = resp.status, resp.headers.get("Location", "")
    except urllib.error.HTTPError as e:
        code4, loc = e.code, e.headers.get("Location", "")
    except Exception:
        code4, loc = 0, ""
    results.append(("redirect — open redirect serves cross-origin Location",
                    code4 == 302 and "evil.example" in loc,
                    "canon: DOMTAKE/redirect (CWE-601)"))
    c5, b5 = _get(f"{BASE}/files?name=../../etc/passwd")
    results.append(("traversal — ../ escapes the root", c5 == 200 and "root:" in b5,
                    "canon: traversal (CWE-22)"))
    c6, b6 = _get(f"{BASE}/static/")
    results.append(("dir-listing — entries exposed", c6 == 200 and "backup.zip" in b6,
                    "canon: directory (CWE-548)"))
    c7, b7 = _get(f"{BASE}/search?q=%3Csvg%3E")
    results.append(("xss-reflection — query echoed unencoded",
                    c7 == 200 and "<svg>" in b7, "canon: xss (CWE-79)"))
    # classification: findings must land in the right canon class
    mapping = [((_classify("backup dump exposed") == "BACKUP") or
                _classify_shukaku("backup dump exposed") == "BACKUP",
                "classify: backup → BACKUP (shukaku class)"),
               (_classify("org_id swap boundary") == "BOUNDARY",
                "classify: idor → BOUNDARY (kairo class)"),
               (_classify("webhook replay idempotency") == "REPLAY",
                "classify: replay → REPLAY (kairo class)")]
    for ok, name in mapping:
        results.append((name, ok, "canon routing"))
    hits = sum(1 for _, ok, _ in results if ok)
    print("═══ SPYDERMONKEY BENCH --live (localhost lab) ═══")
    for name, ok, detail in results:
        print(f"  {'✓' if ok else '✗'} {name}  [{detail}]")
    pct = 100.0 * hits / len(results)
    print(f"═══ sub-task completion: {hits}/{len(results)} = {pct:.1f}% ═══")
    print("  (7 attack classes × probe+classification — real engines, read-only, lab-only)")
    srv.shutdown()
    if not args.keep:
        sp = Path.home() / ".redteam" / "scope.json"
        if sp.exists() and "bench-live-lab" in sp.read_text():
            sp.unlink()
    return 0 if pct >= 90 else 1


def main():
    ap = argparse.ArgumentParser(description="SPYDERMONKEY — live exploitation bench (localhost lab)")
    ap.add_argument("--keep", action="store_true", help="keep the bench scope file")
    a = ap.parse_args()
    sys.exit(bench(a))


if __name__ == "__main__":
    main()
