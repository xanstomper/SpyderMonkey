#!/usr/bin/env python3
"""
SPYDERMONKEY SKILLTREE — generate the family's per-technique skill files from
its REAL canon: every mandate's references/ dir that exists on disk (barbican,
holyshit-mode, undercroft, 3am-shinjitsu, kairo, kaisha, shukaku, kage, dojo —
plus the dispatcher's own references) with WSTG/CWE/ATT&CK bindings. One
technique = one lazy-loaded skill file + a searchable index.

Run:  python3 skilltree.py           # emit to references/skills/ + index.md
      python3 skilltree.py --count   # just count what would be generated
      python3 skilltree.py --verify  # prove index ↔ files ↔ bindings are intact
      python3 skilltree.py --count --json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFS = ROOT / "references"
OUT = REFS / "skills"

# methodology bindings: class keyword → (WSTG, CWE, ATT&CK)
BINDINGS = {
    "boundary": ("WSTG-ATHZ-04", "CWE-639", "T1068"),
    "idor": ("WSTG-ATHZ-04", "CWE-639", "T1068"),
    "replay": ("WSTG-BUSL-06", "CWE-294", "T1550"),
    "webhook": ("WSTG-BUSL-06", "CWE-294", "T1550"),
    "idempoten": ("WSTG-BUSL-06", "CWE-294", "T1550"),
    "state": ("WSTG-BUSL-08", "CWE-841", "T1574"),
    "transition": ("WSTG-BUSL-08", "CWE-841", "T1574"),
    "math": ("WSTG-BUSL-01", "CWE-681", "T1565"),
    "rounding": ("WSTG-BUSL-01", "CWE-681", "T1565"),
    "precision": ("WSTG-BUSL-01", "CWE-1336", "T1565"),
    "entitle": ("WSTG-BUSL-05", "CWE-285", "T1068"),
    "coupon": ("WSTG-BUSL-05", "CWE-285", "T1068"),
    "auth": ("WSTG-ATHN", "CWE-287", "T1111"),
    "token": ("WSTG-SESS", "CWE-287", "T1528"),
    "jwt": ("WSTG-SESS-01", "CWE-347", "T1552"),
    "session": ("WSTG-SESS", "CWE-384", "T1550"),
    "otp": ("WSTG-ATHN-09", "CWE-287", "T1111"),
    "firmware": ("MASTG-RES", "CWE-494", "T1601"),
    "uart": ("MASTG-RES", "CWE-494", "T1601"),
    "flash": ("MASTG-RES", "CWE-494", "T1601"),
    "ota": ("MASTG-RES", "CWE-494", "T1601"),
    "ble": ("MASTG-RES", "CWE-288", "T1557"),
    "radio": ("MASTG-RES", "CWE-288", "T1557"),
    "rfid": ("MASTG-RES", "CWE-288", "T1557"),
    "nfc": ("MASTG-RES", "CWE-288", "T1557"),
    "injection": ("WSTG-INPV", "CWE-74", "T1190"),
    "sql": ("WSTG-INPV-05", "CWE-89", "T1190"),
    "xss": ("WSTG-INPV-02", "CWE-79", "T1189"),
    "ssrf": ("WSTG-INPV-10", "CWE-918", "T1190"),
    "xxe": ("WSTG-INPV-07", "CWE-611", "T1190"),
    "redirect": ("WSTG-INPV-06", "CWE-601", "T1190"),
    "backup": ("WSTG-CONF-04", "CWE-530", "T1552"),
    "dump": ("WSTG-CONF-04", "CWE-530", "T1552"),
    "env": ("WSTG-CONF-04", "CWE-530", "T1552"),
    "git": ("WSTG-CONF-04", "CWE-538", "T1552"),
    "secret": ("WSTG-CONF-04", "CWE-798", "T1552"),
    "cors": ("WSTG-CLNT-03", "CWE-942", "T1557"),
    "smuggl": ("WSTG-ADV-02", "CWE-444", "T1190"),
    "graphql": ("WSTG-APIT-10", "CWE-1321", "T1190"),
    "prototype": ("WSTG-CLNT-04", "CWE-1321", "T1189"),
    "websocket": ("WSTG-CLNT-05", "CWE-345", "T1557"),
    "subdomain": ("WSTG-CONF-09", "CWE-350", "T1584"),
    "takeover": ("WSTG-CONF-09", "CWE-350", "T1584"),
    "bucket": ("WSTG-CONF-04", "CWE-732", "T1530"),
    "s3": ("WSTG-CONF-04", "CWE-732", "T1530"),
    "pi": ("WSTG-BUSL", "CWE-200", "T1005"),
    "disclosure": ("WSTG-INFO", "CWE-200", "T1592"),
    "privesc": ("PTES-LE", "CWE-250", "T1068"),
    "sudo": ("PTES-LE", "CWE-250", "T1548"),
    "suid": ("PTES-LE", "CWE-250", "T1548"),
    "lateral": ("PTES-PE", "CWE-287", "T1550"),
    "cred": ("PTES-PE", "CWE-522", "T1555"),
    "harvest": ("WSTG-BUSL", "CWE-200", "T1005"),
    "crown": ("WSTG-BUSL", "CWE-200", "T1005"),
    "leak": ("WSTG-INFO", "CWE-200", "T1592"),
    "sanitize": ("PTES-OPSEC", "CWE-200", "T1070"),
    "vantage": ("PTES-OPSEC", "CWE-200", "T1070"),
    "timeline": ("PTES-OPSEC", "CWE-200", "T1070"),
    "trail": ("PTES-OPSEC", "CWE-200", "T1070"),
    "rate": ("WSTG-ATHN-04", "CWE-307", "T1110"),
    "brute": ("WSTG-ATHN-04", "CWE-307", "T1110"),
    "cookie": ("WSTG-SESS-03", "CWE-1004", "T1550"),
    "toss": ("WSTG-SESS-03", "CWE-1004", "T1550"),
    "cache": ("WSTG-ADV-01", "CWE-444", "T1190"),
    "poison": ("WSTG-ADV-01", "CWE-444", "T1190"),
    "header": ("WSTG-PARA", "CWE-113", "T1190"),
    "host-header": ("WSTG-PARA", "CWE-113", "T1190"),
    "redirect": ("WSTG-INPV-06", "CWE-601", "T1190"),
    "deserial": ("WSTG-INPV", "CWE-502", "T1190"),
    "race": ("WSTG-BUSL-07", "CWE-362", "T1499"),
    "randomness": ("WSTG-BUSL-03", "CWE-330", "T1036"),
    "entropy": ("WSTG-BUSL-03", "CWE-330", "T1036"),
    "logic": ("WSTG-BUSL", "CWE-840", "T1499"),
    "payment": ("WSTG-BUSL-02", "CWE-840", "T1565"),
    "price": ("WSTG-BUSL-02", "CWE-840", "T1565"),
    "password": ("WSTG-ATHN-08", "CWE-521", "T1110"),
    "reset": ("WSTG-ATHN-07", "CWE-640", "T1078"),
    "mfa": ("WSTG-ATHN-09", "CWE-308", "T1111"),
    "upload": ("WSTG-BUSL-09", "CWE-434", "T1190"),
    "traversal": ("WSTG-PATH", "CWE-22", "T1005"),
    "directory": ("WSTG-CONF-03", "CWE-548", "T1083"),
    "sourcemap": ("WSTG-INFO-10", "CWE-540", "T1552"),
    "container": ("PTES-CON", "CWE-250", "T1611"),
    "kubernetes": ("PTES-CON", "CWE-250", "T1610"),
    "kerberos": ("PTES-WIN", "CWE-287", "T1558"),
    "ldap": ("WSTG-INPV", "CWE-90", "T1190"),
    "cmd": ("WSTG-INPV-09", "CWE-78", "T1059"),
    "ssti": ("WSTG-INPV", "CWE-1336", "T1059"),
    "nosql": ("WSTG-INPV-05", "CWE-943", "T1190"),
}


def _bindings(text):
    t = text.lower()
    hits = []
    for kw, (w, c, a) in BINDINGS.items():
        if kw in t:
            hits.append((w, c, a))
    if not hits:
        return ("WSTG-INFO", "CWE-200", "T1592")
    return hits[0]


def _slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:60] or "technique"


def _extract_blocks(text, headers):
    """Split a reference doc into (title, body) chunks by ## AND ### headers —
    the deeper the header, the denser the tree."""
    out = []
    cur_title, cur = None, []
    for line in text.splitlines():
        if line.startswith("## ") or line.startswith("### "):
            if cur_title and cur:
                out.append((cur_title, "\n".join(cur).strip()))
            cur_title, cur = line.lstrip("#").strip(), []
        elif cur_title:
            cur.append(line)
    if cur_title and cur:
        out.append((cur_title, "\n".join(cur).strip()))
    return out


def collect_sources():
    """Every (category, title, body) from the family's real canon — every mandate
    references/ dir present on disk (all ten mandates, where installed), plus the
    dispatcher's own references."""
    srcs = []
    dirs = []
    sec = Path.home() / ".hermes/skills/security"
    for name in ("barbican", "holyshit-mode", "undercroft", "3am-shinjitsu",
                 "kairo", "kaisha", "shukaku", "kage", "dojo"):
        d = sec / name / "references"
        if d.exists():
            dirs.append((name, d))
    dirs.append(("spydermonkey", REFS))
    seen_titles = set()
    for cat, d in dirs:
        for p in sorted(d.glob("*.md")):
            try:
                text = p.read_text(errors="replace")
            except Exception:
                continue
            for title, body in _extract_blocks(text, True):
                key = f"{cat}:{title}".lower()
                if key in seen_titles or len(body) < 40:
                    continue
                seen_titles.add(key)
                srcs.append((f"{cat}/{p.stem}", title, body))
    # kairo technique classes (table rows)
    se = None
    for cat, d in dirs:
        if cat == "kairo" and (d / "synthesis-engine.md").exists():
            se = d / "synthesis-engine.md"
    if se:
        for ln in se.read_text(errors="replace").splitlines():
            if ln.startswith("| ") and any(c in ln for c in ("REPLAY", "STATEBYPASS", "MATH",
                                                             "ENTITLEMENT", "AUTHBYPASS",
                                                             "HWFLASH", "HDRADIO")):
                cells = [c.strip() for c in ln.strip("|").split("|")]
                if len(cells) >= 3 and cells[0] not in ("Class", "---", ""):
                    srcs.append(("kairo/technique-classes",
                                 f"{cells[0]} — {cells[1]}",
                                 "\n".join(f"- {c}" for c in cells)))
    return srcs


