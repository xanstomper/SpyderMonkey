#!/usr/bin/env python3
"""SPYDERMONKEY CATALOG MATERIALIZER — the archive → workbench lane (v7.3.0).

The 66,569-entry catalog is an INDEX. This engine turns any index line into a
REAL artifact on disk plus a runnable recipe:

    exploit-db: edb-16929   → the actual exploit SOURCE from the exploitdb tree
    nuclei:     CVE-2012-4242 → the actual YAML template (nuclei-executable)
    metasploit: xslt_password_reset → the actual module .rb from the install

Runbook mode prints the full recipe with ZERO side effects (no network, no
disk writes). Materialize fetches the artifact: local mirrors (shallow clones
or native packages) are created on first explicit materialize and reused.
Execution of materialized artifacts still goes through `arsenal` — scope-gated.
This lane hands the operator the payload + the recipe, never a trigger.

Exit: 0 ok · 1 blocked/missing dependency · 2 usage.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scope_authority as sa  # noqa: E402

VERSION = "7.3.0"

MIRRORS = {
    "exploitdb": "https://github.com/offensive-security/exploitdb.git",
    "nuclei-templates": "https://github.com/projectdiscovery/nuclei-templates.git",
}

# language → (build line, run line)
BUILD = {
    ".c":   ("gcc -o {base} {path} 2>/dev/null || gcc {path} -o {base} -lssl -lcrypto",
             "./{base} <target>"),
    ".cpp": ("g++ -o {base} {path} -lssl -lcrypto", "./{base} <target>"),
    ".py":  ("", "python3 {path} <target>"),
    ".rb":  ("", "ruby {path} <target>"),
    ".php": ("", "php {path} <target>"),
    ".pl":  ("", "perl {path} <target>"),
    ".sh":  ("", "bash {path} <target>"),
    ".java": ("javac {path}", "java {base} <target>"),
    ".txt": ("", "READ the PoC — manual reproduction, walls first (documented-PoC only)"),
}


def _home() -> Path:
    return sa.redteam_home()


def _surge() -> dict:
    p = (Path(__file__).resolve().parent.parent / "references"
         / "tool-catalog-surge.json")
    try:
        return json.loads(p.read_text(encoding="utf-8")).get("sections", {})
    except Exception:
        return {}


def _find_entry(kind: str, ident: str) -> dict | None:
    sec = {"exploit-db": "exploit-db", "nuclei": "nuclei-templates",
           "metasploit": "metasploit"}.get(kind)
    if not sec:
        return None
    for r in _surge().get(sec, []):
        nm = (r.get("name") or "").lower()
        if nm == ident.lower() or nm == f"{kind}-{ident}".lower():
            return r
        if kind == "exploit-db" and nm == f"edb-{ident}".lower():
            return r
    return None


def _desc_path(entry: dict) -> str | None:
    """The artifact path embedded in a surge entry's description."""
    d = entry.get("desc") or ""
    m = re.search(r":\s*([A-Za-z0-9_./-]+\.(?:yaml|rb|c|py|php|pl|sh|java|txt|cpp))", d)
    return m.group(1) if m else None


def _resolve(ns) -> tuple[dict | None, str | None, str | None]:
    """kind, ident → (surge entry, resolved repo-relative path, reason)."""
    ident = (ns.id or "").strip().lower()
    if not ident:
        return None, None, None
    entry = _find_entry(ns.kind, ident)
    if entry:
        rp = _desc_path(entry)
        if rp:
            return entry, rp, None
    # direct path-style id (no surge entry needed)
    return entry, (ident if "." in ident else None), None


# ── exploit-db ──────────────────────────────────────────────────────────────

def _edb_root() -> tuple[Path | None, str]:
    cand = _home() / "exploitdb"
    return (cand if cand.exists() else None,
            "searchsploit (apt: exploitdb) or git clone --depth 1 "
            f"{MIRRORS['exploitdb']} {cand}")


def _edb_path(root: Path, entry: dict) -> Path | None:
    platform = (entry.get("cat") or "exploit/").split("/", 1)[-1]
    eid = re.sub(r"\D", "", entry.get("name") or "")
    if not eid:
        return None
    hits = sorted(root.glob(f"exploits/{platform}/{eid}.*"))
    return hits[0] if hits else None


# ── nuclei ──────────────────────────────────────────────────────────────────

def _nuclei_root() -> tuple[Path | None, str]:
    cand = _home() / "nuclei-templates"
    return (cand if cand.exists() else None,
            f"git clone --depth 1 {MIRRORS['nuclei-templates']} {cand}")


