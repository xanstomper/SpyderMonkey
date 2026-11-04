#!/usr/bin/env python3
"""
SPYDERMONKEY — master dispatcher of the HolyShit family. stdlib-only.

v3.0 — THE INTELLIGENCE LAYER. The family's proven engines keep firing; the
dispatcher now owns the engagement brain around them (CyberStrike-derived,
family-native: walls as exit codes, scope authority default-deny, no-gain):

Commands:
  tree                    the family + roles + chain
  route    --goal "..."   goal → the mandate sequence to load/run
  run      --target T --url U --domain D [--bundle P] [--boundary-url U2]
           [--probe-ids 1,2] [--parallel] [--resume] [--close] [--dry-run]
                          the full pipeline (delegates to SHIKI assault)
  mission  --target T --url U --domain D [--skip-fleet] [--close]
                          v3 ONE COMMAND: scope gate → fleet → ledger triage →
                          chain detect → coverage → war report
  phases   --target T     the 13-phase methodology board (lifecycle engine)
  ledger   add|list|show|triage --target T
                          the finding ledger: scope-blocked · deduped ·
                          evidence-gated (downgrade, NEVER suppress)
  gate     --target T --url U --attack-query Q [--baseline-query Q2]
                          the 3-gate confirmation engine: baseline → attack →
                          measurable diff (+ confirm token) → CONFIRMED
  chain    detect|plan --target T
                          8 chain patterns: low findings → high-impact kill chains
  context  set|show --target T
                          session context: endpoints · roles · credentials · functions
  testers  --target T --url U [--url U2…] [--demo]
                          8 parallel sub-testers (IDOR/AUTHZ/MASSASSIGN/INJECTION/
                          AUTHN/BIZLOGIC/SSRF/FILEATTACK) over the session context
  coverage --target T     phase × deliverable matrix + ledger histogram + gaps
  report   --target T     the joint war report (findings+chains+phases+detection+pricing)
  relay    init|list|exec|remove
                          remote execution nodes (Bolt-equivalent): Ed25519 ssh pairs
  status   [--target T]   family meta-status (versions + engines + states)
  verify                  meta self-check: subcommands, mandate file, ten engines,
                          + LIVE gate proof against the built-in lab replica
  mandate  [--file]       print (or locate) the injectable persona contract
  scope    init|check|show  the scope authority (~/.redteam/scope.json) — the
                          machine-checkable estate gate every live probe honors
  doctor                  health check: engines · scope · campaigns · canon · ledger
  bench                   offline route-level benchmark (route accuracy)
  arsenal  list|plan|run  scope-gated execution layer (13 tool wrappers)
  fleet    --goal G ...   PARALLEL multi-agent dispatch: one agent per mandate
  + bench_live.py         LIVE exploitation bench: stdlib vulnerable mini-targets
                          on localhost, real engines scored (sub-task completion)
  + mcp_server.py         the family as 18 MCP tools (stdio JSON-RPC) — any MCP
                          client (Claude Desktop/Cursor) drives the family
  + skilltree.py          per-technique skill files generated from the real canon,
                          WSTG/CWE/ATT&CK-bound (references/skills/ + index)

Live-fire rule (v3): a live HTTP engine (gate/testers) fires at 127.0.0.1/localhost
freely (the lab — dojo replicas, CI). ANY other host requires a scope authority
containing it: no authority or out-of-scope → rc=1 refusal. The walls are exit codes.

Exit codes: 0 ok · 1 gate/verify/scope failure · 2 usage error.
"""
import argparse
import json
import re
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
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
    "kage": (SEC / "kage/scripts/kage.py", "The Mirror — a detection rule for every confirmed attack (the purple layer)"),
    "dojo": (SEC / "dojo/scripts/dojo.py", "The Range — buildable vulnerable replicas of every technique class (where the family trains)"),
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
    ("detect", "kage"), ("mirror", "kage"), ("detection", "kage"), ("purple", "kage"), ("defend", "kage"), ("sigma", "kage"),
    ("train", "dojo"), ("range", "dojo"), ("replica", "dojo"), ("lab", "dojo"), ("lesson", "dojo"),
    ("everything", "shiki"), ("full assault", "shiki"), ("together", "shiki"), ("one command", "shiki"),
    ("confirm", "spy"), ("baseline", "spy"), ("diff", "spy"), ("ledger", "spy"), ("coverage", "spy"),
    ("phase", "spy"), ("report", "spy"), ("remote", "spy"), ("relay", "spy"), ("node", "spy"),
]

RELAY = ["barbican", "holyshit", "undercroft", "kairo", "3am", "kaisha", "shukaku", "kage", "dojo"]

# stem-matching exceptions: noun forms that must NOT trigger the verb keyword
STEM_BLOCK = {"find": ("ings", "ing", "er")}


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
    "kage": "kage mirror --target <t> && kage validate --target <t> && kage report --target <t>",
    "arsenal": "arsenal list && arsenal plan --target <t> && arsenal run --target <t>",
    "dojo": "dojo catalog && dojo build --class <C> --port <p>",
    "spy": "spydermonkey gate run … | testers run … | ledger triage --target <t> | mission …",
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
        ld = _camp(args.target) / "ledger.jsonl"
        if ld.exists():
            rows = [l for l in ld.read_text().splitlines() if l.strip()]
            conf = sum(1 for l in rows if '"CONFIRMED"' in l)
            print(f"  ledger: {len(rows)} finding(s) · {conf} confirmed")
    return 0


def cmd_verify(args):
    missing, broken = [], []
    self = Path(__file__).resolve()
    help_out = subprocess.run([sys.executable, str(self), "--help"],
                              capture_output=True, text=True).stdout
    bad = []
    for want in ("tree", "route", "run", "status", "verify", "mandate", "scope",
                 "doctor", "bench", "fleet", "arsenal", "mission", "phases",
                 "ledger", "gate", "chain", "context", "testers", "coverage",
                 "report", "relay"):
        if want not in help_out:
            bad.append(f"subcommand {want}")
    mandate = self.parent.parent / "references" / "mandate.md"
    if not mandate.exists():
        bad.append("mandate file")
    if len(PHASES) != 13:
        bad.append("phases != 13")
    if len(CHAIN_PATTERNS) < 8:
        bad.append("chain patterns")
    if len(TESTERS) != 8:
        bad.append("testers != 8")
    for name, (script, _) in FAMILY.items():
        if not script.exists():
            missing.append(name)
            continue
        r = subprocess.run([sys.executable, str(script), "verify"],
                           capture_output=True, text=True)
        if r.returncode != 0:
            broken.append(f"{name} engine")
    # the LIVE gate proof: the 3-gate engine vs the built-in lab replica
    live_ok, live_line = _verify_gate_live()
    if not live_ok:
        bad.append("live gate proof")
    if bad or broken or missing:
        print(f"✗ SPYDERMONKEY verify FAILED: {bad + broken}")
        if missing:
            print(f"  ⚠ engines not installed: {', '.join(missing)}")
            print("    the dispatcher needs the family on disk — clone each repo into")
            print("    ~/.hermes/skills/security/<name>/ (see README → Quickstart)")
        return 1
    print(f"✓ SPYDERMONKEY verify: all ten family engines — ALL PASS ({live_line})")
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


def _is_lab(value):
    """localhost-family targets are always lab-legal (dojo replicas, CI)."""
    from urllib.parse import urlparse
    v = value.strip().lower()
    host = urlparse(v).hostname or v if "://" in v else v
    return host in ("127.0.0.1", "localhost", "::1", "0.0.0.0")


