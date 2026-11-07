#!/usr/bin/env python3
"""
LEAKSCAN — SPYDERMONKEY v7.2: the no-leaks gate.

Engagement data NEVER ships. This scans the repo (tracked files + optional
--history for every blob ever committed) for engagement markers derived from
the runtime case registry + a static core list, and exits 1 on any hit.
Run it before every push:  python3 scripts/leakscan.py
CI truth: wired into selftest + ci_smoke.sh. stdlib-only.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def _markers() -> list[str]:
    """The curated no-leak list — single source of truth:
    references/leak-markers.json (leakscan + skilltree sanitizer both read it)."""
    try:
        doc = json.loads((ROOT / "references" / "leak-markers.json").read_text())
        return list(doc.get("markers", []))
    except Exception:
        return list(CORE_FALLBACK)


CORE_FALLBACK = [
    "g***REDACTED***", "i***REDACTED***", "s***REDACTED***", "x***REDACTED***", "e***REDACTED***",
    "p***REDACTED***", "d***REDACTED***", "g***REDACTED***", "l***REDACTED***", "c***REDACTED***", "a***REDACTED***",
    "a***REDACTED***", "g***REDACTED***", "f***REDACTED***", "j***REDACTED***", "d***REDACTED***",
]


def _tracked_files() -> list[str]:
    r = subprocess.run(["git", "-C", str(ROOT), "ls-files"],
                       capture_output=True, text=True)
    return [f for f in r.stdout.splitlines() if f]


def scan_worktree() -> dict:
    markers = _markers()
    rx = re.compile("|".join(re.escape(m) for m in markers), re.I)
    hits = {}
    # the gate + generator carry the marker LIST as code/config — that is a
    # reference to the markers, not engagement data; scanning them would
    # always self-flag
    GATE_FILES = {"scripts/leakscan.py", "scripts/skilltree.py",
                  "references/leak-markers.json"}
    for f in _tracked_files():
        if f in GATE_FILES:
            continue
        try:
            data = open(ROOT / f, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        found = sorted({m.group(0).lower() for m in rx.finditer(data)})
        if found:
            hits[f] = found
    return {"markers": len(markers), "files": len(_tracked_files()),
            "leaks": hits}


def scan_history() -> dict:
    """Pickaxe every marker across full history — catches blobs in old commits."""
    markers = _markers()
    leaks = {}
    for m in markers:
        r = subprocess.run(
            ["git", "-C", str(ROOT), "log", "--all", "-S", m,
             "--exit-code", "--oneline", "--", "."],
            capture_output=True, text=True)
        if r.returncode == 0:  # 0 = match found
            leaks[m] = r.stdout.splitlines()[:3]
    return {"leaks": leaks}


def main() -> int:
    history = "--history" in sys.argv
    w = scan_worktree()
    payload = {"mode": "history+worktree" if history else "worktree",
               "worktree": w}
    ok = not w["leaks"]
    if history and ok:
        h = scan_history()
        payload["history"] = h
        ok = not h["leaks"]
    if os.environ.get("LEAKSCAN_JSON") or "--json" in sys.argv:
        print(json.dumps(payload, indent=1))
    else:
        print(f"═══ LEAKSCAN — {w['markers']} markers × {w['files']} files ═══")
        if w["leaks"]:
            for f, found in list(w["leaks"].items())[:10]:
                print(f"  ✗ {f}: {','.join(found)}")
            print(f"  {len(w['leaks'])} leaking file(s)")
        else:
            print("  ✓ worktree clean — no engagement data ships")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
