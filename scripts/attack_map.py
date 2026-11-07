#!/usr/bin/env python3
"""
ATTACK_MAP — SPYDERMONKEY v7.0.0: the corpus, indexed against MITRE ATT&CK.

Walks the technique corpus (references/skills/, 179k+ files), matches each
file's class keyword against the skilltree BINDINGS (class → WSTG · CWE ·
ATT&CK), and writes references/attack-coverage.json:

    { total_files, mapped_files, coverage_pct,
      techniques: {T-id: {files, cwes, classes}}, ... }

Also fetches the Atomic Red Team atomics count live for an honest comparison
(the largest public ATT&CK emulation library). Re-run any time:
`python3 scripts/attack_map.py [--no-fetch]`. stdlib-only.
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "references" / "skills"
OUT = ROOT / "references" / "attack-coverage.json"
UA = {"User-Agent": "spydermonkey-attack-map/7.0"}

# class keyword → ATT&CK technique (mirrors skilltree.BINDINGS third field)
def _bindings() -> dict[str, str]:
    src = (ROOT / "scripts" / "skilltree.py").read_text(encoding="utf-8")
    m = re.search(r'BINDINGS\s*[:=]\s*\{(.*?)\n\}', src, re.S)
    out: dict[str, str] = {}
    if not m:
        return out
    for kw, cwe, ack in re.findall(
            r'["\']([a-z0-9\-]+)["\']\s*:\s*\(\s*"[^"]+"\s*,\s*"([^"]+)"\s*,\s*"([^"]+)"\s*\)',
            m.group(1)):
        out[kw] = ack
    return out

ACK_RX = re.compile(r"^T\d{4}(?:\.\d{3})?$")
TOKEN_RX = re.compile(r"[^a-z0-9]+")


def map_corpus() -> dict:
    bindings = _bindings()
    if not bindings:
        print("✗ no BINDINGS found in skilltree.py", file=sys.stderr)
        return {}
    # longest keyword first so 'webauthn' wins over 'auth'
    kws = sorted(bindings, key=len, reverse=True)
    kw_tokens = {k: set(TOKEN_RX.split(k)) - {""} for k in kws}

    tech_files: dict[str, int] = defaultdict(int)
    tech_cwes: dict[str, set] = defaultdict(set)
    tech_classes: dict[str, set] = defaultdict(set)
    total = mapped = 0
    for root, dirs, files in os.walk(SKILLS):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            total += 1
            low = fn.lower()
            tokens = set(TOKEN_RX.split(low)) - {""}
            hit = None
            for kw in kws:
                if kw in low and kw_tokens[kw] & tokens:
                    hit = kw
                    break
            if not hit:
                continue
            ack = bindings[hit]
            if not ACK_RX.match(ack):
                continue
            mapped += 1
            tech_files[ack] += 1
            tech_classes[ack].add(hit)
    # CWEs per technique from the bindings table
    src = (ROOT / "scripts" / "skilltree.py").read_text(encoding="utf-8")
    m = re.search(r'BINDINGS\s*[:=]\s*\{(.*?)\n\}', src, re.S)
    for kw, cwe, ack in re.findall(
            r'["\']([a-z0-9\-]+)["\']\s*:\s*\(\s*"[^"]+"\s*,\s*"([^"]+)"\s*,\s*"([^"]+)"\s*\)',
            m.group(1) if m else ""):
        if ACK_RX.match(ack) and kw in tech_classes.get(ack, set()):
            tech_cwes[ack].add(cwe)

    techniques = {t: {"files": n,
                      "cwes": sorted(tech_cwes.get(t, set())),
                      "classes": sorted(tech_classes.get(t, set()))}
                  for t, n in sorted(tech_files.items(),
                                     key=lambda x: -x[1])}
    return {"total_files": total, "mapped_files": mapped,
            "coverage_pct": round(mapped * 100.0 / total, 1) if total else 0.0,
            "technique_count": len(techniques),
            "techniques": techniques}


def atomic_red_team_count() -> int | None:
    """Live count of Atomic Red Team atomics (the largest public ATT&CK
    emulation library) for an honest comparison — None when offline."""
    url = ("https://api.github.com/repos/redcanaryco/atomic-red-team/"
           "git/trees/master?recursive=1")
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read().decode("utf-8", errors="replace"))
        n = 0
        for it in data.get("tree", []):
            p = it.get("path", "")
            if p.startswith("atomics/") and p.lower().endswith((".yaml", ".yml")) \
                    and "T" in p.rsplit("/", 1)[-1][:2]:
                n += 1
        return n
    except Exception:
        return None


def main() -> int:
    no_fetch = "--no-fetch" in sys.argv
    doc = map_corpus()
    if not doc:
        return 1
    doc["comparison"] = {"atomic_red_team_tests": None if no_fetch
                         else atomic_red_team_count(),
                         "note": "ART = the largest public ATT&CK emulation "
                                 "library; our count = technique files mapped "
                                 "to ATT&CK IDs via the skilltree bindings"}
    tmp = OUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(doc, indent=1) + "\n")
    os.replace(tmp, OUT)
    art = doc["comparison"]["atomic_red_team_tests"]
    print(f"═══ ATT&CK COVERAGE — {doc['mapped_files']:,} / {doc['total_files']:,} "
          f"files mapped ({doc['coverage_pct']}%) · "
          f"{doc['technique_count']} techniques ═══")
    if art:
        print(f"  vs Atomic Red Team: {art} test files")
        print(f"  ratio: {doc['mapped_files'] / art:.0f}× ART's library")
    top = list(doc["techniques"].items())[:8]
    for t, v in top:
        print(f"  {t:8s} {v['files']:7,d} files  {','.join(v['cwes'][:3])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