def _scope_gate(value, quiet=False):
    """The live-fire gate. Lab hosts: always allowed. Everything else: a scope
    authority containing the host is REQUIRED — default-deny. Returns bool."""
    if _is_lab(value):
        return True
    scope = _load_scope()
    if scope is None:
        if not quiet:
            print(f"✗ LIVE-FIRE REFUSED — {value}: no scope authority", file=sys.stderr)
            print("  init one: spydermonkey scope init --engagement E --in-scope <host,CIDR>", file=sys.stderr)
        return False
    if _scope_match(scope, value):
        return True
    if not quiet:
        print(f"✗ LIVE-FIRE REFUSED — {value} is not in the declared estate", file=sys.stderr)
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
            if _is_lab(args.value):
                print(f"✓ LAB TARGET — {args.value} (localhost is always lab-legal)")
                return 0
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
        lrows = sum(1 for d in camp.iterdir()
                    if (d / "ledger.jsonl").exists()
                    for l in (d / "ledger.jsonl").read_text().splitlines() if l.strip())
        print(f"  ledger:  {lrows} finding row(s) across campaigns")
    lv = Path.home() / ".redteam" / "learned-vectors.jsonl"
    if lv.exists():
        rows = [l for l in lv.read_text().splitlines() if l.strip()]
        print(f"  canon:   {len(rows)} learned-vector row(s) (3AM promote-ready)")
    rd = Path.home() / ".redteam" / "relays"
    if rd.exists():
        relays = list(rd.glob("*/relay.json"))
        print(f"  relays:  {len(relays)} remote node(s)")
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
    ("detect the intrusion and write the rule", "kage"),
    ("train on a vulnerable replica in the lab", "dojo"),
    ("run the 3-gate confirm on the probe", "spy"),
    ("triage the finding ledger", "spy"),
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
    print("  (route-level only — see bench_live.py for the exploitation-level bench)")
    return 0 if pct >= 90 else 1


def cmd_mandate(args):
    mfile = Path(__file__).resolve().parent.parent / "references" / "mandate.md"
    if args.file:
        print(str(mfile))
        return 0
    print(mfile.read_text())
    return 0


# ── v1.4.0 the agent fleet: one agent per mandate, dispatched in PARALLEL ─────

FLEET_BRIEFS = {
    "barbican":   ("THE SHIELD",   lambda a: ["assess", "--target", a["target"]]),
    "holyshit":   ("THE FINDER",   lambda a: ["dossier", "--target", a["target"]]),
    "undercroft": ("THE DESCENT",  lambda a: ["probe"]),
    "3am":        ("THE PERFORMER", lambda a: ["verify"]),
    "kage":       ("THE MIRROR",   lambda a: ["mirror", "--target", a["target"]]),
    "dojo":       ("THE RANGE",    lambda a: ["catalog"]),
    "kairo":      ("THE SYNTH",    lambda a: ["verify"]),
    "kaisha":     ("THE LADDER",   lambda a: ["rungs", "--target", a["target"]]),
    "shukaku":    ("THE HARVESTER", lambda a: ["verify"]),
    "shiki":      ("THE COMMAND",  lambda a: ["board", "--org", a["target"]]),
}


def cmd_fleet(args):
    """PARALLEL MULTI-AGENT DISPATCH: every mandate wakes as its own agent with
    its brief, runs its capability pass concurrently, and the fleet reports."""
    seq = list(RELAY)
    for kw, mandate in ROUTES:
        if mandate in FAMILY and mandate not in seq and _kw_hit(kw, args.goal.lower()):
            seq.insert(0, mandate)          # matched mandates lead the fleet
    if args.agents:
        want = set(s.strip() for s in args.agents.split(",") if s.strip())
        seq = [m for m in seq if m in want]
    ctx = {"target": args.target, "domain": args.domain}
    results = {}

    def agent(name):
        role, argv_f = FLEET_BRIEFS[name]
        script = FAMILY[name][0]
        if not script.exists():
            results[name] = (role, f"engine missing — agent offline ({script})", 1)
            return
        out, rc = _run([sys.executable, str(script)] + argv_f(ctx))
        results[name] = (role, out, rc)

    print(f"═══ SPYDERMONKEY FLEET — {len(seq)} agent(s) dispatching in PARALLEL ═══")
    print(f"  goal: '{args.goal}' · target: {args.target} · domain: {args.domain}")
    threads = [threading.Thread(target=agent, args=(m,)) for m in seq]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    up = 0
    for name in seq:
        role, out, rc = results[name]
        ok = rc == 0
        up += ok
        lines = [l for l in out.splitlines() if l.strip()][:8]
        print(f"\n  ┌─ AGENT {name} — {role} [{'✓' if ok else '✗'}]")
        for l in lines:
            print(f"  │ {l[:100]}")
        print(f"  └─ ({len(out.splitlines())} lines)")
    print(f"\n═══ FLEET REPORT: {up}/{len(seq)} agent(s) up · joint goal: '{args.goal}' ═══")
    return 0 if up == len(seq) else 1


def _run(argv, timeout=60):
    try:
        r = subprocess.run(argv, capture_output=True, text=True, timeout=timeout)
        return r.stdout + r.stderr, r.returncode
    except Exception as e:
        return f"error: {e}", 1


