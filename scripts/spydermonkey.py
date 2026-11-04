#!/usr/bin/env python3
"""
SPYDERMONKEY — master dispatcher of the HolyShit family. stdlib-only.

Commands:
  tree                    the family + roles + chain
  route    --goal "..."   goal → the mandate sequence to load/run
  run      --target T --url U --domain D [--bundle P] [--boundary-url U2]
           [--probe-ids 1,2] [--parallel] [--resume] [--close] [--dry-run]
                          the full pipeline (delegates to SHIKI assault)
  status   [--target T]   family meta-status (versions + engines + states)
  verify                  meta self-check: subcommands, mandate file, eight engines
  mandate  [--file]       print (or locate) the injectable persona contract
  scope    init|check|show  the scope authority (~/.redteam/scope.json) — the
                          machine-checkable estate gate every live probe honors
  doctor                  health check: engines · scope · campaigns · canon
  bench                   offline route-level benchmark (route accuracy)
  + bench_live.py         LIVE exploitation bench: stdlib vulnerable mini-targets
                          on localhost, real engines scored (sub-task completion)
  + mcp_server.py         the family as 12 MCP tools (stdio JSON-RPC) — any MCP
                          client (Claude Desktop/Cursor) drives the family
  + skilltree.py          per-technique skill files generated from the real canon,
                          WSTG/CWE/ATT&CK-bound (references/skills/ + index)

Exit codes: 0 ok · 1 gate/verify/scope failure · 2 usage error.
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SEC = Path.home() / ".hermes/skills/security"
FAMILY = {
    "barbican": (SEC / "barbican/scripts/barbican.py", "The Shield — first layer (vantage/identity/artifacts/wipe)"),
    "holyshit": (SEC / "holyshit-mode/scripts/finder.py", "The Finder — case canon, recon, dossiers, handoffs"),
    "undercroft": (SEC / "undercroft/scripts/undercroft.py", "The Descent — live auto-engagement on the target's own skin"),
    "3am": (SEC / "3am-shinjitsu/scripts/exploit-intel.py", "The Performer — universal sweep, takeover, growth loop"),
    "kairo": (SEC / "kairo/scripts/kairo.py", "The Synthesizer — findings → attacks for everyone"),
    "kaisha": (SEC / "kaisha/scripts/kaisha.py", "The Ladder — depth below the foothold (era-stack · privesc · lateral)"),
    "shukaku": (SEC / "shukaku/scripts/shukaku.py", "The Harvester — post-compromise catalog · price · disclose (the P5 impact layer)"),
    "shiki": (SEC / "shiki/scripts/shiki.py", "The Command — conducts the whole family as one assault"),
}

ROUTES = [
    ("protect", "barbican"), ("opsec", "barbican"), ("anonymous", "barbican"), ("vantage", "barbican"),
    ("find", "holyshit"), ("recon", "holyshit"), ("dossier", "holyshit"), ("known", "holyshit"),
    ("custom", "undercroft"), ("bundle", "undercroft"), ("logic", "undercroft"),
    ("business", "undercroft"), ("their code", "undercroft"),
    ("attack", "3am"), ("sweep", "3am"), ("take over", "3am"), ("exploit", "3am"),
    ("arm", "kairo"), ("forge", "kairo"), ("vectors", "kairo"), ("weapons", "kairo"), ("chains", "kairo"),
    ("harvest", "shukaku"), ("crown", "shukaku"), ("price", "shukaku"), ("valuation", "shukaku"),
    ("disclose", "shukaku"), ("impact", "shukaku"),
    ("ladder", "kaisha"), ("climb", "kaisha"), ("deepen", "kaisha"), ("privesc", "kaisha"),
    ("lateral", "kaisha"), ("foothold", "kaisha"),
    ("everything", "shiki"), ("full assault", "shiki"), ("together", "shiki"), ("one command", "shiki"),
]

RELAY = ["barbican", "holyshit", "undercroft", "kairo", "3am", "kaisha", "shukaku"]

# stem-matching exceptions: noun forms that must NOT trigger the verb keyword
STEM_BLOCK = {"find": ("ings",)}


def _kw_hit(kw, goal):
    """Word-boundary keyword match. Single words match stems ('protect' hits
    'protecting'); multi-word phrases match on whitespace-separated tokens.
    Stem exceptions (STEM_BLOCK) keep noun forms from hijacking the route:
    'findings' is not the verb 'find'."""
    tokens = kw.split()
    parts = [r"\b" + re.escape(t) for t in tokens]
    block = STEM_BLOCK.get(kw)
    if block:
        parts[-1] += "(?!" + "|".join(b + r"\b" for b in block) + ")"
    parts[-1] += r"\w*"
    return re.search(r"\s+".join(parts), goal) is not None


CMDS = {
    "barbican": "barbican posture --target <t> --vantage vm --alias <alias>   (FIRST)",
    "holyshit": "holyshit recon --domain <d> && holyshit dossier --target <t> → handoff",
    "undercroft": "undercroft run --target <t> --domain <d> --url <u> [--bundle P]",
    "kairo": "kairo forge --target <t> --expand && kairo chain --target <t> --write",
    "3am": "3AM sweep per its SKILL.md §16; absorb kairo's distributed rows first",
    "kaisha": "kaisha ladder --target <t> --host <h> --access <confirmed> && kaisha lateral --target <t> --from <h>",
    "shukaku": "shukaku ingest --target <t> --finding <id> --proof <ref> && shukaku reason --target <t> && shukaku hunt --target <t> [--live U] && shukaku crown … && shukaku feed --target <t> && shukaku report --target <t>",
    "shiki": "shiki assault --target <t> --url <u> --domain <d> [--bundle P] [--parallel] [--resume] [--close]",
}


def cmd_tree(args):
    sk = Path(__file__).resolve().parent.parent / "SKILL.md"
    text = sk.read_text()
    start = text.find("| # |")
    end = text.find("## The Router")
    print(text[start:end] if start >= 0 and end > start else "tree table not found — read SKILL.md")
    return 0


def cmd_route(args):
    goal = args.goal.lower()
    seq = []
    for kw, mandate in ROUTES:
        if mandate not in seq and _kw_hit(kw, goal):
            seq.append(mandate)
    if "everything" in goal or _kw_hit("assault", goal):
        seq = ["shiki"]                     # the one-command override
    elif not seq:
        seq = list(RELAY)                   # documented STANDARD RELAY
    print(f"▸ goal: '{args.goal}'")
    print(f"  → load + run, in order: {' → '.join(seq)}")
    for m in seq:
        print(f"  command: {CMDS[m]}")
    print("  always: barbican posture BEFORE, barbican wipe AFTER (closeout)")
    return 0


def cmd_run(args):
    """The full pipeline = SHIKI assault (the proven path)."""
    shiki = FAMILY["shiki"][0]
    argv = [str(shiki), "assault", "--target", args.target, "--url", args.url,
            "--domain", args.domain]
    if args.bundle:
        argv += ["--bundle", args.bundle]
    if args.boundary_url:
        argv += ["--boundary-url", args.boundary_url]
    if args.probe_ids:
        argv += ["--probe-ids", args.probe_ids]
    if args.parallel:
        argv += ["--parallel"]
    if args.resume:
        argv += ["--resume"]
    if args.close:
        argv += ["--close"]
    print("▸ SPYDERMONKEY runs the family: shiki assault")
    if args.dry_run:
        print("  dry-run — the command that would execute:")
        print("    " + " ".join(argv))
        return 0
    r = subprocess.run(argv)
    return r.returncode


def cmd_status(args):
    print("═══ SPYDERMONKEY — family status ═══")
    for name, (script, role) in FAMILY.items():
        if not script.exists():
            print(f"  ✗ {name:10s} MISSING — {role}")
            continue
        v = subprocess.run([sys.executable, str(script), "verify"],
                           capture_output=True, text=True)
        ok = "✓" if v.returncode == 0 else "✗"
        first = v.stdout.splitlines()[0] if v.stdout else ""
        print(f"  {ok} {name:10s} {first[:70]}")
        print(f"      {role}")
    if args.target:
        camp = Path.home() / ".redteam" / "campaigns" / args.target
        states = [f.name for f in camp.glob("*.json")] if camp.exists() else []
        print(f"  campaign '{args.target}': {states or 'no states yet'}")
    return 0


def cmd_verify(args):
    missing, broken = [], []
    self = Path(__file__).resolve()
    help_out = subprocess.run([sys.executable, str(self), "--help"],
                              capture_output=True, text=True).stdout
    bad = []
    for want in ("tree", "route", "run", "status", "verify", "mandate"):
        if want not in help_out:
            bad.append(f"subcommand {want}")
    mandate = self.parent.parent / "references" / "mandate.md"
    if not mandate.exists():
        bad.append("mandate file")
    for name, (script, _) in FAMILY.items():
        if not script.exists():
            missing.append(name)
            continue
        r = subprocess.run([sys.executable, str(script), "verify"],
                           capture_output=True, text=True)
        if r.returncode != 0:
            broken.append(f"{name} engine")
    if bad or broken or missing:
        print(f"✗ SPYDERMONKEY verify FAILED: {bad + broken}")
        if missing:
            print(f"  ⚠ engines not installed: {', '.join(missing)}")
            print("    the dispatcher needs the family on disk — clone each repo into")
            print("    ~/.hermes/skills/security/<name>/ (see README → Quickstart)")
        return 1
    print("✓ SPYDERMONKEY verify: all eight family engines — ALL PASS")
    return 0


# ── v1.3.0 the scope authority · doctor · bench ───────────────────────────────

SCOPE_PATH = Path.home() / ".redteam" / "scope.json"


def _load_scope(path=None):
    f = Path(path) if path else SCOPE_PATH
    if not f.exists():
        return None
    try:
        return json.loads(f.read_text())
    except Exception:
        return None


def _scope_match(scope, value):
    """Domain-suffix or CIDR matching for a domain/URL/host. Returns True/False."""
    import ipaddress
    from urllib.parse import urlparse
    v = value.strip().lower()
    host = v
    if "://" in v:
        host = urlparse(v).hostname or ""
    try:
        ip = ipaddress.ip_address(host)
        for net in scope.get("in_scope", []):
            try:
                if ip in ipaddress.ip_network(net, strict=False):
                    return True
            except ValueError:
                continue
        for net in scope.get("out_of_scope", []):
            try:
                if ip in ipaddress.ip_network(net, strict=False):
                    return False
            except ValueError:
                continue
        return False
    except ValueError:
        pass
    for o in scope.get("out_of_scope", []):
        if host == o.lower() or host.endswith("." + o.lower()):
            return False
    for i in scope.get("in_scope", []):
        i = i.lower()
        if "://" in i:
            ih = urlparse(i)
            if host == (ih.hostname or "") or (ih.hostname or "").endswith("." + (ih.hostname or "")):
                return True
            if host == i:
                return True
        elif host == i or host.endswith("." + i):
            return True
    return False


def cmd_scope(args):
    if args.action == "init":
        scope = {
            "engagement": args.engagement,
            "in_scope": [s.strip() for s in (args.in_scope or "").split(",") if s.strip()],
            "out_of_scope": [s.strip() for s in (args.out_of_scope or "").split(",") if s.strip()],
            "rules": {"max_rate_rps": args.max_rate or 10, "passive_first": True,
                      "no_destructive": True, "require_scope_check": True},
            "created": datetime.now(timezone.utc).isoformat(),
        }
        f = Path(args.file) if args.file else SCOPE_PATH
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps(scope, indent=2) + "\n")
        print(f"▸ scope authority written: {f}")
        print(f"  engagement: {scope['engagement']} · in-scope: {len(scope['in_scope'])}"
              f" · out-of-scope: {len(scope['out_of_scope'])}")
        print("  every live-probing engine checks this before firing")
        return 0
    if args.action == "check":
        scope = _load_scope(args.file)
        if scope is None:
            if args.strict:
                print("✗ SCOPE CLOSED — no scope authority (spydermonkey scope init)",
                      file=sys.stderr)
                return 1
            print("· no scope authority — engines run ungated (init one: scope init)")
            return 0
        ok = _scope_match(scope, args.value)
        if ok:
            print(f"✓ IN SCOPE — {args.value} under engagement '{scope.get('engagement', '?')}'")
            return 0
        print(f"✗ OUT OF SCOPE — {args.value} is not in the declared estate", file=sys.stderr)
        return 1
    if args.action == "show":
        scope = _load_scope(args.file)
        if scope is None:
            print("· no scope authority — init: spydermonkey scope init")
            return 0
        print(json.dumps(scope, indent=2))
        return 0
    return 2


def cmd_doctor(args):
    print("═══ SPYDERMONKEY DOCTOR ═══")
    ok = True
    import platform
    pv = platform.python_version()
    print(f"  python: {pv}" + ("  ✓" if tuple(map(int, pv.split('.')[:2])) >= (3, 8) else "  ✗ (<3.8)"))
    if tuple(map(int, pv.split('.')[:2])) < (3, 8):
        ok = False
    v = subprocess.run([sys.executable, str(Path(__file__).resolve()), "verify"],
                       capture_output=True, text=True)
    engines = [ln for ln in v.stdout.splitlines() if "family engines" in ln]
    print(f"  engines: {engines[0].strip() if engines else ('FAIL — ' + '; '.join(v.stdout.splitlines()[0:1]))}")
    ok = ok and v.returncode == 0
    scope = _load_scope()
    if scope:
        print(f"  scope:   '{scope.get('engagement', '?')}' in={len(scope.get('in_scope', []))}"
              f" out={len(scope.get('out_of_scope', []))} rules={len(scope.get('rules', {}))}  ✓")
    else:
        print("  scope:   no authority (scope init — recommended)")
    camp = Path.home() / ".redteam" / "campaigns"
    if camp.exists():
        n = len([d for d in camp.iterdir() if d.is_dir()])
        print(f"  campaigns: {n} dir(s)")
        stale = 0
        for d in camp.iterdir():
            for f in d.glob("*state*.json"):
                try:
                    json.loads(f.read_text())
                except Exception:
                    stale += 1
        if stale:
            print(f"  ! {stale} corrupt state file(s)")
            ok = False
    lv = Path.home() / ".redteam" / "learned-vectors.jsonl"
    if lv.exists():
        rows = [l for l in lv.read_text().splitlines() if l.strip()]
        print(f"  canon:   {len(rows)} learned-vector row(s) (3AM promote-ready)")
    print(f"═══ {'HEALTHY' if ok else 'ATTENTION NEEDED'} ═══")
    return 0 if ok else 1


# canned route-level benchmark: goal → expected mandate sequence (first mandate)
BENCH_CASES = [
    ("protect my opsec", "barbican"),
    ("recon the domain", "holyshit"),
    ("their custom bundle logic", "undercroft"),
    ("take over the session", "3am"),
    ("forge weapons from findings", "kairo"),
    ("climb the ladder on the host", "kaisha"),
    ("price what they could take", "shukaku"),
    ("full assault everything", "shiki"),
    ("zzz unmapped goal qqq", "barbican"),  # relay head
]


def cmd_bench(args):
    print("═══ SPYDERMONKEY BENCH (offline, route-level) ═══")
    hits = 0
    for goal, want in BENCH_CASES:
        r = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                            "route", "--goal", goal], capture_output=True, text=True)
        first = ""
        for ln in r.stdout.splitlines():
            if "load + run" in ln:
                first = ln.split(":")[-1].strip().split(" → ")[0]
                break
        mark = "✓" if first == want else "✗"
        hits += mark == "✓"
        print(f"  {mark} '{goal[:38]}' → {first} (want {want})")
    pct = 100.0 * hits / len(BENCH_CASES)
    print(f"═══ route accuracy: {hits}/{len(BENCH_CASES)} = {pct:.1f}% ═══")
    print("  (route-level only — exploitation benchmarks are the next frontier)")
    return 0 if pct >= 90 else 1


def cmd_mandate(args):
    mfile = Path(__file__).resolve().parent.parent / "references" / "mandate.md"
    if args.file:
        print(str(mfile))
        return 0
    print(mfile.read_text())
    return 0


def main():
    ap = argparse.ArgumentParser(description="SPYDERMONKEY — master dispatcher of the HolyShit family")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("tree", help="the family + roles + chain")
    r = sub.add_parser("route", help="goal → mandate sequence")
    r.add_argument("--goal", required=True)
    rn = sub.add_parser("run", help="the full pipeline (SHIKI assault)")
    rn.add_argument("--target", required=True)
    rn.add_argument("--url", required=True)
    rn.add_argument("--domain", required=True)
    rn.add_argument("--bundle")
    rn.add_argument("--boundary-url")
    rn.add_argument("--probe-ids")
    rn.add_argument("--parallel", action="store_true")
    rn.add_argument("--resume", action="store_true")
    rn.add_argument("--close", action="store_true")
    rn.add_argument("--dry-run", action="store_true", help="print the delegated command; do not execute")
    s = sub.add_parser("status", help="family meta-status")
    s.add_argument("--target")
    sub.add_parser("verify", help="meta self-check")
    md = sub.add_parser("mandate", help="print the injectable mandate (persona contract, model-agnostic)")
    md.add_argument("--file", action="store_true", help="print path only")
    sc = sub.add_parser("scope", help="the scope authority: init · check · show")
    sc.add_argument("action", choices=("init", "check", "show"))
    sc.add_argument("--engagement")
    sc.add_argument("--in-scope", help="comma domains/CIDRs/urls")
    sc.add_argument("--out-of-scope", help="comma domains/CIDRs")
    sc.add_argument("--max-rate", type=int, help="max requests/sec (rules)")
    sc.add_argument("--value", help="domain/url/host to check")
    sc.add_argument("--file", help="scope file (default ~/.redteam/scope.json)")
    sc.add_argument("--strict", action="store_true", help="no scope authority → rc=1")
    doc = sub.add_parser("doctor", help="full health check: engines · scope · states · canon")
    bn = sub.add_parser("bench", help="offline route-level benchmark (route accuracy)")
    a = ap.parse_args()
    if a.cmd == "tree":
        return cmd_tree(a)
    if a.cmd == "route":
        return cmd_route(a)
    if a.cmd == "run":
        return cmd_run(a)
    if a.cmd == "status":
        return cmd_status(a)
    if a.cmd == "verify":
        return cmd_verify(a)
    if a.cmd == "mandate":
        return cmd_mandate(a)
    if a.cmd == "scope":
        return cmd_scope(a)
    if a.cmd == "doctor":
        return cmd_doctor(a)
    if a.cmd == "bench":
        return cmd_bench(a)
    return 2


if __name__ == "__main__":
    sys.exit(main())