def _nuclei_path(root: Path, rel: str) -> Path | None:
    for cand in (rel, f"detection/{rel}", rel.removeprefix("detection/")):
        p = root / cand
        if p.exists():
            return p
    return None


# ── metasploit ──────────────────────────────────────────────────────────────

def _msf_root() -> tuple[Path | None, str]:
    for cand in ("/usr/share/metasploit-framework/modules",
                 "/opt/metasploit-framework/embedded/framework/modules"):
        if Path(cand).exists():
            return Path(cand), ""
    return None, ("metasploit not installed — install it first "
                  "(arsenal install --tool msfconsole / official installer)")


def _usage_header(path: Path, limit: int = 120) -> str:
    """The artifact's own comment header — the author's usage instructions."""
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return ""
    out, in_block = [], False
    for ln in lines[:400]:
        s = ln.lstrip()
        if s.startswith(("/*", "**", "#", "//", "<!--", "=begin", "#!/", "/*")):
            if not in_block and out:
                if len(out) > 2:
                    break
            in_block = True
            out.append(ln)
        elif in_block and not s.strip():
            out.append(ln)
        elif in_block:
            if s.startswith(("*", "*/")):
                out.append(ln)
                continue
            break
        if len(out) >= limit:
            break
    return "\n".join(out).strip()


def runbook(kind: str, ident: str) -> dict:
    entry, rel, _ = _resolve(argparse.Namespace(kind=kind, id=ident))
    if not entry and not rel:
        return {"ok": False, "why": f"no surge entry or path for '{kind}:{ident}'"}
    name = (entry or {}).get("name", ident)
    steps: list[str] = []
    if kind == "exploit-db":
        eid = re.sub(r"\D", "", name)
        root, how = _edb_root()
        steps.append(f"mirror:   {how}" if not root else f"mirror:   found at {root}")
        steps.append(f"locate:   searchsploit -p {name}  (or: ls exploits/<platform>/{eid}.*)")
        steps.append(f"materialize: spydermonkey catalog materialize --kind exploit-db --id {eid}")
        steps.append("build:   gcc for .c · g++ for .cpp · python3 for .py · ruby for .rb "
                     "— materialize prints the exact line")
        steps.append("run:     execute against an IN-SCOPE target only "
                     "(documented-PoC class, walls first)")
    elif kind == "nuclei":
        if not rel:
            return {"ok": False, "why": "no template path in entry desc"}
        root, how = _nuclei_root()
        steps.append(f"mirror:   {how}" if not root else f"mirror:   found at {root}")
        steps.append("fire:     nuclei -t <template.yaml> -u <IN-SCOPE-URL> -o findings.txt")
        steps.append("          (update templates first: nuclei -update-templates)")
    elif kind == "metasploit":
        if not rel:
            return {"ok": False, "why": "no module path in entry desc"}
        root, how = _msf_root()
        steps.append(f"mirror:   {how}" if not root else f"mirror:   found at {root}")
        mod = re.sub(r"\.rb$", "", rel or "")
        steps.append(f"module:   {mod}")
        steps.append(f"fire:     msfconsole -q -x \"use {mod}; info; run\"")
    steps.append("gate:     execution scope-gated — arsenal run / gate, estate only")
    return {"ok": True, "kind": kind, "id": ident, "name": name, "path": rel,
            "steps": steps}