def _exec_arsenal(a):
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "arsenal", str(Path(__file__).resolve().parent / "arsenal.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    argv = [a.action] + (["--target", a.target] if a.target else []) \
        + (["--only", a.only] if a.only else []) \
        + (["--dry-run"] if getattr(a, "dry_run", False) else []) \
        + (["--wordlist", a.wordlist] if a.wordlist else [])
    return mod.main_with(argv)


# ════════════════════════════════════════════════════════════════════════════
# v3.0 — THE INTELLIGENCE LAYER (CyberStrike-derived, family-native)
# ════════════════════════════════════════════════════════════════════════════

def _camp(c):
    p = Path.home() / ".redteam" / "campaigns" / c
    p.mkdir(parents=True, exist_ok=True)
    return p


def _load_json(p, default):
    try:
        return json.loads(Path(p).read_text())
    except Exception:
        return default


# ── 3.1 the 13-phase methodology engine ───────────────────────────────────────

PHASES = [
    {"id": "scope_analysis",         "name": "Scope Analysis & Attack Surface", "mandate": "barbican",
     "pre": [],                      "deliverable": "scope"},
    {"id": "passive_recon",          "name": "Passive Reconnaissance", "mandate": "holyshit",
     "pre": ["scope_analysis"],      "deliverable": "context"},
    {"id": "active_recon",           "name": "Active Recon & Enumeration", "mandate": "undercroft",
     "pre": ["passive_recon"],       "deliverable": "undercroft:surface"},
    {"id": "technology_profiling",   "name": "Technology Profiling", "mandate": "kaisha",
     "pre": ["active_recon"],        "deliverable": "ladder:era"},
    {"id": "authentication_testing", "name": "Authentication Testing", "mandate": "3am",
     "pre": ["technology_profiling"], "deliverable": "ledger:AUTHN"},
    {"id": "session_management",     "name": "Session Management", "mandate": "3am",
     "pre": ["authentication_testing"], "deliverable": "ledger:REPLAY"},
    {"id": "authorization_testing",  "name": "Authorization Testing", "mandate": "spy",
     "pre": ["session_management"],  "deliverable": "ledger:IDOR"},
    {"id": "input_validation",       "name": "Input Validation", "mandate": "spy",
     "pre": ["active_recon"],        "deliverable": "ledger:INJECTION"},
    {"id": "business_logic",         "name": "Business Logic", "mandate": "undercroft",
     "pre": ["active_recon"],        "deliverable": "ledger:BIZLOGIC"},
    {"id": "data_protection",        "name": "Data Protection", "mandate": "shukaku",
     "pre": ["business_logic"],      "deliverable": "ledger:HARVEST"},
    {"id": "api_security",           "name": "API Security", "mandate": "spy",
     "pre": ["active_recon"],        "deliverable": "ledger:MASSASSIGN"},
    {"id": "infrastructure",         "name": "Infrastructure", "mandate": "kaisha",
     "pre": ["active_recon"],        "deliverable": "ladder:hosts"},
    {"id": "reporting",              "name": "Reporting", "mandate": "spy",
     "pre": ["authorization_testing", "input_validation", "business_logic"],
     "deliverable": "report"},
]

SEVERITY_ORDER = {"info": 0, "low": 1, "medium": 2, "high": 3, "critical": 4}


def _phase_deliverable(target, ph):
    """Does the phase have at least ONE real deliverable? Checks the family's
    actual state files — statuses are computed, never declared."""
    d = ph["deliverable"]
    camp = _camp(target)
    if d == "scope":
        return _load_scope() is not None
    if d == "context":
        return bool(_load_json(camp / "context.json", {}).get("endpoints"))
    if d == "report":
        return any(camp.glob("*spydermonkey-report.md"))
    if d == "ladder:era":
        l = _load_json(camp / "ladder-state.json", {})
        return any(h.get("era") for h in l.get("hosts", []))
    if d == "ladder:hosts":
        l = _load_json(camp / "ladder-state.json", {})
        return bool(l.get("hosts"))
    if d.startswith("ledger:"):
        want = d.split(":", 1)[1]
        ld = camp / "ledger.jsonl"
        if not ld.exists():
            return False
        for line in ld.read_text().splitlines():
            if not line.strip():
                continue
            try:
                e = json.loads(line)
            except Exception:
                continue
            if want in (e.get("cls") or "") or want in (e.get("title", "").upper()):
                return True
        return False
    if ":" in d:
        fname, key = d.split(":", 1)
        st = _load_json(camp / fname, {})
        return bool(st.get(key))
    return False


def cmd_phases(args):
    camp = _camp(args.target)
    board = _load_json(camp / "phases-state.json", {})
    if args.set_phase and args.phase_status:
        board[args.set_phase] = args.phase_status
        (camp / "phases-state.json").write_text(json.dumps(board, indent= 2) + "\n")
        print(f"▸ phase {args.set_phase} → {args.phase_status}")
        return 0
    done = {p["id"]: _phase_deliverable(args.target, p) for p in PHASES}
    print(f"═══ SPYDERMONKEY PHASES — engagement '{args.target}' (13-phase methodology) ═══")
    n_done = 0
    for p in PHASES:
        manual = board.get(p["id"])
        if manual in ("completed", "blocked", "in_progress", "not_started"):
            status = manual
        else:
            ok = all(done[q] for q in p["pre"])
            status = "completed" if done[p["id"]] else ("in_progress" if ok else "blocked")
        mark = {"completed": "✓", "in_progress": "▸", "blocked": "·", "not_started": "·"}[status]
        n_done += status == "completed"
        print(f"  {mark} {p['id']:22s} [{status:11s}] {p['mandate']:9s} — {p['name']}")
    nxt = next((p for p in PHASES
                if (board.get(p["id"]) or ("completed" if _phase_deliverable(args.target, p) else "in_progress"))
                != "completed"), None)
    print(f"═══ {n_done}/13 phases complete ═══")
    if nxt:
        print(f"  next: {nxt['id']} — run the {nxt['mandate']} mandate"
              + (f" ({CMDS.get(nxt['mandate'], '')[:80]})" if CMDS.get(nxt["mandate"]) else ""))
    return 0


# ── 3.2 the finding ledger (scope-blocked · deduped · evidence-gated) ─────────

_STOP = set("the a an of on in at to for with and or is are be been it its this that".split())


def _norm_title(t):
    words = re.sub(r"[^a-z0-9 ]", " ", t.lower()).split()
    return " ".join(w for w in words if w not in _STOP)[:6]


def _dedupe_key(cls, asset, title):
    return f"{cls}|{asset}|{_norm_title(title)}"


def _ledger_load(c):
    ld = _camp(c) / "ledger.jsonl"
    rows = []
    if ld.exists():
        for line in ld.read_text().splitlines():
            if line.strip():
                try:
                    rows.append(json.loads(line))
                except Exception:
                    pass
    return rows


def _ledger_append(c, entry):
    ld = _camp(c) / "ledger.jsonl"
    with ld.open("a") as f:
        f.write(json.dumps(entry) + "\n")


def _evidence_gate(proof):
    """CyberStrike's evidence rule: a finding needs (1) baseline request/response,
    (2) attack request/response, (3) a one-sentence diff. Anything else is NOT
    suppressed — it is DOWNGRADED to hypothesis confidence 0.4."""
    p = (proof or "").lower()
    has = lambda m: m in p
    if has("baseline:") and has("attack:") and (has("diff:") or has("diff ")):
        return "confirmed", 0.95, None
    if has("diff:") or has("diff "):
        return "hypothesis", 0.4, "evidence incomplete: need baseline: + attack: + diff:"
    return "hypothesis", 0.4, "no 3-gate evidence: need baseline: + attack: + diff:"


def _impact_to_severity(title, proof):
    """Triager check material: does the claimed severity match the impact words?"""
    text = f"{title} {proof}".lower()
    if re.search(r"\b(rce|remote code|command exec|full.?bypass|account takeover|mass data|sql inject.*data)\b", text):
        return "critical"
    if re.search(r"\b(user|email|token|key|password|secret|admin|session|cookie|api.?key|credential)\b", text):
        return "high"
    if re.search(r"\b(version|fingerprint|header|stack trace|error message|debug|info disclosure)\b", text):
        return "info"
    return "medium"


def cmd_ledger(args):
    camp = _camp(args.target)
    if args.action == "add":
        if not _scope_gate(args.asset, quiet=True):
            # the ledger refuses to REGISTER findings about out-of-scope assets
            scope = _load_scope()
            if scope is not None and not _scope_match(scope, args.asset):
                print(f"✗ LEDGER REFUSED — {args.asset} is out of the declared estate", file=sys.stderr)
                return 1
        status, conf, reason = _evidence_gate(args.proof)
        if status != "confirmed" and args.confirmed:
            status, conf = "confirmed", 0.95
            reason = None
        rows = _ledger_load(args.target)
        key = _dedupe_key(args.cls, args.asset, args.title)
        dup = next((r for r in rows if r.get("dedupe") == key), None)
        if dup:
            dup.setdefault("evidence", []).append({"proof": args.proof, "at": _now()})
            if status == "confirmed" and dup["status"] != "CONFIRMED":
                dup["status"], dup["confidence"] = "CONFIRMED", conf
            _ledger_rewrite(args.target, rows)
            print(f"▸ DUPLICATE — matched {dup['id']} (same class+asset+title): evidence"
                  f" attached in place, no new record ({len(dup['evidence'])} evidence item(s))")
            return 0
        eid = f"SPY-{len(rows) + 1:03d}"
        entry = {"id": eid, "title": args.title, "cls": args.cls, "asset": args.asset,
                 "severity": args.severity, "status": status.upper(),
                 "confidence": conf, "proof": args.proof, "cwe": args.cwe or "",
                 "dedupe": key, "evidence": [{"proof": args.proof, "at": _now()}],
                 "at": _now()}
        _ledger_append(args.target, entry)
        line = f"▸ {eid} [{status.upper()} {args.severity} conf={conf:.2f}] {args.title[:56]} @ {args.asset[:40]}"
        print(line)
        if reason:
            print(f"  ⚠ downgraded (never suppressed): {reason}")
        return 0
    if args.action == "list":
        rows = _ledger_load(args.target)
        if not rows:
            print("· ledger empty — ledger add --target <t> --title ... --proof 'baseline:… attack:… diff:…'")
            return 0
        print(f"═══ FINDING LEDGER — {args.target} ({len(rows)} finding(s)) ═══")
        for r in rows:
            print(f"  {r['id']} [{r['status']:9s} {r['severity']:8s} conf={r['confidence']:.2f}]"
                  f" {r['title'][:52]} @ {r['asset'][:44]} ({r['cls']})")
        return 0
    if args.action == "show":
        rows = _ledger_load(args.target)
        r = next((x for x in rows if x["id"] == args.id), None)
        if not r:
            print(f"✗ no finding {args.id}", file=sys.stderr)
            return 2
        print(json.dumps(r, indent=2))
        return 0
    if args.action == "triage":
        rows = _ledger_load(args.target)
        if not rows:
            print("· ledger empty — nothing to triage")
            return 0
        scope = _load_scope()
        blocking, warnings = [], []
        print(f"═══ LEDGER TRIAGE — {args.target} ═══")
        for r in rows:
            vs = []
            want = _impact_to_severity(r["title"], r["proof"])
            if SEVERITY_ORDER.get(r["severity"], 2) < SEVERITY_ORDER[want] - 1:
                vs.append(("severity-impact", "warning",
                           f"claims {r['severity']} but impact words say {want}"))
            if r["status"] != "CONFIRMED" and r["confidence"] < 0.9 and "baseline" not in r["proof"].lower():
                vs.append(("evidence", "warning", "no reproducible 3-gate evidence"))
            if scope is not None and not _is_lab(r["asset"]) and not _scope_match(scope, r["asset"]):
                vs.append(("scope", "blocking", f"asset {r['asset']} out of the declared estate"))
            dups = [x["id"] for x in rows if x["id"] != r["id"]
                    and _dedupe_key(x["cls"], x["asset"], x["title"]) == r["dedupe"]]
            if dups:
                vs.append(("duplicate", "warning", f"same key as {','.join(dups)}"))
            for g, sev, msg in vs:
                (blocking if sev == "blocking" else warnings).append(f"{r['id']} {g}: {msg}")
            mark = "✗" if any(g == "blocking" for g, _, _ in vs) else ("⚠" if vs else "✓")
            print(f"  {mark} {r['id']} {r['title'][:46]} — "
                  + ("; ".join(f"{g}:{m[:44]}" for g, _, m in vs) if vs else "clean"))
        print(f"═══ {len(rows)} finding(s): {len(blocking)} blocking · {len(warnings)} warning(s) ═══")
        for b in blocking:
            print(f"  ✗ BLOCKING {b}")
        return 1 if blocking else 0
    return 2


def _ledger_rewrite(c, rows):
    ld = _camp(c) / "ledger.jsonl"
    ld.write_text("\n".join(json.dumps(r) for r in rows) + "\n")


def _now():
    return datetime.now(timezone.utc).isoformat()


# ── 3.3 the 3-gate confirmation engine (baseline → attack → diff) ─────────────

def _http(url, method="GET", data=None, headers=None, timeout=6):
    """stdlib live request. Returns dict(status, body, elapsed) — never raises."""
    t0 = time.time()
    req = urllib.request.Request(url, method=method,
                                 data=data.encode() if data else None,
                                 headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return {"status": r.status, "body": r.read().decode("utf-8", "replace"),
                    "elapsed": round(time.time() - t0, 3)}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "body": e.read().decode("utf-8", "replace"),
                "elapsed": round(time.time() - t0, 3)}
    except Exception as e:
        return {"status": 0, "body": f"__error__ {type(e).__name__}",
                "elapsed": round(time.time() - t0, 3)}


def cmd_gate(args):
    if args.prove:
        rows = _ledger_load(args.target)
        r = next((x for x in rows if x["id"] == args.prove), None)
        if not r:
            print(f"✗ no finding {args.prove}", file=sys.stderr)
            return 2
        print(f"═══ 3-GATE REPLAY — {r['id']} {r['title'][:50]} ═══")
        for i, ev in enumerate(r.get("evidence", []), 1):
            print(f"  evidence {i}: {ev['proof'][:160]} ({ev['at']})")
        print(f"  status {r['status']} · confidence {r['confidence']}")
        return 0
    if not _scope_gate(args.url):
        return 1
    from urllib.parse import urlencode, urlsplit, urlunsplit, parse_qsl
    sp = urlsplit(args.url)
    base_q = parse_qsl(sp.query, keep_blank_values=True)
    base_path = sp.path or "/"
    url_b = urlunsplit((sp.scheme, sp.netloc, base_path,
                        urlencode(parse_qsl(args.baseline_query, keep_blank_values=True)
                                  if args.baseline_query else base_q), ""))
    # attack request: the attack query REPLACES the baseline query by default
    # (--append-query keeps the baseline params and adds the attack params)
    atk_q = parse_qsl(args.attack_query, keep_blank_values=True)
    if args.append_query:
        atk_q = (parse_qsl(args.baseline_query, keep_blank_values=True)
                 if args.baseline_query else base_q) + atk_q
    url_a = urlunsplit((sp.scheme, sp.netloc, base_path, urlencode(atk_q), ""))
    method = args.method.upper()
    hb = dict(h.split(":", 1) for h in args.header) if args.header else {}
    print(f"═══ 3-GATE CONFIRMATION — {method} {sp.netloc}{base_path} ═══")
    g1 = _http(url_b, method, data=args.data, headers=hb)
    print(f"  ▸ G1 baseline  {url_b[:70]} → {g1['status']} len={len(g1['body'])} {g1['elapsed']}s")
    g2 = _http(url_a, method, data=(args.data + "&" + args.attack_query if args.data and method == "POST"
                                    else args.data), headers=hb)
    print(f"  ▸ G2 attack    {url_a[:70]} → {g2['status']} len={len(g2['body'])} {g2['elapsed']}s")
    diff = (g1["status"], len(g1["body"]), g1["body"]) != (g2["status"], len(g2["body"]), g2["body"])
    what = []
    if g1["status"] != g2["status"]:
        what.append(f"status {g1['status']}→{g2['status']}")
    if len(g1["body"]) != len(g2["body"]):
        what.append(f"length {len(g1['body'])}→{len(g2['body'])}")
    if g1["body"] != g2["body"]:
        what.append("body differs")
    g3 = diff
    token_hit = None
    if args.confirm:
        token_hit = args.confirm.lower() in g2["body"].lower()
        g3 = diff and token_hit
    print(f"  ▸ G3 diff      {'YES' if diff else 'NO'} ({'; '.join(what) or 'identical response'})"
          + (f" · confirm-token {'✓ present' if token_hit else '✗ ABSENT'}" if args.confirm else ""))
    title = args.title or f"{args.cls.lower()} differential on {base_path}"
    if g3:
        proof = (f"baseline: {url_b[:100]} → {g1['status']} len={len(g1['body'])}; "
                 f"attack: {url_a[:100]} → {g2['status']} len={len(g2['body'])}; "
                 f"diff: {'; '.join(what)}")
        rc = _cmd_ledger_internal(args.target, title, args.cls, args.url, args.severity,
                                  proof, args.cwe)
        print("  ✓ CONFIRMED — measurable, reproducible diff; registered in the ledger")
        return 0 if rc == 0 else rc
    if diff:
        print("  ⚠ HYPOTHESIS — measurable diff but the confirm token is absent;"
              " registered at confidence 0.4 (downgraded, never suppressed)")
        proof = (f"baseline: {g1['status']} len={len(g1['body'])}; attack: {g2['status']}"
                 f" len={len(g2['body'])}; diff: {'; '.join(what)} — confirm token unverified")
        _cmd_ledger_internal(args.target, title, args.cls, args.url, "info", proof, args.cwe)
        return 0
    print("  ✗ DISPROVEN — responses identical; nothing registered (no speculation)")
    return 0


def _cmd_ledger_internal(target, title, cls, asset, severity, proof, cwe=None):
    """Register a finding through the ledger's own gates (used by gate/testers)."""
    rows = _ledger_load(target)
    status, conf, reason = _evidence_gate(proof)
    key = _dedupe_key(cls, asset, title)
    dup = next((r for r in rows if r.get("dedupe") == key), None)
    if dup:
        dup.setdefault("evidence", []).append({"proof": proof, "at": _now()})
        if status == "confirmed" and dup["status"] != "CONFIRMED":
            dup["status"], dup["confidence"] = "CONFIRMED", conf
        _ledger_rewrite(target, rows)
        print(f"  ▸ ledger: evidence attached to {dup['id']} (dedupe)")
        return 0
    eid = f"SPY-{len(rows) + 1:03d}"
    _ledger_append(target, {"id": eid, "title": title, "cls": cls, "asset": asset,
                            "severity": severity, "status": status.upper(),
                            "confidence": conf, "proof": proof, "cwe": cwe or "",
                            "dedupe": key, "evidence": [{"proof": proof, "at": _now()}],
                            "at": _now()})
    print(f"  ▸ ledger: {eid} [{status.upper()} {severity} conf={conf:.2f}] {title[:52]}")
    if reason:
        print(f"    ⚠ downgraded (never suppressed): {reason}")
    return 0


# ── 3.4 the chain detection engine (8 patterns) ───────────────────────────────

CHAIN_PATTERNS = [
    {"name": "credential_endpoint",
     "pair": (r"\b(backup|dump|env|git|secret|cred|harvest)\b", r"\b(admin|login|auth|token|session)\b"),
     "impact": "exposed credential/backup material → account takeover on the same estate",
     "plan": "validate the exposed material against the live auth surface (one login attempt, reversed); shukaku crowns the class; kaisha ladders with it",
     "severity": "critical"},
    {"name": "info_disclosure_ssrf",
     "pair": (r"\b(info|debug|stack|error|version|fingerprint)\b", r"\b(ssrf|internal|url fetch|metadata)\b"),
     "impact": "info disclosure names internal hosts → SSRF pivots to them",
     "plan": "point the disclosed-internal host into the SSRF-prone param (GET-only, no-gain); crown the pivot vantage",
     "severity": "high"},
    {"name": "redirect_oauth",
     "pair": (r"\b(redirect|open.?redirect|302)\b", r"\b(oauth|sso|saml|token|callback)\b"),
     "impact": "open redirect on an oauth flow → authorization-code interception",
     "plan": "replay the redirect with an attacker-controlled redirect_uri against a throwaway session (documented-PoC class); kage rule on the callback",
     "severity": "critical"},
    {"name": "idor_data_leak",
     "pair": (r"\b(idor|foreign|scope.?id|org.?id|object.?id)\b", r"\b(data|orders|profile|email|record)\b"),
     "impact": "object-id trust + enumerable data → cross-tenant mass read",
     "plan": "prove read of ONE foreign object id (already-confirmed class, count only); shukaku prices the exposed table",
     "severity": "high"},
    {"name": "xss_csrf",
     "pair": (r"\b(xss|reflected|svg|markup)\b", r"\b(csrf|state change|transfer|payment|invite)\b"),
     "impact": "reflected markup + no CSRF proof → scripted state change on a victim session",
     "plan": "validate the state-changing endpoint accepts a cross-site form POST on a lab account (validation-only)",
     "severity": "high"},
    {"name": "ssti_rce",
     "pair": (r"\b(ssti|template|jinja|twig|velocity)\b", r"\b(rce|code exec|command)\b"),
     "impact": "template injection reaching code evaluation → full server control",
     "plan": "arithmetic-marker probe only ({{7*7}}→49); NEVER a payload chain; undercroft owns the boundary map",
     "severity": "critical"},
    {"name": "race_business",
     "pair": (r"\b(race|replay|idempoten|duplicate|double)\b", r"\b(payment|coupon|balance|withdraw|transfer|credit)\b"),
     "impact": "no idempotency on a money path → double-spend class",
     "plan": "two identical logical requests N=2 (validation-only, zero-balance lab account); kage rule: count_by hash window",
     "severity": "critical"},
    {"name": "custom",
     "pair": None, "impact": "operator-defined pairing — registered via ledger classes",
     "plan": "declare the pair with chain plan --pattern custom --requires 'CLS-A+CLS-B'",
     "severity": "medium"},
]


def _confirmed_rows(target):
    """Every CONFIRMED signal in the campaign: ledger rows + family state rows."""
    camp = _camp(target)
    out = [(r["title"], r["cls"], r["asset"]) for r in _ledger_load(target)
           if r.get("status") == "CONFIRMED"]
    try:
        u = _load_json(camp / "undercroft-state.json", {})
        for s in u.get("surface", []) + u.get("logic", []):
            if s.get("status") == "CONFIRMED":
                out.append((s.get("endpoint") or s.get("seam") or "?", "UNDERCROFT",
                            s.get("endpoint") or s.get("seam") or "?"))
    except Exception:
        pass
    try:
        h = _load_json(camp / "harvest-state.json", {})
        for cr in h.get("crown", []):
            out.append((f"{cr.get('class')} harvested", cr.get("class", "HARVEST"),
                        cr.get("asset", "?")))
    except Exception:
        pass
    return out


def _origin(asset):
    from urllib.parse import urlsplit
    if "://" not in (asset or ""):
        return (asset or "?").lower()
    sp = urlsplit(asset)
    return f"{sp.scheme}://{sp.netloc}".lower()


def cmd_chain(args):
    camp = _camp(args.target)
    if args.action == "plan":
        st = _load_json(camp / "chain-state.json", {})
        ch = next((c for c in st.get("chains", []) if c["id"] == args.chain_id), None)
        if not ch:
            print(f"✗ no chain {args.chain_id}", file=sys.stderr)
            return 2
        print(f"═══ CHAIN PLAN — {ch['id']} [{ch['pattern']}] severity {ch['severity']} ═══")
        print(f"  entries:   {', '.join(ch['entry_ids'])}")
        print(f"  impact:    {ch['impact']}")
        print(f"  plan:      {ch['plan']}")
        print(f"  confidence {ch['confidence']:.2f} · status {ch['status']}")
        return 0
    rows = _confirmed_rows(args.target)
    if len(rows) < 2:
        print("· fewer than 2 confirmed signals — chains need findings; gate/testers/shiki first")
        return 0
    chains = []
    n = 0
    seen_pairs = set()
    print(f"═══ CHAIN DETECTION — {args.target} ({len(rows)} confirmed signal(s)) ═══")
    for pat in CHAIN_PATTERNS:
        if pat["pair"] is None:
            continue
        a_re, b_re = pat["pair"]
        hits_a = [r for r in rows if re.search(a_re, f"{r[0]} {r[1]} {r[2]}".lower())]
        hits_b = [r for r in rows if re.search(b_re, f"{r[0]} {r[1]} {r[2]}".lower())]
        for a in hits_a:
            for b in hits_b:
                if a is b:
                    continue
                same_asset = _origin(a[2]) == _origin(b[2]) or a[2] == "?" or b[2] == "?"
                if not same_asset:
                    continue
                pkey = (pat["name"], tuple(sorted((a[0][:40], b[0][:40]))))
                if pkey in seen_pairs:
                    continue
                seen_pairs.add(pkey)
                n += 1
                cid = f"CH-{n:03d}"
                conf = 0.55 + 0.1 * min(2, len(hits_a) + len(hits_b) - 2)
                chains.append({"id": cid, "pattern": pat["name"], "entry_ids": [a[0][:40], b[0][:40]],
                               "assets": [a[2]], "impact": pat["impact"], "plan": pat["plan"],
                               "severity": pat["severity"], "confidence": round(conf, 2),
                               "status": "detected", "at": _now()})
                print(f"  ▸ {cid} [{pat['name']}] {a[0][:34]} + {b[0][:34]}"
                      f" → {pat['severity']} (conf {conf:.2f})")
    if not chains:
        print("  · no chain patterns matched the confirmed signals")
    st = {"campaign": args.target, "chains": chains, "at": _now()}
    (camp / "chain-state.json").write_text(json.dumps(st, indent=2) + "\n")
    print(f"═══ {len(chains)} chain candidate(s) — chain plan --id CH-XXX for the testing plan ═══")
    return 0


# ── 3.5 the session context (endpoints · roles · credentials · functions) ─────

def cmd_context(args):
    camp = _camp(args.target)
    st = _load_json(camp / "context.json", {"endpoints": [], "roles": [],
                                            "credentials": [], "functions": []})
    for k in ("endpoints", "roles", "credentials", "functions"):
        st.setdefault(k, [])
    if args.action == "set":
        kind = args.kind.lower()
        if kind not in st:
            print(f"✗ kind must be one of: {', '.join(st)}", file=sys.stderr)
            return 2
        if args.value not in st[kind]:
            st[kind].append(args.value)
            (camp / "context.json").write_text(json.dumps(st, indent=2) + "\n")
            print(f"▸ context[{kind}] += {args.value[:80]}")
        else:
            print("· already in context (dedupe)")
        return 0
    print(f"═══ SESSION CONTEXT — {args.target} ═══")
    for k, v in st.items():
        print(f"  {k} ({len(v)}):")
        for x in v[:12]:
            print(f"    · {x[:100]}")
    if not any(st.values()):
        print("  (empty — context set --kind endpoint --value '/api/orders?id=1')")
    return 0


# ── 3.6 the 8 parallel sub-testers ────────────────────────────────────────────

def _t_requests_removed():  # removed — differential requests are built in run_tester
    pass


TESTERS = [
    {"name": "IDOR", "cls": "IDOR",
     "params": ("id", "org_id", "user_id", "account_id", "order_id", "doc_id"),
     "attacks": lambda v: [f"{v}+1", "foreign"] if v else [],
     "logic": "object identifier trusted from the request — swap it, diff the body"},
    {"name": "AUTHZ", "cls": "AUTHZ",
     "params": ("role", "admin", "is_admin", "level"),
     "attacks": lambda v: ["admin", "1", "0"] if v else [],
     "logic": "role/level param trusted from input — flip it, diff the body"},
    {"name": "MASSASSIGN", "cls": "MASSASSIGN",
     "params": ("email", "name", "price", "qty", "amount"),
     "attacks": lambda v: [v] if v else [],
     "extra": "&role=admin&is_admin=1&price=0&balance=999999",
     "logic": "unexpected writable fields accepted in the request body (POST only)"},
    {"name": "INJECTION", "cls": "INJECTION",
     "params": ("q", "search", "name", "filter", "sort", "msg", "comment"),
     "attacks": lambda v: [f"{v}'", "{{7*7}}", "${7*7}"] if v else [],
     "signatures": ("sql", "syntax error", "odbc", "mysql", "sqlite", "49"),
     "logic": "input reaches an interpreter — quote/markers reflected or evaluated"},
    {"name": "AUTHN", "cls": "AUTHN",
     "params": ("token", "otp", "code", "password", "nonce"),
     "attacks": lambda v: ["", "null", "0"] if v else [],
     "logic": "credential param accepted empty/forged — auth bypass class"},
    {"name": "BIZLOGIC", "cls": "BIZLOGIC",
     "params": ("qty", "amount", "price", "count", "discount", "qty"),
     "attacks": lambda v: ["-1", "0", "99999999"] if v else [],
     "logic": "quantity/amount accepted out of business range — negative/overflow class"},
    {"name": "SSRF", "cls": "SSRF",
     "params": ("url", "uri", "fetch", "target", "src", "redirect", "next"),
     "attacks": lambda v: ["http://127.0.0.1:9/", "http://169.254.169.254/latest/meta-data/"] if v else [],
     "logic": "user-controlled URL fetched server-side — internal/metadata reach"},
    {"name": "FILEATTACK", "cls": "TRAVERSAL",
     "params": ("path", "file", "page", "template", "include", "lang"),
     "attacks": lambda v: ["../../etc/passwd", "....//etc/passwd"] if v else [],
     "signatures": ("root:x:0:0", "root:*:0:0", "daemon:"),
     "logic": "path param never normalized — traversal escapes the web root"},
]


def _demo_replica():
    """A lab-bound vulnerable replica (like dojo's): the 8 testers have something
    REAL to strike with zero setup. 127.0.0.1 only, self-terminating."""
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
    state = {"replay_hits": 0}

    def _qs(qs):
        from urllib.parse import unquote_plus
        out = {}
        for x in qs.split("&"):
            if x:
                k, _, v = x.partition("=")
                out[k] = unquote_plus(v)
        return out

    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _send(self, code, body, ctype="application/json"):
            b = body.encode()
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)

        def do_GET(self):
            p, _, qs = self.path.partition("?")
            q = _qs(qs)
            if p == "/api/orders":
                org = q.get("org_id", "acme")
                self._send(200, json.dumps({"org": org, "orders": [1, 2, 3]}))
            elif p == "/api/profile":
                uid = q.get("user_id", "1001")
                self._send(200, json.dumps({"user_id": uid, "email": f"user{uid}@lab",
                                            "role": "user"}))
            elif p == "/search":
                self._send(200, f"results for {q.get('q', '')}", "text/html")
            elif p == "/fetch":
                u = q.get("url", "")
                if u.startswith("http://127.0.0.1:9/"):
                    self._send(200, json.dumps({"fetched": "INTERNAL-BANNER-7f3a"}))
                else:
                    self._send(200, json.dumps({"fetched": "denied"}))
            elif p == "/file":
                if "../" in q.get("path", ""):
                    self._send(200, "root:x:0:0:root:/root:/bin/bash\n", "text/plain")
                else:
                    self._send(404, "nope", "text/plain")
            elif p == "/api/token":
                if not q.get("token"):
                    self._send(200, json.dumps({"authenticated": True, "bypass": True}))
                else:
                    self._send(200, json.dumps({"authenticated": q["token"] == "known"}))
            elif p == "/api/webhook":
                state["replay_hits"] += 1
                self._send(200, json.dumps({"accepted": True, "effects": state["replay_hits"]}))
            elif p == "/api/coupon":
                try:
                    v = int(q.get("amount", "0"))
                except ValueError:
                    v = 0
                self._send(200, json.dumps({"discount": v, "applied": v != 0}))
            elif p == "/role":
                self._send(200, json.dumps({"role": q.get("role", "user"), "menu": "full" if q.get("role") == "admin" else "basic"}))
            else:
                self._send(404, "not found", "text/plain")

        def do_POST(self):
            ln = int(self.headers.get("Content-Length") or 0)
            body = self.rfile.read(ln).decode("utf-8", "replace")
            if self.path == "/api/user":
                fields = _qs(body)
                fields.setdefault("role", "user")
                self._send(200, json.dumps({"created": True, "fields": fields}))
            else:
                self._send(404, "not found", "text/plain")

    srv = ThreadingHTTPServer(("127.0.0.1", 0), H)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{port}"


