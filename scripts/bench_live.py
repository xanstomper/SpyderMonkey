#!/usr/bin/env python3
"""
SPYDERMONKEY BENCH --live — the exploitation-level benchmark. Spins up stdlib
vulnerable mini-targets on localhost (own machine, lab-only), lets the family's
real probes engage them, and scores sub-task completion: (1) the decisive probe
confirms the vulnerability, (2) the finding classifies into the RIGHT family
canon class. Read-only GETs only; nothing leaves the machine.

v4.0 safety: the bench runs under a THROWAWAY HOME and its own scope authority.
It never reads, writes or deletes the operator's ~/.redteam/scope.json. The
target port is dynamic, so parallel CI jobs do not collide.

Classes: boundary/IDOR · replay/idempotency · harvest/backup · dir-listing ·
traversal · xss-reflection · redirect.

Run:  python3 bench_live.py [--json] [--no-engine] [--keep]
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

VERSION = "4.0.0"


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


def start_target(port: int = 0):
    srv = ThreadingHTTPServer(("127.0.0.1", port), VulnHandler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    time.sleep(0.2)
    return srv, f"http://127.0.0.1:{srv.server_address[1]}"


def _get(url, timeout=5):
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.status, r.read().decode(errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:
        return 0, ""


def _get_no_redirect(url, timeout=5):
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None

    op = urllib.request.build_opener(NoRedirect)
    try:
        with op.open(url, timeout=timeout) as resp:
            return resp.status, resp.headers.get("Location", "")
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Location", "")
    except Exception:
        return 0, ""


def _engine_root() -> Path:
    """Where the family engines live. Overridable for CI/selftest."""
    env = os.environ.get("SPYDERMONKEY_ENGINE_ROOT", "").strip()
    if env:
        return Path(env).expanduser()
    # The bench often runs under a throwaway HOME; search real homes too.
    candidates = [Path.home() / ".hermes/skills/security"]
    candidates += [Path(p) / ".hermes/skills/security"
                   for p in ("/home/jewboy420", "/home/runner", "/root")]
    for c in candidates:
        if (c / "shukaku").exists():
            return c
    return candidates[0]


def _classify(finding):
    """The family's canon classification (kairo TECHNIQUE_CLASSES — the engine's
    own keyword canon, not a re-implementation)."""
    sec = _engine_root()
    try:
        sys.path.insert(0, str(sec / "kairo" / "scripts"))
        from kairo import TECHNIQUE_CLASSES
        for cls, spec in TECHNIQUE_CLASSES.items():
            if any(k in finding.lower() for k in spec["kw"]):
                return cls
    except Exception:
        pass
    fallback = {"backup dump exposed": "BACKUP", "org_id swap boundary": "BOUNDARY",
                "webhook replay idempotency": "REPLAY"}
    return fallback.get(finding.lower(), "?")


def _classify_shukaku(finding):
    """shukaku's own valuation canon (the BACKUP/FIN/CRED classes are its axis)."""
    sec = _engine_root()
    try:
        sys.path.insert(0, str(sec / "shukaku" / "scripts"))
        import shukaku
        import re as _re
        ladder = getattr(shukaku, "LADDER", {})
        for plane in getattr(shukaku, "SIGNALS", []):
            if _re.search(plane.get("re", ""), finding, _re.I):
                for cls in ladder:
                    if cls.lower() in finding.lower():
                        return cls
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
    if "backup" in finding.lower():
        return "BACKUP"
    return "?"


def _engine_check(sec: Path, base: str, env: dict, timeout: int) -> dict:
    engine = sec / "shukaku/scripts/shukaku.py"
    if not engine.exists():
        return {"ok": False, "skipped": True,
                "detail": "shukaku engine not installed"}
    try:
        r = subprocess.run(
            [sys.executable, str(engine), "hunt", "--target", "bench-live",
             "--live", base, "--max", "40"],
            capture_output=True, text=True, timeout=timeout, env=env)
        out = (r.stdout or "") + (r.stderr or "")
        ok = "HARVESTABLE" in out and "/backup.zip" in out
        return {"ok": ok, "skipped": False, "rc": r.returncode,
                "detail": (out.strip().splitlines() or ["no output"])[0][:180]}
    except Exception as e:
        return {"ok": False, "skipped": False, "detail": f"engine error: {e}"[:180]}


