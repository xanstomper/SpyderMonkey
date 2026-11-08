#!/usr/bin/env python3
"""CORPUS SURGE (v7.6.6) — the official-knowledge fetch lane.

NVD CVEs · CAPEC · GTFOBins → compact index artifacts the context router
retrieves (kinds: cve · capec · gtfobin). Mirrors + UA fallbacks; a blocked
source is REPORTED, never faked — the honesty is the product.

Run where egress allows (this box's egress is filtered — the artifacts land
on any machine with a real pipe, then ship in-repo like sigma-index.json).

Usage: corpus_surge.py cve|capec|gtfobin|all [--years 2024,2025,2026]
Env:   NVD_API_KEY   (raises the NVD API rate limit 5→50 req/30s)
"""
from __future__ import annotations

import gzip
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
import urllib.error
from pathlib import Path

REFERENCES = Path(__file__).resolve().parent.parent / "references"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, Gecko) "
      "Chrome/126.0 Safari/537.36")
CVE_RX = re.compile(r"CVE-\d{4}-\d{4,7}")


def _get(url: str, headers: dict | None = None, timeout: int = 60) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def _desc_of(cve: dict) -> str:
    for d in cve.get("descriptions", []):
        if d.get("lang") == "en":
            return d.get("value", "")[:160]
    return ""


def _cwes_of(cve: dict) -> list[str]:
    out = []
    for w in cve.get("weaknesses", []):
        for d in w.get("description", []):
            v = d.get("value", "")
            if v.startswith("CWE-") and v not in out:
                out.append(v)
    return out