def cmd_testers(args):
    if not args.demo and not args.url:
        print("✗ testers need --url U (repeatable; declared targets) or --demo (lab replica)",
              file=sys.stderr)
        return 2
    if args.demo:
        srv, base = _demo_replica()
        args.url = [base + "/api/orders?org_id=acme",
                    base + "/search?q=hello",
                    base + "/file?path=etc",
                    base + "/fetch?url=http://example.com",
                    base + "/api/token?token=abc",
                    base + "/api/coupon?amount=5",
                    base + "/role?role=user",
                    base + "/api/user?name=bob&email=bob@lab"]
        print("▸ demo mode: built-in lab replica serving (self-terminating at exit)")
    else:
        srv = None
    urls = list(args.url)
    for u in urls:
        if not _scope_gate(u):
            if srv:
                srv.shutdown()
            return 1
    camp = _camp(args.target)
    ctx = _load_json(camp / "context.json", {})
    endpoints = ctx.get("endpoints", [])
    if endpoints and not args.demo:
        urls = [u if "://" in u else args.url[0].rstrip("/") + u for u in endpoints] or urls
    results = {}
    print(f"═══ SPYDERMONKEY TESTERS — 8 sub-testers in PARALLEL over {len(urls)} url(s) ═══")

    def run_tester(t):
        from urllib.parse import urlsplit, parse_qsl, urlencode, urlunsplit
        hits = []
        for u in urls:
            sp = urlsplit(u)
            params = dict(parse_qsl(sp.query, keep_blank_values=True))
            base = urlunsplit((sp.scheme, sp.netloc, sp.path, "", ""))
            if t["name"] == "MASSASSIGN":
                # POST-body class: unexpected writable fields accepted?
                if not params:
                    continue
                b = _http(base, "POST", data=urlencode(params))
                a = _http(base, "POST", data=urlencode(params) + t["extra"])
                if (b["status"], len(b["body"])) != (a["status"], len(a["body"])) and \
                        any(x in a["body"] for x in ("role", "admin", "balance", "price")):
                    hits.append(("body", "+base fields", t["extra"], b, a, u))
                continue
            for p in t["params"]:
                if p not in params:
                    continue
                orig = params[p]
                for atk in t["attacks"](orig):
                    b = _http(base + "?" + urlencode({**params, p: orig}))
                    a = _http(base + "?" + urlencode({**params, p: atk}))
                    hit = (b["status"], len(b["body"])) != (a["status"], len(a["body"]))
                    sig = t.get("signatures")
                    if sig and hit:
                        low = a["body"].lower()
                        hit = any(s in low for s in sig)
                    if hit:
                        hits.append((p, orig, atk, b, a, u))
        results[t["name"]] = hits

    threads = []
    for t in TESTERS:
        th = threading.Thread(target=run_tester, args=(t,))
        th.start()
        threads.append(th)
    for th in threads:
        th.join()
    total = 0
    confirmed = 0
    for t in TESTERS:
        hits = results.get(t["name"], [])
        if hits:
            p, orig, atk, b, a, u = hits[0]
            proof = (f"baseline: {b['status']} len={len(b['body'])} (param {p}={orig}); "
                     f"attack: {a['status']} len={len(a['body'])} (param {p}={atk}); "
                     f"diff: baseline vs attack differ on {t['name']}")
            title = f"{t['name']} differential on param '{p}'"
            _cmd_ledger_internal(args.target, title, t["cls"], u,
                                 "high" if t["cls"] in ("IDOR", "SSRF", "TRAVERSAL") else "medium",
                                 proof)
            confirmed += 1
            total += len(hits)
            print(f"  ✓ {t['name']:10s} {len(hits)} differential hit(s) → ledger "
                  f"(e.g. {p}={orig!r}→{atk!r}: {b['status']}/{len(b['body'])}B → {a['status']}/{len(a['body'])}B)")
        else:
            print(f"  · {t['name']:10s} no differential (no matching param or identical responses)")
    print(f"═══ {confirmed}/8 tester(s) produced findings · {total} differential(s) · deduped into the ledger ═══")
    if srv:
        srv.shutdown()
    return 0


