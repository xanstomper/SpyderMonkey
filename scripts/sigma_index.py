#!/usr/bin/env python3
"""SIGMA KNOWLEDGE LANE generator (v7.6): SigmaHQ rule files → compact
references/sigma-index.json for the context router's retrieval layer.

stdlib-only line parser — retrieval-grade, not semantic-grade (no yaml dep):
extracts title · logsource (category/product/service/definition) · tags ·
the raw detection block (capped). The router tokenizes the lot, so searching
for a technique/payload term surfaces the exact rule that detects it.

Usage: sigma_index.py <rules-dir> [out.json]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ONE_LINE_KEYS = ("title", "id", "status", "level")
LS_KEYS = ("category", "product", "service", "definition")


def parse_rule(text: str, stem: str) -> dict | None:
    out = {"name": stem, "title": "", "logsource": "", "tags": "",
           "detection": ""}
    lines = text.splitlines()
    ls_parts: list[str] = []
    det_parts: list[str] = []
    tags: list[str] = []
    in_ls = in_det = in_tags = False
    det_shown = 0
    for i, raw in enumerate(lines):
        s = raw.rstrip()
        indent = (len(s) - len(s.lstrip())) if s else 0
        stripped = s.strip()
        if not stripped:
            if in_tags:
                in_tags = False
            continue
        if indent > 0:
            if in_ls and ":" in stripped:
                k, v = stripped.split(":", 1)
                if k in LS_KEYS and v.strip():
                    ls_parts.append(f"{k}={v.strip()}")
            elif in_det and det_shown < 240:
                det_parts.append(stripped[:120])
                det_shown += 1
            elif in_tags and stripped.startswith("- "):
                tags.append(stripped[2:].strip())
            continue
        # top-level key (column 0)
        in_ls = in_det = False
        if stripped.startswith("- ") and in_tags:
            tags.append(stripped[2:].strip())
            continue
        if ":" not in stripped:
            if in_tags:
                in_tags = False
            continue
        k, v = stripped.split(":", 1)
        k = k.strip()
        if k == "logsource":
            in_ls, in_det = True, False
        elif k == "detection":
            in_det, in_ls = True, False
            in_tags = False
        elif k == "tags":
            in_tags, in_ls, in_det = True, False, False
            if v.strip():
                tags.append(v.strip())
        elif k in ONE_LINE_KEYS and not out.get(k) if k == "title" else True:
            if k == "title" and not out["title"]:
                out["title"] = v.strip()
        if k not in ("logsource", "detection", "tags", "title"):
            in_tags = False
    out["logsource"] = " ".join(ls_parts)
    out["tags"] = " ".join(tags)
    out["detection"] = " ".join(det_parts)
    if not (out["title"] or out["logsource"] or det_parts):
        return None
    return out


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    rules_dir = Path(sys.argv[1])
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else \
        Path(__file__).resolve().parent.parent / "references" / "sigma-index.json"
    rules = []
    skipped = 0
    total = 0
    for p in sorted(rules_dir.rglob("*.yml")) + sorted(rules_dir.rglob("*.yaml")):
        total += 1
        try:
            r = parse_rule(p.read_text(encoding="utf-8", errors="replace"),
                           p.relative_to(rules_dir).as_posix())
        except Exception:
            r = None
        if r:
            rules.append(r)
        else:
            skipped += 1
    payload = {"generator": "sigma_index.py v7.6", "total_rules_seen": total,
               "indexed": len(rules), "skipped": skipped, "rules": rules}
    out_path.write_text(json.dumps(payload, separators=(",", ":")))
    print(f"▸ {len(rules)}/{total} sigma rules indexed → {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())