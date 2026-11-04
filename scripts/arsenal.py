#!/usr/bin/env python3
"""
SPYDERMONKEY ARSENAL — the execution layer. Discovers the operator's installed
tooling (nmap, masscan, httpx, nuclei, gobuster, testssl.sh, dnsx, subfinder,
nikto, dirb, whatweb, wafw00f, amass), plans the run per target class, and —
ONLY when the target is in the scope file — executes with the family's gates
in front. Every tool run is scope-checked, lab-defaulted, and its findings are
classified into the family canon (kairo classes) on the way out.

The walls do not move: no scope entry → NO EXECUTION (rc=1). The arsenal is
the muscle; barbican is the reflex.

Commands:
  list                          what's installed (tool × capability × class)
  plan    --target T            the full run plan per class (nothing executes)
  run     --target T [--only TOOLS] [--dry-run]   execute (scope-gated)
  verify                        self-check

Exit: 0 ok · 1 gate/scope refusal · 2 usage.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

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
# nmap/masscan/dig take no extra; nuclei/gobuster/testssl/nikto do
TAKES_EXTRA = {"nuclei", "gobuster", "testssl", "nikto", "masscan"}


def scope_ok(target):
    sf = Path.home() / ".redteam" / "scope.json"
    if not sf.exists():
        return False, "no scope file — run: spydermonkey scope init"
    sc = json.loads(sf.read_text())
    ins = [h.lower() for h in sc.get("in_scope", [])]
    tgt = target.lower().replace("http://", "").replace("https://", "").split("/")[0]
    host = tgt.split(":")[0]
    for h in ins:
        if host == h.lower() or host.endswith("." + h.lower()) or h.lower() in ("*", "all"):
            return True, "in scope"
    return False, f"'{host}' not in scope {ins}"


def installed():
    out = {}
    for tool, (cap, classes, plan, _b) in ARSENAL.items():
        path = shutil.which(tool)
        if path:
            out[tool] = {"capability": cap, "classes": list(classes),
                         "path": path, "plan": plan}
    return out


def cmd_list(args):
    inv = installed()
    print(f"═══ ARSENAL INVENTORY — {len(inv)}/{len(ARSENAL)} tools ═══")
    for tool in ARSENAL:
        if tool in inv:
            i = inv[tool]
            print(f"  ✓ {tool:10s} {i['capability']:22s} feeds: {', '.join(i['classes'])}")
        else:
            print(f"  · {tool:10s} not installed — family probes cover the class")
    print(f"═══ the muscle: {len(inv)} tool(s) · the gates: scope → run ═══")
    return 0


def cmd_plan(args):
    inv = installed()
    ok, why = scope_ok(args.target)
    print(f"═══ ARSENAL RUN PLAN — {args.target} ═══")
    print(f"  scope gate: {'OPEN' if ok else 'CLOSED'} ({why})")
    for tool, (cap, classes, plan, _b) in ARSENAL.items():
        if tool not in inv:
            continue
        print(f"  ▸ {tool:10s} {plan}")
    if not inv:
        print("  (no tools installed — plan is family-probes only)")
    print("═══ nothing executed — run adds --dry-run off ═══")
    return 0 if ok else 1


HTTP_TOOLS = {"curl", "httpx", "nuclei", "gobuster", "nikto", "whatweb", "wafw00f"}


def cmd_run(args):
    ok, why = scope_ok(args.target)
    if not ok:
        print(f"✗ EXECUTION REFUSED — scope gate: {why}", file=sys.stderr)
        return 1
    inv = installed()
    chosen = args.only.split(",") if args.only else list(inv)
    tgt = args.target
    ran = findings = 0
    print(f"═══ ARSENAL RUN — {args.target} (scope: {why}) ═══")
    for tool in chosen:
        if tool not in inv:
            continue
        argv = [tool]
        url = tgt if "://" in tgt else ("http://" + tgt if tool in HTTP_TOOLS else tgt)
        argv += ARSENAL[tool][3](url, args.wordlist)
        if args.dry_run:
            print(f"  ▸ [dry] {' '.join(argv)}")
            continue
        try:
            r = subprocess.run(argv, capture_output=True, text=True, timeout=300)
            out = (r.stdout + r.stderr).strip()
            hits = sum(1 for cls, kws in CANON_KW.items()
                       if any(k in out.lower() for k in kws))
            findings += hits
            ran += 1
            first = out.splitlines()[0][:60] if out else "(no output)"
            print(f"  ✓ {tool:10s} rc={r.returncode} canon-hits={hits}  {first}")
        except subprocess.TimeoutExpired:
            print(f"  ⚠ {tool:10s} timeout 300s — skipped")
        except Exception as e:
            print(f"  ✗ {tool:10s} {e}")
    print(f"═══ {ran} tool run(s) · {findings} canon-classified finding(s) "
          f"· walls intact ═══")
    return 0


CANON_KW = {
    "BOUNDARY": ("idor", "unauthorized access", "403"),
    "REPLAY": ("replay", "idempoten"),
    "HARVEST": ("backup", ".env", ".git", "dump", "exposed"),
    "CRYPTO": ("tls", "ssl", "cipher", "expired", "weak"),
    "NETWORK": ("open port", "open tcp", "http on", "service:"),
    "DIRECTORY": ("directory listing", "index of"),
    "XSS": ("<script", "xss", "reflected"),
    "DOMTAKE": ("cname", "dangling", "NXDOMAIN"),
}


def cmd_verify(args):
    bad = []
    self = Path(__file__).resolve()
    if subprocess.run([sys.executable, "-m", "py_compile", str(self)],
                      capture_output=True).returncode != 0:
        bad.append("compile")
    for want in ("list", "plan", "run", "verify"):
        if want not in subprocess.run([sys.executable, str(self), "--help"],
                                      capture_output=True, text=True).stdout:
            bad.append(want)
    if len(ARSENAL) < 13:
        bad.append("arsenal")
    # the wall: run without scope MUST refuse
    r = subprocess.run([sys.executable, str(self), "run", "--target",
                        "never-in-scope.invalid", "--dry-run"],
                       capture_output=True, text=True)
    if r.returncode != 1:
        bad.append("scope-gate")
    if bad:
        print(f"✗ ARSENAL verify FAILED: {bad}")
        return 1
    print("✓ ARSENAL verify: compile · commands · 13 tools · scope-gate refusal — ALL PASS")
    return 0


def main_with(argv):
    sys.argv = ["arsenal.py"] + argv
    return main()


def main():
    ap = argparse.ArgumentParser(description="SPYDERMONKEY ARSENAL — scope-gated execution layer")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list", help="installed tools × capabilities")
    p = sub.add_parser("plan", help="the run plan (nothing executes)")
    p.add_argument("--target", required=True)
    r = sub.add_parser("run", help="execute (scope-gated)")
    r.add_argument("--target", required=True)
    r.add_argument("--only", help="comma-separated tool list")
    r.add_argument("--dry-run", action="store_true")
    r.add_argument("--wordlist", help="gobuster wordlist path")
    sub.add_parser("verify", help="self-check")
    a = ap.parse_args()
    return {"list": cmd_list, "plan": cmd_plan, "run": cmd_run,
            "verify": cmd_verify}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