def _existing_dates():
    """Preserve the original 'generated' date of files that already exist, so
    regeneration refreshes index + colliding slugs without touching 690+ files."""
    dates = {}
    try:
        for p in OUT.rglob("*.md"):
            try:
                m = re.search(r"^- generated: (\d{4}-\d{2}-\d{2})$",
                              p.read_text(errors="replace"), re.M)
                if m:
                    dates[p.resolve()] = m.group(1)
            except Exception:
                continue
    except Exception:
        pass
    return dates


def emit(args):
    import hashlib
    srcs = collect_sources()
    if args.count:
        payload = {
            "count": len(srcs),
            "sources": len({s for s, _, _ in srcs}),
            "bindings": len(BINDINGS),
            "generated": OUT.exists(),
        }
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print(f"{len(srcs)} technique skill files would be generated "
                  f"from {payload['sources']} source docs ({len(BINDINGS)} binding keys)")
        return 0
    made = 0
    today = datetime.now(timezone.utc).date().isoformat()
    existing_dates = _existing_dates()
    used_paths = {}
    index = ["# SPYDERMONKEY SKILLTREE — the family's technique library",
             "",
             "_generated from the family's REAL canon — one technique per file,_",
             "_WSTG/CWE/ATT&CK-bound, lazy-loaded. regenerate: skilltree.py_",
             ""]
    for src, title, body in sorted(srcs, key=lambda x: (x[0], x[1].lower())):
        slug = _slug(f"{src}-{title}")
        d = OUT / src
        f = d / f"{slug}.md"
        # _slug truncates at 60 chars — on collision, append a stable hash so a
        # later technique never silently overwrites an earlier one.
        if f.resolve() in used_paths:
            digest = hashlib.sha1(f"{src}\0{title}".encode()).hexdigest()[:8]
            slug = f"{slug[:50]}-{digest}"
            f = d / f"{slug}.md"
        used_paths[f.resolve()] = True
        w, c, a = _bindings(f"{title} {body}")
        d.mkdir(parents=True, exist_ok=True)
        generated = existing_dates.get(f.resolve(), today)
        f.write_text(
            f"# {title}\n\n"
            f"- source canon: `{src}.md`\n- bindings: **{w}** · **{c}** · **ATT&CK {a}**\n"
            f"- generated: {generated}\n\n"
            f"## The technique\n\n{body}\n\n"
            f"## Family use\n\n- decisive-test shape lives in the source canon\n"
            f"- walls: validation-only · NO-GAIN · documented-class adaptation only\n")
        made += 1
        index.append(f"- [{title}](skills/{src}/{slug}.md) — `{src}` · {w} · {c} · {a}")
    (REFS / "skilltree-index.md").write_text("\n".join(index) + "\n")
    if args.json:
        print(json.dumps({"count": made, "sources": len({s for s, _, _ in srcs}),
                          "bindings": len(BINDINGS), "out": str(OUT),
                          "index": str(REFS / "skilltree-index.md")}, indent=2))
    else:
        print(f"▸ skilltree: {made} technique skill files → {OUT}/")
        print(f"▸ index: {REFS / 'skilltree-index.md'} ({len(BINDINGS)} binding keys)")
    return 0