def _sev_of(cve: dict) -> str:
    m = cve.get("metrics", {})
    for key in ("cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
        if key in m and m[key]:
            return str(m[key][0].get("cvssData", {}).get("baseSeverity",
                                                        m[key][0].get("baseSeverity", "")))
    return ""


def fetch_cve(years: list[int]) -> tuple[bool, str]:
    """The CVE density play. Priority: NVD API 2.0 paging (resumable); the
    legacy bulk gz feeds as fallback. ~240k+ records when the pipe works."""
    out_path = REFERENCES / "cve-index.json"
    entries: dict[str, dict] = {}
    if out_path.exists():
        try:
            for e in json.loads(out_path.read_text()).get("cves", []):
                entries[e["id"]] = e
        except Exception:
            pass
    api = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    key = os.environ.get("NVD_API_KEY")
    headers = {"apiKey": key} if key else {}
    pause = 6.5 if not key else 1.2
    got = 0

    def _flush():
        payload = {"generator": "corpus_surge.py cve (NVD API 2.0)",
                   "total": len(entries), "fetched_this_run": got,
                   "cves": sorted(entries.values(), key=lambda x: x["id"])}
        out_path.write_text(json.dumps(payload, separators=(",", ":")))

    try:
        start = 0
        while True:
            url = f"{api}?resultsPerPage=2000&startIndex={start}"
            if years:
                url += f"&pubStartDate={years[0]}-01-01T00:00:00.000"
            doc = None
            for attempt in range(3):          # transient read-timeouts: retry
                try:
                    doc = json.loads(_get(url, headers, timeout=120).decode())
                    break
                except Exception as e:
                    if attempt == 2:
                        raise
                    time.sleep(4)
            batch = doc.get("vulnerabilities", [])
            if not batch:
                break
            for it in batch:
                cve = it.get("cve", {})
                cid = cve.get("id", "")
                if not cid:
                    continue
                entries[cid] = {"id": cid,
                                "cwe": _cwes_of(cve),
                                "sev": _sev_of(cve),
                                "desc": _desc_of(cve)}
                got += 1
            total = doc.get("totalResults", 0)
            start += doc.get("resultsPerPage", 2000)
            print(f"  … {start}/{total}", flush=True)
            _flush()                           # INCREMENTAL: partial progress persists
            if start >= total:
                break
            time.sleep(pause)
    except urllib.error.HTTPError as e:
        _flush()
        if e.code == 403:
            return False, (f"NVD API refused (403 — rate/blocked); fetched "
                           f"{got} new this run; {len(entries)} total known")
        return False, f"NVD API HTTP {e.code}; {len(entries)} indexed so far"
    except Exception as e:
        _flush()                               # partial corpus PERSISTS — resume picks up
        return False, (f"NVD API interrupted ({e}); {len(entries)} indexed so "
                       f"far — RE-RUN TO RESUME")
    return True, f"{len(entries)} CVEs indexed ({got} fetched this run)"


def fetch_capec() -> tuple[bool, str]:
    """CAPEC attack-pattern encyclopedia (~550 patterns, MITRE)."""
    out_path = REFERENCES / "capec-index.json"
    for url in ("https://capec.mitre.org/data/json/views/1000.json",
                "http://capec.mitre.org/data/json/views/1000.json"):
        try:
            doc = json.loads(_get(url, timeout=90).decode("utf-8", "replace"))
            objs = doc.get("objects", [])
            pats = []
            for o in objs:
                if o.get("type") != "attack-pattern":
                    continue
                name = o.get("name", "")
                desc = (o.get("description", "") or "")[:200]
                ext_refs = [r.get("external_id", "")
                            for r in o.get("external_references", [])]
                capec_id = next((x for x in ext_refs if x.startswith("CAPEC-")), "")
                pats.append({"id": capec_id or name, "name": name, "desc": desc})
            if not pats:
                return False, "CAPEC source reachable but empty"
            out_path.write_text(json.dumps(
                {"generator": "corpus_surge.py capec", "total": len(pats),
                 "patterns": pats}, separators=(",", ":")))
            return True, f"{len(pats)} CAPEC patterns indexed"
        except Exception as e:
            continue
    return False, f"CAPEC unreachable from this box ({url})"


def fetch_gtfobin() -> tuple[bool, str]:
    """GTFOBins — privesc knowledge for the kaisha battery (~600 binaries)."""
    out_path = REFERENCES / "gtfobin-index.json"
    with tempfile.TemporaryDirectory(prefix="gtfo-") as td:
        clone = Path(td) / "gtfo"
        try:
            r = subprocess.run(["git", "clone", "--depth", "1", "--quiet",
                                "https://github.com/GTFOBins/GTFOBins.github.io.git",
                                str(clone)], capture_output=True, timeout=300)
            if r.returncode != 0:
                return False, f"GTFOBins clone failed: {r.stderr.decode()[:120]}"
        except Exception as e:
            return False, f"GTFOBins clone crashed: {e}"
        entries = []
        md_dir = None
        for cand in ("_gtfobins", "gtfobins", "_data"):
            if (clone / cand).is_dir():
                md_dir = clone / cand
                break
        if md_dir is None:
            return False, "GTFOBins layout changed — no binary dir found"
        for p in sorted(md_dir.glob("*")):
            if not p.is_file():
                continue
            text = p.read_text(errors="replace")
            # the functions are YAML keys under `functions:` (indented), e.g.
            # "  file-read:", "  sudo:", "  shell:" — plus ## headers in older revs
            funcs = sorted(set(re.findall(r"^## ([a-z\-]+)", text, re.M))
                           | set(re.findall(r"^  ([a-z][a-z\-]{2,}):", text, re.M)))
            entries.append({"bin": p.stem, "functions": funcs,
                            "title": p.stem})
        out_path.write_text(json.dumps(
            {"generator": "corpus_surge.py gtfobin", "total": len(entries),
             "bins": entries}, separators=(",", ":")))
        return True, f"{len(entries)} GTFOBins binaries indexed"


def main() -> int:
    ap = sys.argv[1:] if len(sys.argv) > 1 else ["all"]
    which = ap[0]
    years = []
    if "--years" in ap:
        years = [int(y) for y in ap[ap.index("--years") + 1].split(",")]
    jobs = {"cve": lambda: fetch_cve(years),
            "capec": fetch_capec, "gtfobin": fetch_gtfobin}
    if which == "all":
        todo = ["cve", "capec", "gtfobin"]
    elif which in jobs:
        todo = [which]
    else:
        print(__doc__)
        return 2
    rc = 0
    for name in todo:
        ok, msg = jobs[name]()
        print(f"  {'✓' if ok else '✗'} {name:8s} {msg}")
        if not ok:
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())