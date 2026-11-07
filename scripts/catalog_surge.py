#!/usr/bin/env python3
"""
CATALOG_SURGE — SPYDERMONKEY v7.0.0: the known-tool index scales 1,686 → ~95k.

Pulls the PUBLIC indexes of the three biggest offensive tool corpora and folds
them into the catalog as a separate lazy-loaded surge file:

  · Exploit-DB        (exploit-database/exploitdb, files_exploits.csv)
  · Nuclei templates  (projectdiscovery/nuclei-templates, git tree)
  · Metasploit module (rapid7/metasploit-framework, git tree)

Catalog discipline unchanged: this is a MAP, not an armory — nothing here
executes; firing goes through `arsenal` (installed tools only, scope-gated).
Re-run on any machine with network: `python3 scripts/catalog_surge.py`.
stdlib-only.
"""
from __future__ import annotations

import csv
import io
import json
import os
import sys
import urllib.request
from pathlib import Path

REF = Path(__file__).resolve().parent.parent / "references"
OUT = REF / "tool-catalog-surge.json"
UA = {"User-Agent": "spydermonkey-catalog-surge/7.0"}

EDB_CSV_URLS = [
    "https://raw.githubusercontent.com/offensive-security/exploitdb/main/files_exploits.csv",
    "https://gitlab.com/exploit-database/exploitdb/-/raw/main/files_exploits.csv",
]
NUCLEI_TREE = ("https://api.github.com/repos/projectdiscovery/"
               "nuclei-templates/git/trees/main?recursive=1")
MSF_TREE = ("https://api.github.com/repos/rapid7/metasploit-framework/"
            "git/trees/master?recursive=1")

MAX_DESC = 110


def _get(url: str, timeout: int = 120) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def _fetch_first(urls: list[str]) -> bytes:
    last = None
    for u in urls:
        try:
            return _get(u)
        except Exception as e:  # try the next mirror
            last = e
    raise RuntimeError(f"all sources failed: {last}")


def edb_entries() -> list[dict]:
    raw = _fetch_first(EDB_CSV_URLS).decode("utf-8", errors="replace")
    out = []
    for row in csv.DictReader(io.StringIO(raw)):
        eid = (row.get("id") or "").strip()
        desc = (row.get("description") or "").strip()
        if not eid or not desc:
            continue
        plat = (row.get("platform") or "unknown").strip().lower().replace(" ", "-")
        etype = (row.get("type") or "exploit").strip().lower()
        out.append({
            "name": f"edb-{eid}",
            "cat": f"exploit/{plat}",
            "desc": desc[:MAX_DESC],
            "mode": "active" if etype != "shellcode" else "payload",
            "src": "exploit-db",
        })
    return out


def _tree_yaml_rb(url: str, prefix: str, exts: tuple[str, ...]) -> list[str]:
    data = json.loads(_get(url).decode("utf-8", errors="replace"))
    if data.get("truncated"):
        print(f"⚠ tree truncated for {prefix}", file=sys.stderr)
    paths = [it["path"] for it in data.get("tree", [])
             if it.get("type") == "blob" and it["path"].lower().endswith(exts)
             and it["path"].startswith(prefix)]
    return paths


def nuclei_entries() -> list[dict]:
    out = []
    for p in _tree_yaml_rb(NUCLEI_TREE, "", (".yaml", ".yml")):
        if "/" not in p or p.endswith((".md", ".cfg")):
            continue
        stem = p.rsplit("/", 1)[-1][:-5] if p.lower().endswith(".yaml") else p.rsplit("/", 1)[-1][:-4]
        top = p.split("/")[0]
        out.append({
            "name": f"nuclei-{stem}"[:120],
            "cat": f"detection/{top}",
            "desc": f"nuclei detection template: {p}"[:MAX_DESC],
            "mode": "passive",
            "src": "nuclei-templates",
        })
    return out


def msf_entries() -> list[dict]:
    out = []
    for p in _tree_yaml_rb(MSF_TREE, "modules/", (".rb",)):
        parts = p.split("/")
        if len(parts) < 3:
            continue
        kind = parts[1]                      # exploit/auxiliary/payload/post/encoders
        stem = p[len("modules/"):-3].replace("/", "-")
        out.append({
            "name": f"msf-{stem}"[:140],
            "cat": f"{kind}/metasploit",
            "desc": f"metasploit {kind} module: {'/'.join(parts[2:])}"[:MAX_DESC],
            "mode": "active" if kind in ("exploit", "payload") else "passive",
            "src": "metasploit",
        })
    return out


def main() -> int:
    sections = {}
    print("▸ fetching Exploit-DB index…")
    sections["exploit-db"] = edb_entries()
    print(f"  {len(sections['exploit-db'])} entries")
    print("▸ fetching Nuclei template tree…")
    sections["nuclei-templates"] = nuclei_entries()
    print(f"  {len(sections['nuclei-templates'])} entries")
    print("▸ fetching Metasploit module tree…")
    sections["metasploit"] = msf_entries()
    print(f"  {len(sections['metasploit'])} entries")

    total = sum(len(v) for v in sections.values())
    doc = {"surge_version": "7.0.0", "total": total, "sections": sections}
    tmp = OUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(doc, separators=(",", ":")) + "\n")
    os.chmod(tmp, 0o644)
    os.replace(tmp, OUT)
    print(f"═══ CATALOG SURGE — {total} entries → {OUT.name} ═══")
    return 0


if __name__ == "__main__":
    sys.exit(main())