LINK_RE = re.compile(
    r"^- \[(?P<title>.+?)\]\((?P<href>skills/[^)]+)\) — "
    r"`(?P<source>[^`]+)` · (?P<wstg>[^ ·]+) · (?P<cwe>[^ ·]+) · (?P<attack>\S+)$",
    re.M)


def verify(json_mode=False):
    """Check the generated tree is internally consistent: every index link
    resolves, every file carries its provenance + bindings, and no orphan file
    is left behind from an older generation run."""
    errors, warnings = [], []
    index_path = REFS / "skilltree-index.md"
    if not index_path.exists():
        errors.append("references/skilltree-index.md missing — run skilltree.py")
        links = []
    else:
        text = index_path.read_text(errors="replace")
        links = [m.groupdict() for m in LINK_RE.finditer(text)]
        if len(links) < 1:
            errors.append("index contains no technique links")
        if "regenerate: skilltree.py" not in text:
            warnings.append("index is missing its regeneration banner")
    linked = {}
    for item in links:
        href = item["href"]
        path = REFS / href
        if href in linked:
            errors.append(f"duplicate index link: {href}")
            continue
        linked[href] = item
        if not path.exists():
            errors.append(f"index link has no file: {href}")
            continue
        body = path.read_text(errors="replace")
        for needle, label in (
                ("- source canon:", "source canon"),
                ("- bindings:", "bindings"),
                ("## The technique", "technique body"),
                ("## Family use", "family use")):
            if needle not in body:
                errors.append(f"{href}: missing {label}")
        if not re.search(r"^- generated: \d{4}-\d{2}-\d{2}$", body, re.M):
            errors.append(f"{href}: missing generated date")
        if item["source"] not in body:
            errors.append(f"{href}: source canon mismatch ({item['source']})")
        for binding in (item["wstg"], item["cwe"], "ATT&CK " + item["attack"]):
            if binding not in body:
                errors.append(f"{href}: binding {binding} not present in file")
    files = sorted(str(p.relative_to(REFS)) for p in OUT.rglob("*.md")) if OUT.exists() else []
    orphans = [f for f in files if f not in linked]
    if orphans:
        warnings.append(f"{len(orphans)} orphan file(s) not in index "
                        f"(e.g. {orphans[0]})")
    payload = {
        "ok": not errors,
        "index": str(index_path),
        "links": len(links),
        "files": len(files),
        "sources": len({i["source"] for i in links}),
        "bindings": len(BINDINGS),
        "orphans": len(orphans),
        "errors": errors[:40],
        "warnings": warnings[:20],
    }
    if json_mode:
        print(json.dumps(payload, indent=2))
    else:
        print("═══ SPYDERMONKEY SKILLTREE VERIFY ═══")
        print(f"  index links: {payload['links']} · files: {payload['files']} "
              f"· sources: {payload['sources']} · orphans: {payload['orphans']}")
        for e in payload["errors"]:
            print(f"  ✗ {e}")
        for w in payload["warnings"]:
            print(f"  ! {w}")
        print(f"═══ {'ALL PASS' if payload['ok'] else 'FAILED'} ═══")
    return 0 if payload["ok"] else 1


def main():
    ap = argparse.ArgumentParser(description="SPYDERMONKEY skilltree generator")
    ap.add_argument("--count", action="store_true")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.verify:
        sys.exit(verify(json_mode=a.json))
    sys.exit(emit(a))


if __name__ == "__main__":
    main()