# ── 3.7 coverage + report ─────────────────────────────────────────────────────

def cmd_coverage(args):
    camp = _camp(args.target)
    board = _load_json(camp / "phases-state.json", {})
    rows = _ledger_load(args.target)
    hist = {}
    for r in rows:
        hist[r["cls"]] = hist.get(r["cls"], 0) + 1
    print(f"═══ COVERAGE — engagement '{args.target}' ═══")
    gaps = []
    for p in PHASES:
        live = board.get(p["id"]) or ("completed" if _phase_deliverable(args.target, p) else "blocked")
        mark = {"completed": "✓", "in_progress": "▸", "blocked": "·"}.get(live, "·")
        if live != "completed":
            gaps.append((p["id"], p["mandate"]))
        print(f"  {mark} {p['id']:22s} [{live:11s}] via {p['mandate']}")
    print(f"  findings histogram: {', '.join(f'{k}={v}' for k, v in sorted(hist.items())) or '—'}")
    chains = _load_json(camp / "chain-state.json", {}).get("chains", [])
    print(f"  chain candidates: {len(chains)} · ledger rows: {len(rows)}")
    print(f"  gaps: {', '.join(g[0] for g in gaps) or 'none — full coverage'}")
    if gaps:
        print(f"  next mandates: {' → '.join(dict.fromkeys(g[1] for g in gaps))}")
    return 0


