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
  verify                  meta self-check: subcommands, mandate file, six engines
  mandate  [--file]       print (or locate) the injectable persona contract

Exit codes: 0 ok · 1 gate/verify failure · 2 usage error.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

SEC = Path.home() / ".hermes/skills/security"
FAMILY = {
    "barbican": (SEC / "barbican/scripts/barbican.py", "The Shield — first layer (vantage/identity/artifacts/wipe)"),
    "holyshit": (SEC / "holyshit-mode/scripts/finder.py", "The Finder — case canon, recon, dossiers, handoffs"),
    "undercroft": (SEC / "undercroft/scripts/undercroft.py", "The Descent — live auto-engagement on the target's own skin"),
    "3am": (SEC / "3am-shinjitsu/scripts/exploit-intel.py", "The Performer — universal sweep, takeover, growth loop"),
    "kairo": (SEC / "kairo/scripts/kairo.py", "The Synthesizer — findings → attacks for everyone"),
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
    ("everything", "shiki"), ("full assault", "shiki"), ("together", "shiki"), ("one command", "shiki"),
]

RELAY = ["barbican", "holyshit", "undercroft", "kairo", "3am", "shukaku"]

CMDS = {
    "barbican": "barbican posture --target <t> --vantage vm --alias <alias>   (FIRST)",
    "holyshit": "holyshit recon --domain <d> && holyshit dossier --target <t> → handoff",
    "undercroft": "undercroft run --target <t> --domain <d> --url <u> [--bundle P]",
    "kairo": "kairo forge --target <t> --expand && kairo chain --target <t> --write",
    "3am": "3AM sweep per its SKILL.md §16; absorb kairo's distributed rows first",
    "shukaku": "shukaku ingest --target <t> --finding <id> --proof <ref> && shukaku reason --target <t> && shukaku hunt --target <t> [--live U] && shukaku crown … && shukaku feed --target <t> && shukaku report --target <t>",
    "shiki": "shiki assault --target <t> --url <u> --domain <d> [--bundle P] [--parallel] [--resume] [--close]",
}


def _kw_hit(kw, goal):
    """Word-boundary keyword match. Single words match stems ('protect' hits
    'protecting'); multi-word phrases match on whitespace-separated tokens."""
    tokens = kw.split()
    parts = [r"\b" + re.escape(t) for t in tokens]
    parts[-1] += r"\w*"
    return re.search(r"\s+".join(parts), goal) is not None


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
    print("✓ SPYDERMONKEY verify: all seven family engines — ALL PASS")
    return 0


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
    return 2


if __name__ == "__main__":
    sys.exit(main())