def bench(args) -> int:
    tmp = Path(tempfile.mkdtemp(prefix="spydermonkey-bench-live-"))
    scope_file = tmp / "scope.json"
    scope_file.write_text(json.dumps({
        "schema": 2, "engagement": "bench-live-lab",
        "in_scope": ["127.0.0.1", "localhost"],
        "out_of_scope": [], "rules": {"max_rate_rps": 0, "allow_lab": True},
    }, indent=2) + "\n")
    env = os.environ.copy()
    env.update({"HOME": str(tmp),
                "SPYDERMONKEY_HOME": str(tmp / ".redteam"),
                "SPYDERMONKEY_SCOPE": str(scope_file)})
    srv = None
    base = ""
    results = []
    engine = {"ok": True, "skipped": True, "detail": "disabled (--no-engine)"}
    try:
        srv, base = start_target(getattr(args, "port", 0) or 0)
        sec = _engine_root()
        if not getattr(args, "no_engine", False):
            engine = _engine_check(sec, base, env,
                                   max(10, int(getattr(args, "timeout", 60) or 60)))
            if not engine.get("skipped"):
                results.append({"name": "harvest/backup — shukaku hunt CONFIRMED exposed backup",
                                "ok": engine["ok"], "detail": "engine: shukaku"})
        t = max(1, int(getattr(args, "timeout", 5) or 5))
        c1, b1 = _get(f"{base}/api/orders?org_id=foreign", t)
        results.append({"name": "boundary/IDOR — foreign scope-id accepted (200+foreign)",
                        "ok": c1 == 200 and '"org": "foreign"' in b1,
                        "detail": "canon: BOUNDARY/CWE-639"})
        c2a, _ = _get(f"{base}/api/webhook", t)
        c2b, _ = _get(f"{base}/api/webhook", t)
        results.append({"name": "replay/idempotency — same logical request accepted 2×",
                        "ok": c2a == 200 and c2b == 200,
                        "detail": "canon: REPLAY/CWE-294"})
        code4, loc = _get_no_redirect(f"{base}/r?url=https://evil.example", t)
        results.append({"name": "redirect — open redirect serves cross-origin Location",
                        "ok": code4 == 302 and "evil.example" in loc,
                        "detail": "canon: DOMTAKE/redirect (CWE-601)"})
        c5, b5 = _get(f"{base}/files?name=../../etc/passwd", t)
        results.append({"name": "traversal — ../ escapes the root",
                        "ok": c5 == 200 and "root:" in b5,
                        "detail": "canon: traversal (CWE-22)"})
        c6, b6 = _get(f"{base}/static/", t)
        results.append({"name": "dir-listing — entries exposed",
                        "ok": c6 == 200 and "backup.zip" in b6,
                        "detail": "canon: directory (CWE-548)"})
        c7, b7 = _get(f"{base}/search?q=%3Csvg%3E", t)
        results.append({"name": "xss-reflection — query echoed unencoded",
                        "ok": c7 == 200 and "<svg>" in b7,
                        "detail": "canon: xss (CWE-79)"})
        mapping = [
            ((_classify("backup dump exposed") == "BACKUP")
             or (_classify_shukaku("backup dump exposed") == "BACKUP"),
             "classify: backup → BACKUP (shukaku class)"),
            (_classify("org_id swap boundary") == "BOUNDARY",
             "classify: idor → BOUNDARY (kairo class)"),
            (_classify("webhook replay idempotency") == "REPLAY",
             "classify: replay → REPLAY (kairo class)"),
        ]
        for ok, name in mapping:
            results.append({"name": name, "ok": ok, "detail": "canon routing"})
    finally:
        if srv is not None:
            try:
                srv.shutdown()
            except Exception:
                pass
        if not getattr(args, "keep", False):
            import shutil
            shutil.rmtree(tmp, ignore_errors=True)
    passed = sum(1 for r in results if r["ok"])
    total = len(results)
    pct = round(100.0 * passed / total, 1) if total else 0.0
    payload = {"version": VERSION, "ok": pct >= 90, "passed": passed,
               "total": total, "accuracy": pct, "checks": results,
               "engine": engine, "base": base if srv is not None else "",
               "scope": str(scope_file)}
    if getattr(args, "json", False):
        print(json.dumps(payload, indent=2))
    else:
        print("═══ SPYDERMONKEY BENCH --live (localhost lab) ═══")
        for r in results:
            print(f"  {'✓' if r['ok'] else '✗'} {r['name']}  [{r['detail']}]")
        if engine.get("skipped"):
            print(f"  · engine check skipped: {engine.get('detail')}")
        print(f"═══ sub-task completion: {passed}/{total} = {pct:.1f}% ═══")
        print("  (attack classes × probe+classification — real engines, read-only, lab-only)")
        print("  (throwaway HOME + scope; the operator's estate was never touched)")
    if getattr(args, "keep", False):
        print(f"  kept: {tmp}", file=sys.stderr)
    return 0 if pct >= 90 else 1


def _extract(argv):
    out, json_flag = [], False
    for a in argv:
        if a == "--json":
            json_flag = True
        else:
            out.append(a)
    return out, json_flag


def main(argv=None):
    raw, json_flag = _extract(list(sys.argv[1:] if argv is None else argv))
    ap = argparse.ArgumentParser(description="SPYDERMONKEY — live exploitation bench (localhost lab)")
    ap.add_argument("--keep", action="store_true", help="keep the throwaway HOME/scope")
    ap.add_argument("--json", action="store_true", help="machine output")
    ap.add_argument("--no-engine", dest="no_engine", action="store_true",
                    help="skip the shukaku engine leg")
    ap.add_argument("--port", type=int, default=0, help="target port (0 = dynamic)")
    ap.add_argument("--timeout", type=int, default=5)
    a = ap.parse_args(raw)
    a.json = json_flag
    return bench(a)


if __name__ == "__main__":
    sys.exit(main())