def cmd_report(args):
    camp = _camp(args.target)
    rows = _ledger_load(args.target)
    chains = _load_json(camp / "chain-state.json", {}).get("chains", [])
    kage = _load_json(camp / "kage-state.json", {})
    harvest = _load_json(camp / "harvest-state.json", {})
    scope = _load_scope()
    out = args.output or f"{args.target}-spydermonkey-report.md"
    conf = [r for r in rows if r["status"] == "CONFIRMED"]
    sev_hist = {}
    for r in rows:
        sev_hist[r["severity"]] = sev_hist.get(r["severity"], 0) + 1
    L = [f"# SPYDERMONKEY War Report — {args.target}", "",
         f"_generated {_now()} · scope: {scope.get('engagement', 'none declared') if scope else 'none declared'}_",
         "", "## Executive summary", "",
         f"- **{len(rows)}** finding(s) registered · **{len(conf)}** confirmed (3-gate evidence)",
         f"- severity mix: {', '.join(f'{k}={v}' for k, v in sorted(sev_hist.items())) or '—'}",
         f"- **{len(chains)}** chain candidate(s) — low findings combining into high-impact chains",
         f"- **{len(kage.get('rules', []))}** detection rule(s) mirrored (kage)",
         f"- harvest crown rows: {len(harvest.get('crown', []))} (shukaku pricing)",
         ""]
    if rows:
        L += ["## Findings", ""]
        for r in rows:
            L += [f"### {r['id']} — {r['title']} [{r['status']} · {r['severity']} · conf {r['confidence']:.2f}]",
                  f"- class: {r['cls']} · asset: {r['asset']}" + (f" · CWE {r['cwe']}" if r.get("cwe") else ""),
                  f"- proof: {r['proof'][:300]}", ""]
    if chains:
        L += ["## Attack chains", ""]
        for ch in chains:
            L += [f"- **{ch['id']}** [{ch['pattern']}] {ch['severity']} (conf {ch['confidence']:.2f}):"
                  f" {' + '.join(ch['entry_ids'])} → {ch['impact']}"]
        L.append("")
    st = _load_json(camp / "phases-state.json", {})
    L += ["## Phase coverage", ""]
    for p in PHASES:
        live = st.get(p["id"]) or ("completed" if _phase_deliverable(args.target, p) else "blocked")
        L.append(f"- {live:11s} {p['id']} ({p['mandate']})")
    L.append("")
    Path(out).write_text("\n".join(L) + "\n")
    print(f"▸ war report written: {out}")
    print(f"  {len(rows)} finding(s) · {len(conf)} confirmed · {len(chains)} chain(s)"
          f" · {len(kage.get('rules', []))} detection rule(s)")
    return 0


