#!/usr/bin/env python3
"""
SPYDERMONKEY MCP v4 — the HolyShit family as MCP tools. stdlib-only JSON-RPC
2.0 over stdio (the MCP stdio transport). Any MCP client (Claude Desktop,
Cursor, any IDE) can drive the family.

The server is a thin, safe adapter over the dispatcher: every tool invokes a
real CLI path, and every live path keeps the shared scope authority. `--test`
validates the whole tool surface without touching an estate.

Run:   python3 mcp_server.py            (stdio loop)
       python3 mcp_server.py --test     (machine-readable self-check)
       python3 mcp_server.py --list     (tool names)
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

VERSION = "5.15.0"
PROTOCOL = "2024-11-05"
SM = str(Path(__file__).resolve().parent / "spydermonkey.py")
NAME_RE = re.compile(r"^[a-z][a-z0-9_]{1,63}$")


def _engine_root() -> Path:
    env = os.environ.get("SPYDERMONKEY_ENGINE_ROOT", "").strip()
    if env:
        return Path(env).expanduser()
    candidates = [Path.home() / ".hermes/skills/security",
                  Path("/home/jewboy420/.hermes/skills/security"),
                  Path("/root/.hermes/skills/security")]
    for c in candidates:
        if c.exists():
            return c
    return candidates[0]


SEC = _engine_root()


class ToolError(Exception):
    pass


def _need(args: dict, *names: str) -> None:
    missing = [n for n in names if args.get(n) in (None, "")]
    if missing:
        raise ToolError(f"missing required argument(s): {', '.join(missing)}")


def _run_sm(argv: list[str], timeout: int = 180) -> dict:
    try:
        r = subprocess.run([sys.executable, SM] + argv + ["--json"],
                           capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise ToolError(f"dispatcher timed out after {timeout}s")
    except Exception as e:
        raise ToolError(f"dispatcher invocation failed: {e}")
    out = (r.stdout or "").strip()
    payload = None
    if out:
        try:
            payload = json.loads(out)
        except Exception:
            payload = None
    if payload is None:
        detail = (out or r.stderr or "no output").strip()
        if r.returncode != 0:
            raise ToolError(detail[:1200])
        return {"rc": r.returncode, "text": detail}
    if isinstance(payload, dict):
        payload.setdefault("_rc", r.returncode)
    return {"rc": r.returncode, "payload": payload}


def _run_engine(engine: str, argv: list[str], timeout: int = 120) -> dict:
    p = SEC / engine / "scripts" / {
        "barbican": "barbican.py", "holyshit": "finder.py",
        "undercroft": "undercroft.py", "3am": "exploit-intel.py",
        "kairo": "kairo.py", "kaisha": "kaisha.py", "shukaku": "shukaku.py",
        "shiki": "shiki.py", "kage": "kage.py", "dojo": "dojo.py",
    }[engine]
    if not p.exists():
        raise ToolError(f"{engine} engine not installed at {p}")
    try:
        r = subprocess.run([sys.executable, str(p)] + argv,
                           capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise ToolError(f"{engine} timed out after {timeout}s")
    out = (r.stdout or "") + (f"\n[stderr] {r.stderr}" if r.stderr else "")
    return {"rc": r.returncode, "text": out.strip()[:20000]}


def _scope_file(args: dict) -> list[str]:
    f = args.get("scope_file")
    return ["--scope-file", f] if f else []


# ── tool handlers ────────────────────────────────────────────────────────────

def h_family_status(a):
    return _run_sm(["status", "--fast"])


def h_family_verify(a):
    argv = ["verify"]
    if a.get("fast"):
        argv.append("--fast")
    return _run_sm(argv, timeout=300)


def h_version(a):
    return _run_sm(["version"])


def h_route_goal(a):
    _need(a, "goal")
    return _run_sm(["route", "--goal", a["goal"]])


def h_scope_check(a):
    _need(a, "value")
    return _run_sm(["scope", "check", "--value", a["value"]] + _scope_file(a))


def h_scope_show(a):
    return _run_sm(["scope", "show"] + _scope_file(a))


def h_scope_history(a):
    argv = ["scope", "history"]
    if a.get("limit"):
        argv += ["--limit", str(a["limit"])]
    return _run_sm(argv + _scope_file(a))


def h_doctor(a):
    argv = ["doctor"]
    if a.get("fast"):
        argv.append("--fast")
    return _run_sm(argv, timeout=300)


def h_bench(a):
    return _run_sm(["bench"])


def h_campaign_list(a):
    return _run_sm(["campaign", "list"])


def h_campaign_show(a):
    _need(a, "target")
    return _run_sm(["campaign", "show", "--target", a["target"]])


def h_campaign_timeline(a):
    _need(a, "target")
    argv = ["campaign", "timeline", "--target", a["target"]]
    if a.get("limit"):
        argv += ["--limit", str(a["limit"])]
    return _run_sm(argv)


def h_mandates_list(a):
    return _run_sm(["mandates", "list"])


def h_mandates_verify(a):
    return _run_sm(["mandates", "verify"])


def h_next_action(a):
    _need(a, "target")
    return _run_sm(["next", "--target", a["target"]])


def h_kernel_absorb(a):
    _need(a, "target", "file")
    return _run_sm(["absorb", "--target", a["target"], "--file", a["file"]])


def h_capabilities(a):
    return _run_sm(["capabilities"])


def h_protect_scan(a):
    argv = ["protect", a.get("action") or "scan"]
    if a.get("target"):
        argv += ["--target", a["target"]]
    if a.get("all_campaigns"):
        argv += ["--all-campaigns"]
    return _run_sm(argv, timeout=300)


def h_takeover(a):
    _need(a, "target", "domain")
    argv = ["takeover", "--target", a["target"], "--domain", a["domain"]]
    if a.get("subdomains"):
        argv += ["--subdomains", a["subdomains"]]
    return _run_sm(argv, timeout=300)


def h_train(a):
    argv = ["train", "--target", a.get("target") or "training"]
    if a.get("classes"):
        argv += ["--classes", a["classes"]]
    return _run_sm(argv, timeout=600)


def h_memory(a):
    _need(a, "target")
    argv = ["memory", "--target", a["target"]]
    if a.get("forget"):
        argv += ["--forget"]
    return _run_sm(argv)


def h_kernel_loop(a):
    _need(a, "target")
    argv = ["loop", "--target", a["target"]]
    if a.get("url"):
        argv += ["--url", a["url"]]
    if a.get("domain"):
        argv += ["--domain", a["domain"]]
    if a.get("agent_cmd"):
        argv += ["--agent-cmd", a["agent_cmd"]]
    argv += ["--max-steps", str(int(a.get("max_steps") or 6))]
    return _run_sm(argv, timeout=900)


def h_ledger_add(a):
    _need(a, "target", "title", "asset")
    argv = ["ledger", "add", "--target", a["target"], "--title", a["title"],
            "--asset", a["asset"]]
    for key, flag in (("cls", "--cls"), ("proof", "--proof"), ("cwe", "--cwe"),
                      ("wstg", "--wstg"), ("attack", "--attack")):
        if a.get(key):
            argv += [flag, str(a[key])]
    if a.get("severity"):
        argv += ["--severity", a["severity"]]
    if a.get("cvss") is not None:
        argv += ["--cvss", str(a["cvss"])]
    return _run_sm(argv)


def h_ledger_list(a):
    _need(a, "target")
    argv = ["ledger", "list", "--target", a["target"]]
    for key, flag in (("status", "--status"), ("cls", "--class"),
                      ("severity", "--severity"), ("search", "--search"),
                      ("sort", "--sort")):
        if a.get(key):
            argv += [flag, str(a[key])]
    if a.get("limit"):
        argv += ["--limit", str(a["limit"])]
    return _run_sm(argv)


def h_ledger_show(a):
    _need(a, "target", "id")
    return _run_sm(["ledger", "show", "--target", a["target"], "--id", a["id"]])


def h_ledger_triage(a):
    _need(a, "target")
    r = _run_sm(["ledger", "triage", "--target", a["target"]])
    return r


def h_ledger_stats(a):
    _need(a, "target")
    return _run_sm(["ledger", "stats", "--target", a["target"]])


def h_ledger_verify(a):
    _need(a, "target")
    argv = ["ledger", "verify", "--target", a["target"]]
    if a.get("strict"):
        argv.append("--strict")
    return _run_sm(argv)


def h_ledger_export(a):
    _need(a, "target")
    argv = ["ledger", "export", "--target", a["target"],
            "--format", a.get("format", "json")]
    if a.get("output"):
        argv += ["--output", a["output"]]
    return _run_sm(argv)


def h_gate_run(a):
    _need(a, "target", "url", "attack_query")
    argv = ["gate", "--target", a["target"], "--url", a["url"],
            "--attack-query", a["attack_query"]]
    for key, flag in (("confirm", "--confirm"), ("expect_regex", "--expect-regex"),
                      ("method", "--method"), ("data", "--data"),
                      ("title", "--title"), ("cls", "--cls"), ("cwe", "--cwe")):
        if a.get(key):
            argv += [flag, str(a[key])]
    if a.get("expect_status") is not None:
        argv += ["--expect-status", str(a["expect_status"])]
    if a.get("append_query"):
        argv.append("--append-query")
    if a.get("auto_confirm"):
        argv.append("--auto-confirm")
    return _run_sm(argv, timeout=60)


def h_chain_detect(a):
    _need(a, "target")
    argv = ["chain", "detect", "--target", a["target"]]
    if a.get("include_hypothesis"):
        argv.append("--include-hypothesis")
    if a.get("min_confidence") is not None:
        argv += ["--min-confidence", str(a["min_confidence"])]
    return _run_sm(argv)


def h_chain_list(a):
    _need(a, "target")
    return _run_sm(["chain", "list", "--target", a["target"]])


def h_phases_board(a):
    _need(a, "target")
    return _run_sm(["phases", "--target", a["target"]])


def h_coverage(a):
    _need(a, "target")
    return _run_sm(["coverage", "--target", a["target"]])


def h_war_report(a):
    _need(a, "target")
    argv = ["report", "--target", a["target"],
            "--format", a.get("format", "markdown")]
    if a.get("output"):
        argv += ["--output", a["output"]]
    return _run_sm(argv, timeout=120)


def h_context_show(a):
    _need(a, "target")
    return _run_sm(["context", "show", "--target", a["target"]])


def h_testers_demo(a):
    _need(a, "target")
    return _run_sm(["testers", "--target", a["target"], "--demo", "--json"],
                   timeout=120)


def h_hypothesis_gen(a):
    _need(a, "target")
    argv = ["hypothesis", "gen", "--target", a["target"], "--json"]
    if a.get("url"):
        argv += ["--url", a["url"]]
    if a.get("kinds"):
        argv += ["--kinds", a["kinds"]]
    return _run_sm(argv, timeout=60)


def h_hypothesis_brief(a):
    _need(a, "target")
    argv = ["hypothesis", "brief", "--target", a["target"], "--json"]
    if a.get("url"):
        argv += ["--url", a["url"]]
    return _run_sm(argv, timeout=60)


def h_hypothesis_run(a):
    _need(a, "target")
    argv = ["hypothesis", "run", "--target", a["target"], "--json"]
    if a.get("id"):
        argv += ["--id", a["id"]]
    return _run_sm(argv, timeout=120)


def h_relay_list(a):
    return _run_sm(["relay", "list"])


def h_arsenal_list(a):
    return _run_engine("barbican", ["verify"]) if False else _run_sm(["arsenal", "list"])


def h_arsenal_plan(a):
    _need(a, "target")
    return _run_sm(["arsenal", "plan", "--target", a["target"]])


def h_catalog_search(a):
    _need(a, "q")
    limit = a.get("limit", 50)
    try:
        limit = int(limit)
    except Exception:
        limit = 50
    argv = ["catalog", "search", str(a["q"]), "--limit", str(max(1, limit))]
    if a.get("cat"):
        argv += ["--cat", str(a["cat"])]
    return _run_sm(argv)


def h_catalog_show(a):
    _need(a, "name")
    return _run_sm(["catalog", "show", str(a["name"])])


def h_skilltree_count(a):
    p = Path(__file__).resolve().parent / "skilltree.py"
    try:
        r = subprocess.run([sys.executable, str(p), "--count", "--json"],
                           capture_output=True, text=True, timeout=60)
        data = json.loads(r.stdout)
        return {"rc": r.returncode, "payload": data}
    except Exception as e:
        raise ToolError(f"skilltree failed: {e}")


def h_skilltree_verify(a):
    p = Path(__file__).resolve().parent / "skilltree.py"
    try:
        r = subprocess.run([sys.executable, str(p), "--verify", "--json"],
                           capture_output=True, text=True, timeout=120)
        data = json.loads(r.stdout)
        return {"rc": r.returncode, "payload": data}
    except Exception as e:
        raise ToolError(f"skilltree verify failed: {e}")


def h_mission_plan(a):
    _need(a, "target", "url", "domain")
    argv = ["mission", "--target", a["target"], "--url", a["url"],
            "--domain", a["domain"], "--plan"]
    if a.get("goal"):
        argv += ["--goal", a["goal"]]
    return _run_sm(argv, timeout=60)


def h_shukaku_hunt_dryrun(a):
    _need(a, "target", "url")
    return _run_engine("shukaku", ["hunt", "--target", a["target"],
                                   "--live", a["url"], "--dry-run"])


def h_shiki_plan_only(a):
    _need(a, "target", "domain")
    argv = ["assault", "--target", a["target"], "--domain", a["domain"],
            "--plan-only"]
    if a.get("url"):
        argv += ["--url", a["url"]]
    return _run_engine("shiki", argv)


def h_kaisha_rungs(a):
    _need(a, "target")
    return _run_engine("kaisha", ["rungs", "--target", a["target"]])


def h_kairo_gene_check(a):
    _need(a, "target")
    return _run_engine("kairo", ["gene", "--check", "--target", a["target"]])


def h_undercroft_probe_table(a):
    return _run_engine("undercroft", ["probe"])


def h_holyshit_surface(a):
    _need(a, "domain")
    return _run_engine("holyshit", ["surface", "--domain", a["domain"]])


def h_dojo_catalog(a):
    return _run_engine("dojo", ["catalog"])


# ── tool surface ─────────────────────────────────────────────────────────────

def _props(**kw):
    return {"type": "object", "properties": kw, "additionalProperties": False}


def _s(desc):
    return {"type": "string", "description": desc}


def _i(desc):
    return {"type": "integer", "description": desc}


def _b(desc):
    return {"type": "boolean", "description": desc}


TOOLS = [
    {"name": "family_status", "description": "Family engines + campaign meta-status (fast presence check).",
     "inputSchema": _props()},
    {"name": "family_verify", "description": "Meta self-check: ten engines, contracts, live gate proof, selftest.",
     "inputSchema": _props(fast=_b("presence-only engine checks"))},
    {"name": "version", "description": "Dispatcher version, schema, data root and scope path.",
     "inputSchema": _props()},
    {"name": "route_goal", "description": "Route a plain-language goal to the mandate sequence.",
     "inputSchema": _props(goal=_s("the operator's goal")), "required": ["goal"]},
    {"name": "scope_check", "description": "Check a domain/url/CIDR against the shared scope authority.",
     "inputSchema": _props(value=_s("domain, URL or IP"),
                           scope_file=_s("optional alternate scope file")),
     "required": ["value"]},
    {"name": "scope_show", "description": "Show the active scope authority and its summary.",
     "inputSchema": _props(scope_file=_s("optional alternate scope file"))},
    {"name": "scope_history", "description": "Recent scope verdicts (audit trail).",
     "inputSchema": _props(limit=_i("number of verdicts"), scope_file=_s("alternate scope"))},
    {"name": "doctor", "description": "Deep health check: compile, engines, scope, campaigns, ledger, MCP, disk.",
     "inputSchema": _props(fast=_b("skip engine verify"))},
    {"name": "bench", "description": "Offline route-accuracy benchmark.",
     "inputSchema": _props()},
    {"name": "campaign_list", "description": "List engagement campaigns with ledger/phase counts.",
     "inputSchema": _props()},
    {"name": "campaign_show", "description": "Show one campaign: manifest, states, ledger, phases.",
     "inputSchema": _props(target=_s("campaign name")), "required": ["target"]},
    {"name": "campaign_timeline", "description": "Campaign event timeline.",
     "inputSchema": _props(target=_s("campaign name"), limit=_i("events")),
     "required": ["target"]},
    {"name": "mandates_list", "description": "The ten mandate contracts with axis/phase/contract status.",
     "inputSchema": _props()},
    {"name": "mandates_verify", "description": "Verify the ten contracts exist and carry every section.",
     "inputSchema": _props()},
    {"name": "next_action", "description": "The one next action with the exact mandate command.",
     "inputSchema": _props(target=_s("campaign name"), url=_s("optional target url"),
                           domain=_s("optional domain")), "required": ["target"]},
    {"name": "kernel_absorb", "description": "Ingest a result JSON through the ledger gates and re-plan (the kernel loop closes here).",
     "inputSchema": _props(target=_s("campaign"), file=_s("result json path")),
     "required": ["target", "file"]},
    {"name": "kernel_loop", "description": "THE AUTONOMOUS LOOP: plan → execute → absorb → repeat until complete (autopilot, or any model via agent_cmd).",
     "inputSchema": _props(target=_s("campaign"), url=_s("target url"),
                           domain=_s("domain"), agent_cmd=_s("external agent command"),
                           max_steps=_i("loop cap (default 6)")),
     "required": ["target"]},
    {"name": "capabilities", "description": "THE MIRROR OF SELF: live-introspected registry (engines · classes · batteries · executors · corpus · priors).",
     "inputSchema": _props()},
    {"name": "protect_scan", "description": "SELF-PROTECTION: operator posture + artifact leak scan (rc=1 while operator strings leak).",
     "inputSchema": _props(action=_s("posture | scan"), target=_s("one campaign"),
                           all_campaigns=_b("scan every campaign"))},
    {"name": "takeover", "description": "THE TAKEOVER ENGINE: dangling CNAME fingerprints (read-only, NO-GAIN).",
     "inputSchema": _props(target=_s("campaign"), domain=_s("domain to check"),
                           subdomains=_s("file of subdomains")),
     "required": ["target", "domain"]},
    {"name": "train", "description": "SELF-PLAY: attack the dojo range, learn per-class priors (the planner orders by what works).",
     "inputSchema": _props(target=_s("campaign"), classes=_s("comma list (default: all)"))},
    {"name": "memory", "description": "ESTATE MEMORY: what the family knows about a target (--forget wipes).",
     "inputSchema": _props(target=_s("campaign"), forget=_b("wipe the memory")),
     "required": ["target"]},
    {"name": "ledger_add", "description": "Register a finding (scope-gated, deduped, evidence-gated).",
     "inputSchema": _props(target=_s("campaign"), title=_s("finding title"),
                           asset=_s("url/host"), proof=_s("baseline: … attack: … diff: …"),
                           cls=_s("class (IDOR/AUTHZ/…)"), severity=_s("severity"),
                           cwe=_s("CWE id"), wstg=_s("WSTG id"), attack=_s("ATT&CK id"),
                           cvss={"type": "number", "description": "CVSS score"}),
     "required": ["target", "title", "asset"]},
    {"name": "ledger_list", "description": "List findings with status/class/severity/search filters.",
     "inputSchema": _props(target=_s("campaign"), status=_s("status filter"),
                           cls=_s("class filter"), severity=_s("severity filter"),
                           search=_s("substring search"), sort=_s("id|severity|cvss|confidence|class|updated"),
                           limit=_i("max rows")), "required": ["target"]},
    {"name": "ledger_show", "description": "Show one finding by id.",
     "inputSchema": _props(target=_s("campaign"), id=_s("SPY-NNN")),
     "required": ["target", "id"]},
    {"name": "ledger_triage", "description": "Triager gates: evidence, scope, duplicates, severity-impact.",
     "inputSchema": _props(target=_s("campaign")), "required": ["target"]},
    {"name": "ledger_stats", "description": "Ledger statistics: severity/status/class histograms, risk score.",
     "inputSchema": _props(target=_s("campaign")), "required": ["target"]},
    {"name": "ledger_verify", "description": "Verify the tamper-evident ledger hash chain.",
     "inputSchema": _props(target=_s("campaign"), strict=_b("require every row signed")),
     "required": ["target"]},
    {"name": "ledger_export", "description": "Export findings as JSON/JSONL/CSV/markdown/SARIF.",
     "inputSchema": _props(target=_s("campaign"), format=_s("json|jsonl|csv|markdown|sarif"),
                           output=_s("output path")), "required": ["target"]},
    {"name": "gate_run", "description": "3-gate confirmation: baseline → attack → measurable diff (live, scope-gated).",
     "inputSchema": _props(target=_s("campaign"), url=_s("baseline URL"),
                           attack_query=_s("attack query string"), confirm=_s("required token"),
                           expect_regex=_s("required regex"), expect_status=_i("required status"),
                           method=_s("HTTP method"), data=_s("request body"),
                           append_query=_b("merge baseline query"), auto_confirm=_b("accept a stable diff"),
                           title=_s("finding title"), cls=_s("class"), cwe=_s("CWE id")),
     "required": ["target", "url", "attack_query"]},
    {"name": "chain_detect", "description": "Detect kill chains from confirmed findings (8 patterns).",
     "inputSchema": _props(target=_s("campaign"), include_hypothesis=_b("include hypotheses"),
                           min_confidence={"type": "number"}),
     "required": ["target"]},
    {"name": "chain_list", "description": "List saved chain candidates.",
     "inputSchema": _props(target=_s("campaign")), "required": ["target"]},
    {"name": "phases_board", "description": "The 13-phase methodology board computed from real deliverables.",
     "inputSchema": _props(target=_s("campaign")), "required": ["target"]},
    {"name": "coverage", "description": "Coverage matrix, ledger histogram and the gap list.",
     "inputSchema": _props(target=_s("campaign")), "required": ["target"]},
    {"name": "war_report", "description": "Write the joint war report (markdown/json/sarif).",
     "inputSchema": _props(target=_s("campaign"), format=_s("markdown|json|sarif"),
                           output=_s("output path")), "required": ["target"]},
    {"name": "context_show", "description": "Session context: endpoints, roles, credentials, functions.",
     "inputSchema": _props(target=_s("campaign")), "required": ["target"]},
    {"name": "testers_demo", "description": "Strike the built-in lab replica with the 18 sub-testers.",
     "inputSchema": _props(target=_s("campaign")), "required": ["target"]},
    {"name": "hypothesis_gen", "description": "THE REASONING ENGINE: rank wall-checked hypothesis cards (surface/cve-map/variant/chain) that guide a model toward unconfirmed vulnerability instances. Generation is offline; execution stays scope-gated.",
     "inputSchema": _props(target=_s("campaign"), url=_s("optional surface url"),
                           kinds=_s("comma list: surface,cve-map,variant,chain")),
     "required": ["target"]},
    {"name": "hypothesis_brief", "description": "The model brief: top-ranked hypothesis cards + the exact loop to run them through the 3-gate engine.",
     "inputSchema": _props(target=_s("campaign"), url=_s("optional surface url")),
     "required": ["target"]},
    {"name": "hypothesis_run", "description": "Fire ONE hypothesis card through the 3-gate discipline (baseline → attack → class verdict → ledger). Confirmed registers CONFIRMED; non-decisive HYPOTHESIS; identical DISPROVEN (nothing registered).",
     "inputSchema": _props(target=_s("campaign"), id=_s("card id (default: top executable)")),
     "required": ["target"]},
    {"name": "relay_list", "description": "Remote execution nodes and key state.",
     "inputSchema": _props()},
    {"name": "arsenal_list", "description": "Installed arsenal tools × capabilities.",
     "inputSchema": _props()},
    {"name": "arsenal_plan", "description": "Scope-gated arsenal run plan (nothing executes).",
     "inputSchema": _props(target=_s("target")), "required": ["target"]},
    {"name": "catalog_search", "description": "Search the 1,053-entry known-tool catalog (offensive tooling reference index; info only, execution stays scope-gated via arsenal).",
     "inputSchema": _props(q=_s("search term (name/description/category)"),
                           limit=_i("max results (default 50)"),
                           cat=_s("optional category prefix filter, e.g. web, recon/dns, wifi")),
     "required": ["q"]},
    {"name": "catalog_show", "description": "Show one catalog entry: category, mode, source, one-line description (reference only — never executes).",
     "inputSchema": _props(name=_s("tool name, e.g. 'nmap'")), "required": ["name"]},
    {"name": "skilltree_count", "description": "Count the generated technique skill files.",
     "inputSchema": _props()},
    {"name": "skilltree_verify", "description": "Verify index ↔ files ↔ WSTG/CWE/ATT&CK bindings.",
     "inputSchema": _props()},
    {"name": "mission_plan", "description": "Plan a full mission (scope + fleet + intelligence steps).",
     "inputSchema": _props(target=_s("campaign"), url=_s("target URL"), domain=_s("domain"),
                           goal=_s("goal")), "required": ["target", "url", "domain"]},
    {"name": "shukaku_hunt_dryrun", "description": "SHUKAKU harvest-surface candidates (dry-run).",
     "inputSchema": _props(target=_s("campaign"), url=_s("base URL")),
     "required": ["target", "url"]},
    {"name": "shiki_plan_only", "description": "SHIKI full-assault plan; nothing executes.",
     "inputSchema": _props(target=_s("campaign"), domain=_s("domain"), url=_s("url")),
     "required": ["target", "domain"]},
    {"name": "kaisha_rungs", "description": "KAISHA ladder rungs for a campaign.",
     "inputSchema": _props(target=_s("campaign")), "required": ["target"]},
    {"name": "kairo_gene_check", "description": "KAIRO five-gene validator (NO Δ = NO VECTOR).",
     "inputSchema": _props(target=_s("campaign")), "required": ["target"]},
    {"name": "undercroft_probe_table", "description": "UNDERCROFT's 15 NO-GAIN probe plans.",
     "inputSchema": _props()},
    {"name": "holyshit_surface", "description": "HOLYSHIT attack-surface checklist for a domain.",
     "inputSchema": _props(domain=_s("domain")), "required": ["domain"]},
    {"name": "dojo_catalog", "description": "DOJO's buildable vulnerable replicas.",
     "inputSchema": _props()},
]

HANDLERS = {
    "family_status": h_family_status, "family_verify": h_family_verify,
    "version": h_version, "route_goal": h_route_goal,
    "scope_check": h_scope_check, "scope_show": h_scope_show,
    "scope_history": h_scope_history, "doctor": h_doctor, "bench": h_bench,
    "campaign_list": h_campaign_list, "campaign_show": h_campaign_show,
    "campaign_timeline": h_campaign_timeline,
    "mandates_list": h_mandates_list, "mandates_verify": h_mandates_verify,
    "next_action": h_next_action, "ledger_add": h_ledger_add,
    "kernel_absorb": h_kernel_absorb, "kernel_loop": h_kernel_loop,
    "capabilities": h_capabilities, "protect_scan": h_protect_scan,
    "takeover": h_takeover, "train": h_train, "memory": h_memory,
    "ledger_list": h_ledger_list, "ledger_show": h_ledger_show,
    "ledger_triage": h_ledger_triage, "ledger_stats": h_ledger_stats,
    "ledger_verify": h_ledger_verify, "ledger_export": h_ledger_export,
    "gate_run": h_gate_run, "chain_detect": h_chain_detect,
    "chain_list": h_chain_list, "phases_board": h_phases_board,
    "coverage": h_coverage, "war_report": h_war_report,
    "context_show": h_context_show, "testers_demo": h_testers_demo,
    "hypothesis_gen": h_hypothesis_gen, "hypothesis_brief": h_hypothesis_brief,
    "hypothesis_run": h_hypothesis_run,
    "relay_list": h_relay_list, "arsenal_list": h_arsenal_list,
    "arsenal_plan": h_arsenal_plan, "catalog_search": h_catalog_search,
    "catalog_show": h_catalog_show, "skilltree_count": h_skilltree_count,
    "skilltree_verify": h_skilltree_verify,
    "mission_plan": h_mission_plan,
    "shukaku_hunt_dryrun": h_shukaku_hunt_dryrun,
    "shiki_plan_only": h_shiki_plan_only, "kaisha_rungs": h_kaisha_rungs,
    "kairo_gene_check": h_kairo_gene_check,
    "undercroft_probe_table": h_undercroft_probe_table,
    "holyshit_surface": h_holyshit_surface, "dojo_catalog": h_dojo_catalog,
}


# v5.15 — THE 23 CHAINS AS MCP TOOLS: every feeding chain + single-tool runs,
# scope-gated through the arsenal (which gates through the shared authority).
def h_arsenal_chain(a):
    _need(a, "target")
    argv = ["arsenal", "run", "--target", a["target"], "--json"]
    if a.get("chain"):
        argv += ["--chain", a["chain"]]
    if a.get("only"):
        argv += ["--only", a["only"]]
    if a.get("dry_run"):
        argv += ["--dry-run"]
    if a.get("wordlist"):
        argv += ["--wordlist", a["wordlist"]]
    if a.get("timeout"):
        argv += ["--timeout", str(int(a["timeout"]))]
    return _run_sm(argv, timeout=max(60, int(a.get("timeout") or 300) + 30))


def h_arsenal_run(a):
    a = dict(a)
    a["chain"] = None
    return h_arsenal_chain(a)


_CHAINS = ["recon", "web", "tls", "net", "dns", "content", "api", "services",
           "cms", "win", "osint", "db", "takeover", "cloud", "packet", "fuzz",
           "cve-sweep", "exposure-sweep", "takeover-full", "cloud-full",
           "db-full", "mail-full", "cms-full"]
_CHAIN_INPUT = {
    "type": "object",
    "properties": {
        "target": {"type": "string", "description": "In-scope target (host or url)."},
        "dry_run": {"type": "boolean", "description": "Plan only — nothing executes."},
        "wordlist": {"type": "string", "description": "Optional wordlist/resolver path."},
        "timeout": {"type": "integer", "description": "Per-tool timeout seconds (default 300)."},
    },
    "required": ["target"],
}
_RUN_INPUT = dict(_CHAIN_INPUT)
_RUN_INPUT["properties"] = dict(_CHAIN_INPUT["properties"])
_RUN_INPUT["properties"]["only"] = {"type": "string",
    "description": "Comma-separated arsenal tool ids (e.g. sslscan,nuclei)."}
_RUN_INPUT["required"] = ["target"]

for _c in _CHAINS:
    TOOLS.append({"name": f"arsenal_chain_{_c.replace('-', '_')}",
                  "description": f"Scope-gated execution of the '{_c}' feeding chain "
                                 f"(stages feed each other; every stage passes the shared "
                                 f"scope authority; dry_run=true plans without executing).",
                  "inputSchema": dict(_CHAIN_INPUT)})
    HANDLERS[f"arsenal_chain_{_c.replace('-', '_')}"] = h_arsenal_chain

TOOLS.append({"name": "arsenal_run",
              "description": "Scope-gated execution of ONE OR MORE named arsenal tools "
                             "(--only sslscan,nuclei...). Refuses out-of-estate targets (rc=1).",
              "inputSchema": _RUN_INPUT})
HANDLERS["arsenal_run"] = h_arsenal_run


def _tool_text(result) -> tuple[str, dict | None]:
    if isinstance(result, dict) and "payload" in result:
        payload = result["payload"]
        return json.dumps(payload, indent=2, ensure_ascii=False), payload if isinstance(payload, dict) else None
    if isinstance(result, dict) and "text" in result:
        return str(result["text"]), None
    return json.dumps(result, indent=2, ensure_ascii=False), result if isinstance(result, dict) else None


def call_tool(name: str, args: dict | None) -> dict:
    args = args or {}
    handler = HANDLERS.get(name)
    if not handler:
        raise KeyError(name)
    result = handler(args)
    text, structured = _tool_text(result)
    out = {"content": [{"type": "text", "text": text}], "isError": False}
    if structured is not None:
        out["structuredContent"] = structured
    return out


def _error(rid, code, message, data=None):
    err = {"code": code, "message": message}
    if data is not None:
        err["data"] = data
    return {"jsonrpc": "2.0", "id": rid, "error": err}


def handle(req):
    if not isinstance(req, dict):
        return _error(None, -32600, "invalid request")
    rid = req.get("id")
    method = req.get("method")
    if not method:
        return _error(rid, -32600, "invalid request: missing method")
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": rid, "result": {
            "protocolVersion": PROTOCOL,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": "spydermonkey", "version": VERSION},
        }}
    if method in ("notifications/initialized", "initialized"):
        return None
    if method == "ping":
        return {"jsonrpc": "2.0", "id": rid, "result": {}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": rid, "result": {"tools": TOOLS}}
    if method == "resources/list":
        return {"jsonrpc": "2.0", "id": rid, "result": {"resources": []}}
    if method == "prompts/list":
        return {"jsonrpc": "2.0", "id": rid, "result": {"prompts": []}}
    if method == "tools/call":
        params = req.get("params") or {}
        if not isinstance(params, dict):
            return _error(rid, -32602, "tools/call params must be an object")
        name = params.get("name")
        if not isinstance(name, str) or name not in HANDLERS:
            return _error(rid, -32602, f"unknown tool: {name}")
        try:
            result = call_tool(name, params.get("arguments") or {})
        except ToolError as e:
            result = {"content": [{"type": "text", "text": f"tool error: {e}"}],
                      "isError": True}
        except Exception as e:
            result = {"content": [{"type": "text", "text": f"tool error: {e}"}],
                      "isError": True}
        return {"jsonrpc": "2.0", "id": rid, "result": result}
    return _error(rid, -32601, f"unknown method {method}")


def _test() -> int:
    errors = []
    names = [t["name"] for t in TOOLS]
    if len(names) != len(set(names)):
        errors.append("duplicate tool names")
    for t in TOOLS:
        if not NAME_RE.match(t.get("name", "")):
            errors.append(f"bad tool name: {t.get('name')}")
        if not t.get("description"):
            errors.append(f"{t.get('name')}: missing description")
        schema = t.get("inputSchema")
        if not isinstance(schema, dict) or schema.get("type") != "object":
            errors.append(f"{t.get('name')}: invalid inputSchema")
        if t["name"] not in HANDLERS:
            errors.append(f"{t.get('name')}: no handler")
        if len(t.get("required", [])) and not all(
                r in schema.get("properties", {}) for r in t.get("required", [])):
            errors.append(f"{t.get('name')}: required property missing from schema")
    payload = {"version": VERSION, "protocol": PROTOCOL, "ok": not errors,
               "count": len(TOOLS), "tools": names, "errors": errors}
    print(json.dumps(payload, indent=2))
    return 0 if not errors else 1


def _run_stdio():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception as e:
            print(json.dumps(_error(None, -32700, f"parse error: {e}")), flush=True)
            continue
        batch = req if isinstance(req, list) else [req]
        replies = []
        for item in batch:
            reply = handle(item)
            if reply is not None:
                replies.append(reply)
        if not replies:
            continue
        out = replies if isinstance(req, list) else replies[0]
        print(json.dumps(out), flush=True)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--test" in argv:
        return _test()
    if "--list" in argv:
        for t in TOOLS:
            print(t["name"])
        return 0
    if "--help" in argv or "-h" in argv:
        print(__doc__)
        return 0
    _run_stdio()
    return 0


if __name__ == "__main__":
    sys.exit(main())
