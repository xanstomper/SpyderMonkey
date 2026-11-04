#!/usr/bin/env python3
"""
SPYDERMONKEY — master dispatcher of the HolyShit family. stdlib-only.

Commands:
  tree                    the family + roles + chain
  route    --goal "..."   goal → the mandate sequence to load/run
  run      --target T --url U --domain D [--bundle P] [--boundary-url U2]
           [--probe-ids 1,2] [--parallel] [--resume] [--close]
                          the full pipeline (delegates to SHIKI assault)
  status   [--target T]   family meta-status (versions + engines + states)
  verify                  meta self-check: all six family engines verify

Exit codes: 0 ok · 1 gate/verify failure · 2 usage error.
"""
import argparse
import json
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
    "shiki": (SEC / "shiki/scripts/shiki.py", "The Command — conducts the whole family as one assault"),
}

ROUTES = [
    ("protect", "barbican", ["posture", "--target", "{target}", "--vantage", "vm", "--alias", "{alias}"]),
    ("opsec", "barbican", None), ("anonymous", "barbican", None), ("vantage", "barbican", None),
    ("find", "holyshit", ["recon", "--domain", "{domain}"]),
    ("recon", "holyshit", None), ("dossier", "holyshit", None), ("known", "holyshit", None),
    ("custom", "undercroft", None), ("bundle", "undercroft", None), ("logic", "undercroft", None),
    ("business", "undercroft", None), ("their code", "undercroft", None),
    ("attack", "3am", None), ("sweep", "3am", None), ("take over", "3am", None),
    ("exploit", "3am", None),
    ("arm", "kairo", None), ("forge", "kairo", None), ("vectors", "kairo", None),
    ("weapons", "kairo", None), ("chains", "kairo", None),
    ("everything", "shiki", None), ("full assault", "shiki", None),
    ("together", "shiki", None), ("one command", "shiki", None),
]


def cmd_tree(args):
    from pathlib import Path as P
    sk = P(__file__).resolve().parent.parent / "SKILL.md"
    text = sk.read_text()
    start = text.find("| # |")
    end = text.find("## The Router")
    print(text[start:end] if start >= 0 and end > start else "tree table not found — read SKILL.md")
    return 0


def cmd_route(args):
    goal = args.goal.lower()
    seq = []
    for kw, mandate, _ in ROUTES:
        if kw in goal and mandate not in seq:
            seq.append(mandate)
    if not seq or "everything" in goal or "assault" in goal or "together" in goal:
        seq = ["shiki"] if not seq or "everything" in goal or "assault" in goal else seq
        if not seq:
            seq = ["barbican", "holyshit", "undercroft", "kairo", "3am"]
    print(f"▸ goal: '{args.goal}'")
    print(f"  → load + run, in order: {' → '.join(seq)}")
    if seq == ["shiki"]:
        print("  command: shiki assault --target <t> --url <u> --domain <d> [--bundle P] [--parallel] [--resume] [--close]")
    elif "barbican" in seq:
        print("  command: barbican posture --target <t> --vantage vm --alias <alias>   (FIRST)")
    elif "holyshit" in seq:
        print("  command: holyshit recon --domain <d> && holyshit dossier --target <t> → handoff")
    elif "undercroft" in seq:
        print("  command: undercroft run --target <t> --domain <d> --url <u> [--bundle P]")
    elif "kairo" in seq:
        print("  command: kairo forge --target <t> --expand && kairo chain --target <t> --write")
    elif "3am" in seq:
        print("  command: 3AM sweep per its SKILL.md §16; absorb kairo's distributed rows first")
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
    print(f"▸ SPYDERMONKEY runs the family: shiki assault")
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
    bad = []
    self = Path(__file__).resolve()
    help_out = subprocess.run([sys.executable, str(self), "--help"],
                              capture_output=True, text=True).stdout
    for want in ("tree", "route", "run", "status", "verify", "mandate"):
        if want not in help_out:
            bad.append(f"subcommand {want}")
    mandate = Path(__file__).resolve().parent.parent / "references" / "mandate.md"
    if not mandate.exists():
        bad.append("mandate file")
    for name, (script, _) in FAMILY.items():
        r = subprocess.run([sys.executable, str(script), "verify"],
                           capture_output=True, text=True)
        if r.returncode != 0:
            bad.append(f"{name} engine")
    if bad:
        print(f"✗ SPYDERMONKEY verify FAILED: {bad}")
        return 1
    print("✓ SPYDERMONKEY verify: all six family engines — ALL PASS")
    return 0


def main():
    ap = argparse.ArgumentParser(description="SPYDERMONKEY — master dispatcher of the HolyShit family")
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("tree", help="the family + roles + chain")
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
    s = sub.add_parser("status", help="family meta-status")
    s.add_argument("--target")
    vf = sub.add_parser("verify", help="meta self-check")
    md = sub.add_parser("mandate", help="print the injectable persona contract (kimiko architecture, model-agnostic)")
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
        mfile = Path(__file__).resolve().parent.parent / "references" / "mandate.md"
        if a.file:
            print(str(mfile))
            return 0
        print(mfile.read_text())
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())