# ── 3.8 relay — remote execution nodes (Bolt-equivalent, Ed25519, scope-gated) ─

RELAY_DIR = Path.home() / ".redteam" / "relays"


def cmd_relay(args):
    if args.action == "init":
        import shutil
        if not shutil.which("ssh-keygen"):
            print("✗ ssh-keygen not found — relay nodes need OpenSSH", file=sys.stderr)
            return 1
        d = RELAY_DIR / args.name
        d.mkdir(parents=True, exist_ok=True)
        key = d / "ed25519.key"
        if not key.exists():
            r = subprocess.run(["ssh-keygen", "-t", "ed25519", "-f", str(key), "-N", "",
                                "-C", f"spydermonkey-relay-{args.name}"], capture_output=True, text=True)
            if r.returncode != 0:
                print(f"✗ ssh-keygen failed: {r.stderr.strip()[:120]}", file=sys.stderr)
                return 1
        (d / "relay.json").write_text(json.dumps(
            {"name": args.name, "host": args.host, "key": str(key),
             "added": _now()}) + "\n")
        print(f"═══ RELAY NODE '{args.name}' — {args.host} ═══")
        print(f"  keypair: {key} (Ed25519)")
        print(f"  install the public key on the node, one line:")
        print(f"    ssh-copy-id -i {key}.pub {args.host}")
        print(f"  then prove it: spydermonkey relay exec --name {args.name} --cmd 'echo paired'")
        print("  every exec scope-checks the host + every host-like token in the command")
        return 0
    if args.action == "list":
        if not RELAY_DIR.exists():
            print("· no relays — relay init --name N --host user@host")
            return 0
        print("═══ RELAY NODES ═══")
        for f in sorted(RELAY_DIR.glob("*/relay.json")):
            r = _load_json(f, {})
            print(f"  ▸ {r.get('name', '?'):12s} {r.get('host', '?')[:44]}  key {r.get('key', '')}")
        return 0
    if args.action == "remove":
        import shutil
        d = RELAY_DIR / args.name
        if not d.exists():
            print(f"✗ no relay '{args.name}'", file=sys.stderr)
            return 2
        shutil.rmtree(d)
        print(f"▸ relay '{args.name}' removed")
        return 0
    if args.action == "exec":
        rf = RELAY_DIR / args.name / "relay.json"
        r = _load_json(rf, {})
        if not r:
            print(f"✗ no relay '{args.name}' — relay init first", file=sys.stderr)
            return 2
        host = r["host"].split("@")[-1].split(":")[0]
        # scope gate: the node's host AND every host-like token in the command
        for tok in [host] + re.findall(r"\b(?:[a-z0-9-]+\.)+[a-z]{2,}\b|\b\d{1,3}(?:\.\d{1,3}){3}\b",
                                       args.relay_cmd.lower()):
            if not _scope_gate(tok):
                return 1
        key = r["key"]
        argv = ["ssh", "-i", key, "-o", "BatchMode=yes",
                "-o", "StrictHostKeyChecking=accept-new", r["host"], "--", args.relay_cmd]
        print(f"═══ RELAY EXEC — {args.name} ({r['host']}) ═══")
        print(f"  ▸ {args.relay_cmd[:100]}")
        try:
            rc = subprocess.run(argv, timeout=args.timeout).returncode
        except subprocess.TimeoutExpired:
            print("✗ relay timed out", file=sys.stderr)
            return 1
        print(f"═══ relay exit {rc} ═══")
        return rc
    return 2


# ── 3.9 mission — one command, the whole war + the intelligence layer ─────────

def cmd_mission(args):
    print("═══ SPYDERMONKEY MISSION — scope gate → fleet → triage → chains → coverage → report ═══")
    scope = _load_scope()
    if scope is None and not _is_lab(args.url):
        print("✗ MISSION REFUSED — no scope authority and the target is not lab-bound", file=sys.stderr)
        print("  scope init --engagement E --in-scope <host> ; then re-run", file=sys.stderr)
        return 1
    rc = 0
    if not args.skip_fleet:
        argv = [sys.executable, str(Path(__file__).resolve()), "fleet",
                "--goal", args.goal or f"full assault on {args.target}",
                "--target", args.target, "--domain", args.domain]
        subprocess.run(argv)   # fleet capability misses don't kill the mission
    # the intelligence layer
    steps = [
        ["ledger", "triage", "--target", args.target],
        ["chain", "detect", "--target", args.target],
        ["coverage", "--target", args.target],
        ["report", "--target", args.target],
    ]
    for st in steps:
        r = subprocess.run([sys.executable, str(Path(__file__).resolve())] + st,
                           capture_output=True, text=True)
        print(r.stdout.rstrip())
        if r.returncode not in (0, 1):
            rc |= 1
    if args.close:
        bc = FAMILY["barbican"][0]
        if bc.exists():
            r = subprocess.run([sys.executable, str(bc), "wipe", "--target", args.target],
                               capture_output=True, text=True)
            print(r.stdout.rstrip())
    print(f"═══ MISSION {'COMPLETE' if rc == 0 else 'COMPLETE WITH BLOCKERS (rc=1)'} —"
          f" report: {args.target}-spydermonkey-report.md ═══")
    return rc


