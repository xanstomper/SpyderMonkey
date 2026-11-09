#!/usr/bin/env python3
"""SPYDERMONKEY CONTEXT ROUTER — the retrieval layer (v7.4 rail: any model, the
right knowledge in context at the right moment).

Read-only, deterministic, stdlib. Indexes the family's real corpora:
  · canon    — the 30+ reference canon volumes (full text, tokenized)
  · skill    — the curated skilltree index (1,114 technique entries, WSTG/CWE/T tags)
  · expanded — the expanded technique corpus (138k+ platform × auth × federated files)
  · tool     — the 66,569-entry tool-catalog surge (exploit-db · nuclei · metasploit)

The index cache lives under $SPYDERMONKEY_HOME/cache/ (never under references/ —
the corpus is read-only). Scoring is deterministic (rarity-weighted term overlap
with a title boost); the same query always returns the same ranked hits.

CLI:  context_router.py query --terms "ssrf jwt" [--top N] [--budget CHARS]
                               [--kinds canon,skill,tool,expanded] [--json]
      context_router.py stats [--json]
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFERENCES = ROOT / "references"

KINDS = ("canon", "skill", "expanded", "tool", "sigma", "capec", "cve",
         "gtfobin", "lane")
KIND_WEIGHT = {"canon": 3.0, "skill": 2.2, "expanded": 1.6, "tool": 1.0,
               "sigma": 1.4, "capec": 1.5, "cve": 1.3, "gtfobin": 1.2,
               "lane": 2.5}

STOP = {
    "the", "a", "an", "and", "or", "for", "to", "of", "in", "on", "with",
    "by", "from", "via", "how", "what", "is", "are", "it", "its", "this",
    "that", "be", "as", "at", "we", "you", "your", "their", "they", "can",
    "will", "not", "no", "but", "do", "does", "did", "has", "have", "had",
    "was", "were", "would", "could", "should", "into", "over", "under",
    "than", "then", "there", "here", "when", "which", "who", "whom", "all",
    "any", "each", "more", "most", "some", "such", "only", "own", "same",
    "so", "too", "very", "just", "also", "get", "got", "use", "using",
    "used", "one", "two", "etc", "e", "g", "vs", "aka", "s",
}

TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9\-_+.]*")


def tokenize(text: str) -> set[str]:
    out = set()
    for m in TOKEN_RE.finditer(text.lower()):
        t = m.group(0)
        if len(t) >= 3 and t not in STOP and not t.isdigit():
            out.add(t)
    return out


def _stamp() -> str:
    latest = 0.0
    for p in REFERENCES.glob("*.md"):
        latest = max(latest, p.stat().st_mtime)
    for p in (REFERENCES / "skilltree-index.md",
              REFERENCES / "skilltree-expanded-index.md"):
        latest = max(latest, p.stat().st_mtime)
    surge = REFERENCES / "tool-catalog-surge.json"
    if surge.exists():
        latest = max(latest, surge.stat().st_mtime)
    sigma_idx = REFERENCES / "sigma-index.json"
    if sigma_idx.exists():
        latest = max(latest, sigma_idx.stat().st_mtime)
    for extra in ("cve-index.json", "capec-index.json", "gtfobin-index.json"):
        p = REFERENCES / extra
        if p.exists():
            latest = max(latest, p.stat().st_mtime)
    return f"{latest:.0f}"


def _index_path(kinds: tuple[str, ...] | None = None) -> Path:
    home = Path(os.environ.get("SPYDERMONKEY_HOME",
                               str(Path.home() / ".redteam")))
    cache = home / "cache"
    cache.mkdir(parents=True, exist_ok=True)
    if kinds:
        # kind-scoped caches share nothing with the full index
        return cache / ("context-index-" + "-".join(sorted(kinds)) + ".json")
    return cache / "context-index.json"


def build_index(kinds: tuple[str, ...] | None = None) -> dict:
    """Build (or load cached) the corpus index. Read-only on references/.

    kinds=subset → build ONLY those lanes (e.g. ("canon","skill") for fleet
    briefs): the 138k expanded variants and 66k tool surge are skipped, so
    scoped builds take milliseconds instead of ~30s of cold build.
    """
    allow = set(kinds) if kinds else None

    def _w(k: str) -> bool:
        return allow is None or k in allow

    ipath = _index_path(kinds)
    stamp = _stamp()
    if ipath.exists():
        try:
            idx = json.loads(ipath.read_text())
            if idx.get("stamp") == stamp:
                return idx
        except Exception:
            pass

    docs = []

    # 1) canon volumes — full text tokenized, first-350-char snippet.
    #    glob MUST be *canon*.md — *canon.md silently drops the numbered
    #    technique-canon-N.md volumes (a 12-volume density loss, v7.6 fix).
    for p in sorted(REFERENCES.glob("*canon*.md")):
        if not _w("canon"):
            break
        text = p.read_text(errors="replace")
        toks = tokenize(text)
        if not toks:
            continue
        snip = re.sub(r"\s+", " ", text).strip()[:350]
        docs.append({"k": "canon", "id": p.name, "t": p.name,
                     "tags": "", "snip": snip,
                     "toks": sorted(toks),
                     "ttoks": sorted(tokenize(p.name))})

    # 2) curated skilltree index — title + WSTG/CWE/T tags
    LINE_RE = re.compile(r"- \[(.+?)\]\(([^)]+)\) — (.*)$")
    for idx_file, kind in (("skilltree-index.md", "skill"),
                           ("skilltree-expanded-index.md", "expanded")):
        if not _w(kind):
            continue
        p = REFERENCES / idx_file
        if not p.exists():
            continue
        for line in p.read_text(errors="replace").splitlines():
            m = LINE_RE.match(line.strip())
            if not m:
                continue
            title, path, tail = m.group(1), m.group(2), m.group(3)
            toks = tokenize(title + " " + tail)
            if not toks:
                continue
            docs.append({"k": kind, "id": path, "t": title, "tags": tail.strip(),
                         "snip": tail.strip()[:220], "toks": sorted(toks),
                         "ttoks": sorted(tokenize(title))})

    # 3) tool-catalog surge — name + cat + desc
    surge = REFERENCES / "tool-catalog-surge.json"
    if _w("tool") and surge.exists():
        try:
            data = json.loads(surge.read_text())
            for entries in data.get("sections", {}).values():
                for e in entries:
                    name = e.get("name", "")
                    desc = e.get("desc", "")
                    cat = e.get("cat", "")
                    toks = tokenize(name + " " + desc + " " + cat)
                    if not toks:
                        continue
                    docs.append({"k": "tool", "id": name, "t": name,
                                 "tags": cat, "snip": desc[:220],
                                 "toks": sorted(toks),
                                 "ttoks": sorted(tokenize(name))})
        except Exception:
            pass

    # 4) SIGMA knowledge lane (v7.6): the detection corpus — every public
    #    SigmaHQ rule as a retrievable doc (title + logsource + detection
    #    tags). Generator: scripts/sigma_index.py; artifact ships in-repo.
    sigma_idx = REFERENCES / "sigma-index.json"
    if _w("sigma") and sigma_idx.exists():
        try:
            for e in json.loads(sigma_idx.read_text()).get("rules", []):
                name = e.get("name", "")
                title = e.get("title", "")
                toks = tokenize(" ".join([name, title,
                                          e.get("logsource", ""),
                                          e.get("tags", "")]))
                if not toks:
                    continue
                docs.append({"k": "sigma", "id": name, "t": title or name,
                             "tags": e.get("logsource", ""),
                             "snip": (e.get("detection", "") or "")[:220],
                             "toks": sorted(toks),
                             "ttoks": sorted(tokenize(title or name))})
        except Exception:
            pass

    # 4.5) THE LANE LANE (v7.9.5): the family's OWN measured capabilities —
    # every benchmark/result artifact becomes a retrievable doc, so any
    # agent's inject packet CARRIES the family's proven capability floor
    # (the numbers are the knowledge: the floor is 0.8 SR no-model, 3/3
    # synthesis, 4/5 remediation, ~1000 ips classified, 3/3 chains)
    for fname, lane in (("apb-family-result.json", "no-model-bench"),
                        ("synthesize-result.json", "synthesis"),
                        ("remediate-result.json", "remediation"),
                        ("masslane-result.json", "mass"),
                        ("fuzzfleet-result.json", "fuzz-ab"),
                        ("chainbench-result.json", "chain-depth")):
        lf = REFERENCES / fname
        if _w("lane") and lf.exists():
            try:
                d = json.loads(lf.read_text())
                bits = []
                for k in ("sr_this_run", "flags_captured", "fixes_verified",
                          "fixes_total", "hops_closed", "hops_total",
                          "throughput_ips", "findings_ratio", "paper_baseline_autonomous_sr"):
                    if k in d:
                        bits.append(f"{k}={d[k]}")
                lane_txt = (d.get("lane", "") + " · " + d.get("protocol", "")
                            + " · " + " ".join(bits)
                            + " · " + str(d.get("caveats", ""))[:200])
                toks = tokenize(lane_txt + " " + lane)
                if toks:
                    docs.append({"k": "lane", "id": "lane/" + lane,
                                 "t": f"{lane} — measured capability",
                                 "tags": "lane bench capability",
                                 "snip": lane_txt[:220],
                                 "toks": sorted(toks),
                                 "ttoks": sorted(tokenize(lane))})
            except Exception:
                pass

    # 5) THE CORPUS SURGE LANE (v7.6.6): official corpora fetched by
    #    corpus_surge.py — cve (NVD) · capec (MITRE) · gtfobin (privesc).
    #    Artifacts ship in-repo when fetched; absent file = kind absent.
    for fname, kind, weight in (("cve-index.json", "cve", 1.3),
                                ("capec-index.json", "capec", 1.5),
                                ("gtfobin-index.json", "gtfobin", 1.2)):
        if not _w(kind):
            continue
        p = REFERENCES / fname
        if not p.exists():
            continue
        try:
            data = json.loads(p.read_text())
        except Exception:
            continue
        if kind == "cve":
            for e in data.get("cves", []):
                toks = tokenize(" ".join([e.get("id", ""), e.get("desc", ""),
                                          " ".join(e.get("cwe", []))]))
                if not toks:
                    continue
                docs.append({"k": kind, "id": e.get("id", ""), "t": e.get("id", ""),
                             "tags": " ".join(e.get("cwe", [])) + " " + e.get("sev", ""),
                             "snip": e.get("desc", ""), "toks": sorted(toks),
                             "ttoks": sorted(tokenize(e.get("id", "")))})
        elif kind == "capec":
            for e in data.get("patterns", []):
                toks = tokenize(" ".join([e.get("id", ""), e.get("name", ""),
                                          e.get("desc", "")]))
                if not toks:
                    continue
                docs.append({"k": kind, "id": e.get("id", ""), "t": e.get("name", ""),
                             "tags": e.get("id", ""), "snip": e.get("desc", ""),
                             "toks": sorted(toks),
                             "ttoks": sorted(tokenize(e.get("name", "")))})
        elif kind == "gtfobin":
            for e in data.get("bins", []):
                toks = tokenize(" ".join([e.get("bin", ""), " ".join(e.get("functions", []))]))
                if not toks:
                    continue
                docs.append({"k": kind, "id": e.get("bin", ""), "t": e.get("bin", ""),
                             "tags": " ".join(e.get("functions", [])),
                             "snip": "privesc/sandbox-escape functions: " + " ".join(e.get("functions", [])),
                             "toks": sorted(toks),
                             "ttoks": sorted(tokenize(e.get("bin", "")))})

    df: dict[str, int] = {}
    for d in docs:
        for t in set(d["toks"]):
            df[t] = df.get(t, 0) + 1

    idx = {"stamp": stamp, "docs": docs, "df": df}
    try:
        ipath.write_text(json.dumps(idx, separators=(",", ":")))
    except Exception:
        pass
    return idx


def query(terms: str, top: int = 8, budget: int | None = None,
          kinds: tuple[str, ...] | None = None, mix: bool = True) -> list[dict]:
    """Ranked retrieval. Deterministic: score = rarity-weighted term overlap
    with a 2× title boost, kind weight, then (score desc, id).

    mix=True (default): KIND-BALANCED — each kind gets ~top/K seats in
    round-robin by kind weight, so the 138k expanded variants can't shout
    over the 30 canon volumes or the sigma/tool lanes (v7.6.3). mix=False:
    pure global ranking."""
    idx = build_index(kinds)
    qtoks = tokenize(terms)
    if not qtoks:
        return []
    df = idx["df"]
    allow = set(kinds) if kinds else set(KINDS)

    scored = []
    for d in idx["docs"]:
        if d["k"] not in allow:
            continue
        dtoks = set(d["toks"])
        ttoks = set(d.get("ttoks", ()))
        hit = qtoks & dtoks
        if not hit:
            continue
        s = 0.0
        for t in hit:
            w = KIND_WEIGHT[d["k"]] * (2.0 if t in ttoks else 1.0)
            s += w / (1.0 + math.log2(1.0 + df.get(t, 1)))
        scored.append((s, d))

    scored.sort(key=lambda x: (-x[0], x[1]["id"]))
    if mix and len(allow) > 1:
        buckets: dict[str, list] = {}
        for sd in scored:
            buckets.setdefault(sd[1]["k"], []).append(sd)
        order = sorted(buckets, key=lambda k: -KIND_WEIGHT[k])
        picked = []
        added = 0
        while added < top:
            progressed = False
            for k in order:
                if buckets[k]:
                    picked.append(buckets[k].pop(0))
                    added += 1
                    progressed = True
                    if added >= top:
                        break
            if not progressed:
                break
        scored = picked
    hits = []
    used = 0
    for s, d in scored:
        entry = {"kind": d["k"], "id": d["id"], "title": d["t"],
                 "tags": d.get("tags", ""), "score": round(s, 4),
                 "snippet": d.get("snip", "")}
        hits.append(entry)
        if budget is not None and len(entry["snippet"]) > 0:
            used += len(entry["snippet"])
            if used >= budget and len(hits) >= 1:
                break
        if len(hits) >= top:
            break
    return hits


def stats() -> dict:
    idx = build_index()
    counts: dict[str, int] = {}
    for d in idx["docs"]:
        counts[d["k"]] = counts.get(d["k"], 0) + 1
    return {"stamp": idx["stamp"], "docs": len(idx["docs"]), "terms": len(idx["df"]),
            "kinds": counts, "cache": str(_index_path())}


def main() -> int:
    ap = argparse.ArgumentParser(prog="context_router", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    q = sub.add_parser("query", help="ranked retrieval over the family corpora")
    q.add_argument("--terms", required=True, help="space/comma separated terms")
    q.add_argument("--top", type=int, default=8)
    q.add_argument("--budget", type=int, default=None, help="max snippet chars")
    q.add_argument("--kinds", default=",".join(KINDS),
                   help="comma list of canon,skill,expanded,tool")
    q.add_argument("--json", action="store_true")
    s = sub.add_parser("stats", help="index stats")
    s.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.cmd == "stats":
        st = stats()
        if args.json:
            print(json.dumps(st, indent=2))
        else:
            print(f"context index: {st['docs']} docs · {st['terms']} terms · "
                  f"stamp {st['stamp']}")
            for k, v in sorted(st["kinds"].items()):
                print(f"  {k:9s} {v}")
            print(f"  cache at {st['cache']}")
        return 0

    kinds = tuple(k.strip() for k in args.kinds.split(",") if k.strip())
    hits = query(args.terms, top=args.top, budget=args.budget, kinds=kinds)
    if args.json:
        print(json.dumps({"terms": args.terms, "count": len(hits), "hits": hits},
                         indent=2))
        return 0
    print(f"▸ {args.terms} — {len(hits)} hit(s)")
    for h in hits:
        print(f"  [{h['kind']:8s}] {h['title']}")
        print(f"           {h['id']}  {h['tags']}")
        print(f"           {h['snippet'][:160]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())