def materialize(kind: str, ident: str, out: str | None, dry_run: bool) -> dict:
    entry, rel, _ = _resolve(argparse.Namespace(kind=kind, id=ident))
    if not entry and not rel:
        return {"ok": False, "why": f"no surge entry or path for '{kind}:{ident}'"}
    out_dir = Path(out) if out else Path.cwd()
    out_dir.mkdir(parents=True, exist_ok=True)
    name = (entry or {}).get("name", ident)
    events: list[str] = []
    src: Path | None = None
    hdr = ""

    def _run(cmd: list[str]) -> int:
        events.append(" ".join(str(c) for c in cmd))
        if dry_run:
            return 0
        return subprocess.run(cmd).returncode

    if kind == "exploit-db":
        eid = re.sub(r"\D", "", name)
        root, how = _edb_root()
        if not root:
            if dry_run:
                events.append(f"# mirror missing — would run: {how}")
            else:
                r = _run(["git", "clone", "--depth", "1", MIRRORS["exploitdb"],
                          str(_home() / "exploitdb")])
                if r != 0:
                    return {"ok": False, "why": "exploitdb clone failed",
                            "events": events}
                root = _home() / "exploitdb"
        src = _edb_path(root, entry) if (entry and root) else None
        if not src and dry_run:
            src = out_dir / f"{eid}.EXT"
        if not src:
            return {"ok": False, "why": f"file for {name} not in mirror tree",
                    "events": events}
        if not dry_run:
            shutil.copy2(src, out_dir / src.name)
        events.append(f"materialized: {out_dir / src.name}  (from {src})")
        ext = src.suffix.lower()
        if ext in BUILD:
            b, rl = BUILD[ext]
            if b:
                events.append("build:   " + b.format(base=src.stem, path=src.name))
            events.append("run:     " + rl.format(base=src.stem, path=src.name))
        hdr = "" if dry_run else _usage_header(src)
    elif kind == "nuclei":
        root, how = _nuclei_root()
        if not root:
            if dry_run:
                events.append(f"# mirror missing — would run: {how}")
            else:
                r = _run(["git", "clone", "--depth", "1", MIRRORS["nuclei-templates"],
                          str(_home() / "nuclei-templates")])
                if r != 0:
                    return {"ok": False, "why": "nuclei-templates clone failed",
                            "events": events}
                root = _home() / "nuclei-templates"
        tmpl = _nuclei_path(root, rel) if (rel and root) else None
        if not tmpl and dry_run:
            tmpl = out_dir / (rel or "template.yaml").replace("/", "_")
        if not tmpl:
            return {"ok": False, "why": f"template '{rel}' not in mirror tree",
                    "events": events}
        if not dry_run:
            shutil.copy2(tmpl, out_dir / tmpl.name)
        events.append(f"materialized: {out_dir / tmpl.name}  (from {tmpl})")
        events.append("fire:     nuclei -t " + tmpl.name +
                      " -u <IN-SCOPE-URL> -o findings.txt")
        hdr = "" if dry_run else _usage_header(tmpl)
    elif kind == "metasploit":
        root, how = _msf_root()
        if not root:
            events.append("# " + how)
            return {"ok": False, "why": how, "events": events}
        mod = re.sub(r"\.rb$", "", rel or "")
        modfile = root / f"{mod}.rb"
        if not modfile.exists() and not dry_run:
            return {"ok": False, "why": f"module {mod} not in install", "events": events}
        if not dry_run:
            shutil.copy2(modfile, out_dir / modfile.name)
        events.append(f"materialized: {out_dir / modfile.name}  (from {modfile})")
        events.append(f"fire:     msfconsole -q -x \"use {mod}; info; run\"")
        hdr = "" if dry_run else _usage_header(modfile)

    return {"ok": True, "kind": kind, "id": ident, "name": name, "out": str(out_dir),
            "events": events, "usage_header": hdr}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="SPYDERMONKEY CATALOG MATERIALIZER")
    sub = ap.add_subparsers(dest="cmd", required=True)
    rb = sub.add_parser("runbook", help="print the full execution recipe (zero side effects)")
    rb.add_argument("--kind", choices=("exploit-db", "nuclei", "metasploit"), required=True)
    rb.add_argument("--id", required=True, help="entry name/id (edb-16929, CVE-2012-4242, xslt_password_reset, or a path)")
    rb.add_argument("--json", action="store_true")
    mz = sub.add_parser("materialize", help="fetch the REAL artifact to disk (mirrors built on first use)")
    mz.add_argument("--kind", choices=("exploit-db", "nuclei", "metasploit"), required=True)
    mz.add_argument("--id", required=True)
    mz.add_argument("--out", help="target dir (default: cwd)")
    mz.add_argument("--dry-run", action="store_true", help="print every command, touch nothing")
    mz.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "runbook":
        res = runbook(a.kind, a.id)
    else:
        res = materialize(a.kind, a.id, getattr(a, "out", None),
                          bool(getattr(a, "dry_run", False)))
    if a.json:
        print(json.dumps(res, indent=2))
    else:
        if not res.get("ok"):
            print(f"✗ {res.get('why', 'failed')}", file=sys.stderr)
            return 1
        print(f"═══ {res['kind'].upper()} {res['id']} — {res.get('name', '')} ═══")
        for e in res.get("steps", res.get("events", [])):
            print("  ▸ " + e)
        uh = res.get("usage_header") or ""
        if uh:
            print("── the artifact's own usage header ──")
            print(uh[:4500])
    return 0 if res.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())