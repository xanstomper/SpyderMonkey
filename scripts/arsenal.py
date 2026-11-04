#!/usr/bin/env python3
"""
SPYDERMONKEY ARSENAL — the execution layer. Discovers the operator's installed
tooling (nmap, masscan, httpx, nuclei, gobuster, testssl.sh, dnsx, subfinder,
nikto, dirb, whatweb, wafw00f, amass), plans the run per target class, and —
ONLY when the target is inside the shared scope authority — executes with the
family's gates in front. Every tool run is scope-checked, lab-defaulted, and
its output is classified into the family canon on the way out.

v4.0 uses scripts/scope_authority.py (the same implementation as the dispatcher,
gate, ledger, MCP server and live bench): CIDRs, deny precedence, expiry, URL
paths, ports and rate limits are all honored. No authority → NO EXECUTION.

Commands:
  list                          what's installed (tool × capability × class)
  plan    --target T            the full run plan per class (nothing executes)
  run     --target T [--only T1,T2] [--dry-run]   execute (scope-gated)
  verify                        self-check in a throwaway scope

Exit: 0 ok · 1 gate/scope refusal · 2 usage.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scope_authority as sa  # noqa: E402

VERSION = "4.0.0"

# tool → (capability, canon classes it feeds, plan line, args builder)
ARSENAL = {
    "nmap":      ("port/service scan", ("network", "services"),
                  "top-1000 TCP + service versions",
                  lambda t, extra=None: ["-Pn", "--top-ports", "1000", "-sV", "--open", t]),
    "httpx":     ("http surface probe", ("web", "api"),
                  "live-host + title + tech fingerprint",
                  lambda t, extra=None: [t, "-title", "-tech-detect", "-status-code"]),
    "nuclei":    ("vuln templates", ("web", "api"),
                  "medium+ severity template sweep (read-only tags)",
                  lambda t, extra=None: ["-u", t, "-severity", "medium,high,critical",
                                         "-tags", "cve,misconfig,exposure", "-silent"]),
    "gobuster":  ("path/content discovery", ("web", "harvest"),
                  "dir sweep with common wordlist",
                  lambda t, extra=None: ["dir", "-u", t, "-w",
                                         str(extra or "/usr/share/wordlists/dirb/common.txt"),
                                         "-q", "--no-error-continuation"]),
    "testssl":   ("tls posture", ("crypto", "config"),
                  "tls versions/ciphers/chain audit",
                  lambda t, extra=None: ["--quiet", "--color", "0", t]),
    "dnsx":      ("dns inventory", ("dns", "domtake"),
                  "A/AAAA/CNAME/MX/TXT enumeration",
                  lambda t, extra=None: ["-silent", "-a", "-cname", "-mx", "-txt", t]),
    "subfinder": ("subdomain enum", ("dns", "domtake"),
                  "passive subdomain discovery",
                  lambda t, extra=None: ["-d", t, "-all", "-silent"]),
    "whatweb":   ("tech fingerprint", ("web", "api"),
                  "web tech identification",
                  lambda t, extra=None: ["-q", "-a", "3", t]),
    "wafw00f":   ("waf detection", ("web", "edge"),
                  "waf/edge identification",
                  lambda t, extra=None: [t]),
    "nikto":     ("web misconfig sweep", ("web", "config"),
                  "classic misconfig/exposure checks",
                  lambda t, extra=None: ["-quiet", "-nolisting", t]),
    "masscan":   ("fast port scan", ("network", "services"),
                  "high-rate tcp syn (lab nets only)",
                  lambda t, extra=None: ["-p1-65535", "--rate", "1000", t]),
    "dig":       ("dns records", ("dns",),
                  "zone records via system resolver",
                  lambda t, extra=None: ["+short", "ANY", t]),
    "curl":      ("http fetch", ("web",),
                  "header/body fetch (always present)",
                  lambda t, extra=None: ["-sSI", "-m", "10", t]),
}

TAKES_EXTRA = {"nuclei", "gobuster", "testssl", "nikto", "masscan"}
HTTP_TOOLS = {"curl", "httpx", "nuclei", "gobuster", "nikto", "whatweb", "wafw00f"}
CANON_KW = {
    "BOUNDARY": ("idor", "unauthorized access", "403"),
    "REPLAY": ("replay", "idempoten"),
    "HARVEST": ("backup", ".env", ".git", "dump", "exposed"),
    "CRYPTO": ("tls", "ssl", "cipher", "expired", "weak"),
    "NETWORK": ("open port", "open tcp", "http on", "service:"),
    "DIRECTORY": ("directory listing", "index of"),
    "XSS": ("<script", "xss", "reflected"),
    "DOMTAKE": ("cname", "dangling", "nodomain", "nxdomain"),
}


def _host(target: str) -> str:
    if "://" in target:
        return urlsplit(target).hostname or target
    return target.split("/")[0].split(":")[0]


def _url(target: str) -> str:
    return target if "://" in target else "http://" + target


def _state_path(target: str) -> Path:
    try:
        name = sa.safe_name(target, "target")
    except sa.ScopeError:
        name = re.sub(r"[^A-Za-z0-9._-]+", "-", target)[:64] or "target"
    return sa.campaigns_root() / name / "arsenal-state.json"


def _record(target: str, row: dict) -> None:
    try:
        p = _state_path(target)
        p.parent.mkdir(parents=True, exist_ok=True)
        state = {}
        if p.exists():
            try:
                state = json.loads(p.read_text())
            except Exception:
                state = {}
        state.setdefault("target", target)
        state.setdefault("version", VERSION)
        state.setdefault("runs", []).append(row)
        state["runs"] = state["runs"][-20:]
        state["updated"] = datetime.now(timezone.utc).isoformat()
        tmp = p.with_name(p.name + f".tmp.{os.getpid()}")
        tmp.write_text(json.dumps(state, indent=2) + "\n")
        os.chmod(tmp, 0o600)
        os.replace(tmp, p)
    except OSError:
        pass


def scope_verdict(target: str, scope_file: str | None = None) -> tuple[bool, str]:
    ok, reason, _ = sa.check(target, file=scope_file, strict=True,
                             audit=True, allow_lab=True)
    return ok, reason


def installed() -> dict:
    out = {}
    for tool, (cap, classes, plan, _b) in ARSENAL.items():
        path = shutil.which(tool)
        if path:
            out[tool] = {"capability": cap, "classes": list(classes),
                         "path": path, "plan": plan}
    return out


def _emit(args, payload, text: str | None = None) -> None:
    if getattr(args, "json", False):
        print(json.dumps(payload, indent=2))
    elif text is not None:
        print(text)


def cmd_list(args):
    inv = installed()
    rows = []
    for tool, (cap, classes, plan, _b) in ARSENAL.items():
        rows.append({"tool": tool, "installed": tool in inv,
                     "path": inv.get(tool, {}).get("path", ""),
                     "capability": cap, "classes": list(classes), "plan": plan})
    payload = {"version": VERSION, "tools": rows, "installed": len(inv),
               "total": len(ARSENAL)}
    if getattr(args, "json", False):
        _emit(args, payload)
        return 0
    print(f"═══ ARSENAL INVENTORY — {len(inv)}/{len(ARSENAL)} tools ═══")
    for r in rows:
        if r["installed"]:
            print(f"  ✓ {r['tool']:10s} {r['capability']:22s} feeds: {', '.join(r['classes'])}")
        else:
            print(f"  · {r['tool']:10s} not installed — family probes cover the class")
    print(f"═══ the muscle: {len(inv)} tool(s) · the gate: shared scope authority ═══")
    return 0


def cmd_plan(args):
    inv = installed()
    ok, why = scope_verdict(args.target, getattr(args, "scope_file", None))
    plan = []
    for tool, (cap, classes, line, builder) in ARSENAL.items():
        if tool not in inv:
            continue
        target = _url(args.target) if tool in HTTP_TOOLS else _host(args.target)
        try:
            argv = [tool] + builder(target, getattr(args, "wordlist", None))
        except Exception as e:
            argv = [tool, f"<builder error: {e}>"]
        plan.append({"tool": tool, "capability": cap, "classes": list(classes),
                     "plan": line, "argv": argv})
    payload = {"version": VERSION, "target": args.target, "scope_ok": ok,
               "scope": why, "plan": plan, "installed": len(inv),
               "executed": False}
    if getattr(args, "json", False):
        _emit(args, payload)
    else:
        print(f"═══ ARSENAL RUN PLAN — {args.target} ═══")
        print(f"  scope gate: {'OPEN' if ok else 'CLOSED'} ({why})")
        for p in plan:
            print(f"  ▸ {p['tool']:10s} {p['plan']}")
        if not plan:
            print("  (no tools installed — plan is family-probes only)")
        print("═══ nothing executed — run adds --dry-run off ═══")
    return 0 if ok else 1


def cmd_run(args):
    ok, why = scope_verdict(args.target, getattr(args, "scope_file", None))
    if not ok:
        print(f"✗ EXECUTION REFUSED — scope gate: {why}", file=sys.stderr)
        if getattr(args, "json", False):
            _emit(args, {"target": args.target, "scope_ok": False,
                         "error": why, "executed": False})
        return 1
    inv = installed()
    if args.only:
        chosen = [s.strip() for s in args.only.split(",") if s.strip()]
        unknown = [t for t in chosen if t not in ARSENAL]
        if unknown:
            print(f"✗ unknown tool(s): {', '.join(unknown)}", file=sys.stderr)
            return 2
    else:
        chosen = list(inv)
    tgt = args.target
    timeout = max(5, min(int(getattr(args, "timeout", 300) or 300), 3600))
    started = datetime.now(timezone.utc).isoformat()
    runs, ran, failed, findings = [], 0, 0, []
    if not getattr(args, "json", False):
        print(f"═══ ARSENAL RUN — {args.target} (scope: {why}) ═══")
    for tool in chosen:
        if tool not in inv:
            continue
        target = _url(tgt) if tool in HTTP_TOOLS else _host(tgt)
        argv = [tool] + ARSENAL[tool][3](target, args.wordlist)
        row = {"tool": tool, "argv": argv, "rc": None, "hits": [],
               "output": "", "elapsed": 0.0}
        if getattr(args, "dry_run", False):
            row["skipped"] = "dry-run"
            runs.append(row)
            if not getattr(args, "json", False):
                print(f"  ▸ [dry] {' '.join(argv)}")
            continue
        try:
            r = subprocess.run(argv, capture_output=True, text=True, timeout=timeout)
            out = (r.stdout + r.stderr).strip()
            hits = [cls for cls, kws in CANON_KW.items()
                    if any(k in out.lower() for k in kws)]
            row.update({"rc": r.returncode, "hits": hits, "output": out[:12000]})
            runs.append(row)
            ran += 1
            if r.returncode != 0:
                failed += 1
            findings.extend({"tool": tool, "class": c, "target": target}
                            for c in hits)
            if not getattr(args, "json", False):
                first = out.splitlines()[0][:60] if out else "(no output)"
                print(f"  ✓ {tool:10s} rc={r.returncode} canon-hits={len(hits)}  {first}")
        except subprocess.TimeoutExpired:
            failed += 1
            row.update({"rc": 124, "error": f"timeout {timeout}s"})
            runs.append(row)
            if not getattr(args, "json", False):
                print(f"  ⚠ {tool:10s} timeout {timeout}s — skipped")
        except Exception as e:
            failed += 1
            row.update({"rc": 1, "error": str(e)})
            runs.append(row)
            if not getattr(args, "json", False):
                print(f"  ✗ {tool:10s} {e}")
    payload = {"version": VERSION, "target": args.target, "scope_ok": True,
               "scope": why, "dry_run": bool(getattr(args, "dry_run", False)),
               "ran": ran, "failed": failed, "tools": runs,
               "findings": findings, "started": started}
    _record(args.target, {"at": started, "scope": why,
                          "dry_run": payload["dry_run"], "ran": ran,
                          "failed": failed, "tools": [r["tool"] for r in runs],
                          "hits": [f["class"] for f in findings]})
    if getattr(args, "output_dir", None):
        outdir = Path(args.output_dir).expanduser()
        outdir.mkdir(parents=True, exist_ok=True)
        out = outdir / f"arsenal-{sa.safe_name(args.target, 'target')}.json"
        out.write_text(json.dumps(payload, indent=2) + "\n")
        payload["output"] = str(out)
    if getattr(args, "json", False):
        _emit(args, payload)
    else:
        print(f"═══ {ran} tool run(s) · {len(findings)} canon-classified candidate(s)"
              f" · {failed} failure(s) · walls intact ═══")
    if payload["dry_run"]:
        return 0
    if chosen and inv and ran == 0:
        return 1
    return 0


def cmd_verify(args):
    bad = []
    self = Path(__file__).resolve()
    if subprocess.run([sys.executable, "-m", "py_compile", str(self)],
                      capture_output=True).returncode != 0:
        bad.append("compile")
    help_out = subprocess.run([sys.executable, str(self), "--help"],
                              capture_output=True, text=True).stdout
    for want in ("list", "plan", "run", "verify"):
        if want not in help_out:
            bad.append(want)
    if len(ARSENAL) < 13:
        bad.append("arsenal-inventory")
    with tempfile.TemporaryDirectory(prefix="arsenal-verify-") as td:
        absent = str(Path(td) / "no-scope.json")
        r = subprocess.run([sys.executable, str(self), "run", "--target",
                            "never-in-scope.invalid", "--dry-run",
                            "--scope-file", absent], capture_output=True, text=True)
        if r.returncode != 1:
            bad.append("scope-gate-run")
        r = subprocess.run([sys.executable, str(self), "plan", "--target",
                            "never-in-scope.invalid", "--scope-file", absent],
                           capture_output=True, text=True)
        if r.returncode != 1:
            bad.append("scope-gate-plan")
        r = subprocess.run([sys.executable, str(self), "list", "--json"],
                           capture_output=True, text=True)
        try:
            data = json.loads(r.stdout)
            if data.get("total") != len(ARSENAL):
                bad.append("json-list")
        except Exception:
            bad.append("json-list")
    if bad:
        print(f"✗ ARSENAL verify FAILED: {bad}")
        return 1
    print("✓ ARSENAL verify: compile · commands · 13 tools · shared-scope refusal"
          " · JSON surface — ALL PASS")
    return 0


def _extract(argv):
    out, json_flag, scope_file = [], False, None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--json":
            json_flag = True
            i += 1
            continue
        if a == "--scope-file":
            if i + 1 >= len(argv):
                print("✗ --scope-file needs a value", file=sys.stderr)
                raise SystemExit(2)
            scope_file = argv[i + 1]
            i += 2
            continue
        if a.startswith("--scope-file="):
            scope_file = a.split("=", 1)[1]
            i += 1
            continue
        out.append(a)
        i += 1
    return out, json_flag, scope_file


def main(argv=None):
    raw, json_flag, scope_file = _extract(list(sys.argv[1:] if argv is None else argv))
    ap = argparse.ArgumentParser(description="SPYDERMONKEY ARSENAL — scope-gated execution layer")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list", help="installed tools × capabilities")
    p = sub.add_parser("plan", help="the run plan (nothing executes)")
    p.add_argument("--target", required=True)
    p.add_argument("--wordlist")
    r = sub.add_parser("run", help="execute (scope-gated)")
    r.add_argument("--target", required=True)
    r.add_argument("--only", help="comma-separated tool list")
    r.add_argument("--dry-run", action="store_true")
    r.add_argument("--wordlist", help="gobuster wordlist path")
    r.add_argument("--timeout", type=int, default=300)
    r.add_argument("--output-dir")
    sub.add_parser("verify", help="self-check")
    a = ap.parse_args(raw)
    a.json = json_flag
    a.scope_file = scope_file
    return {"list": cmd_list, "plan": cmd_plan, "run": cmd_run,
            "verify": cmd_verify}[a.cmd](a)


def main_with(argv):
    return main(argv)


if __name__ == "__main__":
    sys.exit(main())