def _verify_gate_live():
    """verify's live proof: spin the demo replica, run ONE 3-gate confirmation
    against it, require CONFIRMED. The engine is exercised, not asserted."""
    try:
        srv, base = _demo_replica()
        time.sleep(0.2)
        b = _http(base + "/api/orders?org_id=acme")
        a = _http(base + "/api/orders?org_id=foreign")
        ok = b["status"] == 200 and a["status"] == 200 and b["body"] != a["body"] \
            and '"org": "foreign"' in a["body"]
        srv.shutdown()
        return ok, "live gate proof: baseline→attack→diff CONFIRMED on the lab replica"
    except Exception:
        return False, "live gate proof failed"


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
    ms = sub.add_parser("mission", help="v3 one command: fleet + intelligence layer + report")
    ms.add_argument("--target", required=True)
    ms.add_argument("--url", required=True)
    ms.add_argument("--domain", required=True)
    ms.add_argument("--goal")
    ms.add_argument("--skip-fleet", action="store_true")
    ms.add_argument("--close", action="store_true")
    ph = sub.add_parser("phases", help="the 13-phase methodology board")
    ph.add_argument("--target", required=True)
    ph.add_argument("--set-phase", dest="set_phase", help="phase id to override")
    ph.add_argument("--phase-status", dest="phase_status",
                    choices=("not_started", "in_progress", "completed", "blocked"))
    lg = sub.add_parser("ledger", help="the finding ledger: add · list · show · triage")
    lg.add_argument("action", choices=("add", "list", "show", "triage"))
    lg.add_argument("--target")
    lg.add_argument("--title")
    lg.add_argument("--cls", default="GENERAL")
    lg.add_argument("--asset", help="url/host the finding is about")
    lg.add_argument("--severity", choices=("info", "low", "medium", "high", "critical"), default="medium")
    lg.add_argument("--proof", help="'baseline: … attack: … diff: …' (else downgraded to hypothesis)")
    lg.add_argument("--cwe")
    lg.add_argument("--id")
    lg.add_argument("--confirmed", action="store_true", help="operator asserts confirmation (still evidence-tagged)")
    gt = sub.add_parser("gate", help="the 3-gate confirmation engine: baseline → attack → diff")
    gt.add_argument("--target", required=True)
    gt.add_argument("--url", required=True, help="baseline request url")
    gt.add_argument("--attack-query", required=True, help="query params for the attack request")
    gt.add_argument("--baseline-query", help="override baseline query (default: the url's own)")
    gt.add_argument("--append-query", action="store_true",
                    help="attack request keeps the baseline params and adds the attack params")
    gt.add_argument("--method", default="GET")
    gt.add_argument("--data", help="POST body")
    gt.add_argument("--header", action="append", help="'Name: value' (repeatable)")
    gt.add_argument("--confirm", help="token that must appear in the attack body for CONFIRMED")
    gt.add_argument("--title", help="ledger title (default: derived)")
    gt.add_argument("--cls", default="DIFFERENTIAL")
    gt.add_argument("--severity", choices=("info", "low", "medium", "high", "critical"), default="medium")
    gt.add_argument("--cwe")
    gt.add_argument("--prove", metavar="SPY-NNN", help="replay the stored 3-gate evidence for a finding")
    ch = sub.add_parser("chain", help="8 chain patterns: low findings → high-impact chains")
    ch.add_argument("action", choices=("detect", "plan"))
    ch.add_argument("--target", required=True)
    ch.add_argument("--id", dest="chain_id", help="CH-NNN for plan")
    cx = sub.add_parser("context", help="session context: endpoints · roles · credentials · functions")
    cx.add_argument("action", choices=("set", "show"))
    cx.add_argument("--target", required=True)
    cx.add_argument("--kind", help="endpoint | role | credential | function")
    cx.add_argument("--value")
    ts = sub.add_parser("testers", help="8 parallel sub-testers over the session context")
    ts.add_argument("--target", required=True)
    ts.add_argument("--url", action="append",
                    help="baseline target url (repeatable: one entry per surface)")
    ts.add_argument("--demo", action="store_true", help="strike the built-in lab replica (no setup)")
    cv = sub.add_parser("coverage", help="phase × deliverable matrix + gaps")
    cv.add_argument("--target", required=True)
    rp = sub.add_parser("report", help="the joint war report (markdown)")
    rp.add_argument("--target", required=True)
    rp.add_argument("--output")
    rl = sub.add_parser("relay", help="remote execution nodes: init · list · exec · remove")
    rl.add_argument("action", choices=("init", "list", "exec", "remove"))
    rl.add_argument("--name")
    rl.add_argument("--host", help="user@host for init")
    rl.add_argument("--cmd", dest="relay_cmd", help="command for exec (scope-checked)")
    rl.add_argument("--timeout", type=int, default=120)
    s = sub.add_parser("status", help="family meta-status")
    s.add_argument("--target")
    sub.add_parser("verify", help="meta self-check + live gate proof")
    ar = sub.add_parser("arsenal", help="scope-gated execution layer (real tools, 13 wrappers)")
    ar.add_argument("action", choices=["list", "plan", "run", "verify"], nargs="?", default="list")
    ar.add_argument("--target")
    ar.add_argument("--only")
    ar.add_argument("--dry-run", action="store_true")
    ar.add_argument("--wordlist")
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
    doc = sub.add_parser("doctor", help="full health check: engines · scope · states · canon · ledger")
    bn = sub.add_parser("bench", help="offline route-level benchmark (route accuracy)")
    fl = sub.add_parser("fleet", help="PARALLEL multi-agent dispatch: one agent per mandate")
    fl.add_argument("--goal", required=True)
    fl.add_argument("--target", required=True)
    fl.add_argument("--domain", required=True)
    fl.add_argument("--agents", help="comma subset (default: full relay)")
    a = ap.parse_args()
    if a.cmd == "tree":
        return cmd_tree(a)
    if a.cmd == "route":
        return cmd_route(a)
    if a.cmd == "run":
        return cmd_run(a)
    if a.cmd == "mission":
        return cmd_mission(a)
    if a.cmd == "phases":
        return cmd_phases(a)
    if a.cmd == "ledger":
        if not a.target:
            print("✗ ledger needs --target", file=sys.stderr)
            return 2
        if a.action == "add" and not (a.title and a.asset):
            print("✗ ledger add needs --title, --asset (and --proof for evidence)", file=sys.stderr)
            return 2
        if a.action == "show" and not a.id:
            print("✗ ledger show needs --id", file=sys.stderr)
            return 2
        return cmd_ledger(a)
    if a.cmd == "gate":
        if not a.prove and not a.attack_query:
            print("✗ gate run needs --attack-query (or --prove SPY-NNN)", file=sys.stderr)
            return 2
        return cmd_gate(a)
    if a.cmd == "chain":
        if a.action == "plan" and not a.chain_id:
            print("✗ chain plan needs --id CH-NNN", file=sys.stderr)
            return 2
        return cmd_chain(a)
    if a.cmd == "context":
        if a.action == "set" and not (a.kind and a.value):
            print("✗ context set needs --kind and --value", file=sys.stderr)
            return 2
        return cmd_context(a)
    if a.cmd == "testers":
        return cmd_testers(a)
    if a.cmd == "coverage":
        return cmd_coverage(a)
    if a.cmd == "report":
        return cmd_report(a)
    if a.cmd == "relay":
        need = {"init": ("name", "host"), "exec": ("name", "relay_cmd"),
                "remove": ("name",)}.get(a.action, ())
        for f in need:
            if not getattr(a, f):
                print(f"✗ relay {a.action} needs --{f.replace('_', '-')}", file=sys.stderr)
                return 2
        return cmd_relay(a)
    if a.cmd == "status":
        return cmd_status(a)
    if a.cmd == "verify":
        return cmd_verify(a)
    if a.cmd == "mandate":
        return cmd_mandate(a)
    if a.cmd == "arsenal":
        return _exec_arsenal(a)
    if a.cmd == "scope":
        return cmd_scope(a)
    if a.cmd == "doctor":
        return cmd_doctor(a)
    if a.cmd == "bench":
        return cmd_bench(a)
    if a.cmd == "fleet":
        return cmd_fleet(a)
    return 2


if __name__ == "__main__":
    sys.exit(main())
