#!/usr/bin/env python3
"""
SPYDERMONKEY MCP — the HolyShit family as MCP tools. stdlib-only JSON-RPC 2.0
over stdio (the MCP stdio transport). Any MCP client (Claude Desktop, Cursor,
any IDE) can drive the family.

Run:  python3 mcp_server.py            (stdio loop)
Tools: family_status · family_verify · route_goal · scope_check · doctor ·
       bench · shukaku_hunt_dryrun · shiki_plan_only · kaisha_rungs ·
       kairo_gene_check · undercroft_probe_table · holyshit_surface ·
       ledger_triage · chain_detect · phases_board · coverage · relay_list ·
       war_report
"""
import json
import subprocess
import sys
from pathlib import Path

SEC = Path.home() / ".hermes/skills/security"
SM = str(Path(__file__).resolve().parent / "spydermonkey.py")

TOOLS = [
    {"name": "family_status", "description": "HolyShit family: every mandate's engine presence + verify state",
     "inputSchema": {"type": "object", "properties": {}}},
    {"name": "family_verify", "description": "Meta self-check: all ten family engines verify",
     "inputSchema": {"type": "object", "properties": {}}},
    {"name": "route_goal", "description": "Route a plain-language goal to the mandate sequence",
     "inputSchema": {"type": "object", "properties": {"goal": {"type": "string"}},
                     "required": ["goal"]}},
    {"name": "scope_check", "description": "Check a domain/url against the scope authority",
     "inputSchema": {"type": "object", "properties": {"value": {"type": "string"}},
                     "required": ["value"]}},
    {"name": "doctor", "description": "Family health check: engines · scope · states · canon",
     "inputSchema": {"type": "object", "properties": {}}},
    {"name": "bench", "description": "Offline route-level benchmark (route accuracy)",
     "inputSchema": {"type": "object", "properties": {}}},
    {"name": "shukaku_hunt_dryrun", "description": "SHUKAKU harvest-surface candidates for a base URL (dry-run, read-only)",
     "inputSchema": {"type": "object", "properties": {"target": {"type": "string"},
                                                      "url": {"type": "string"}},
                     "required": ["target", "url"]}},
    {"name": "shiki_plan_only", "description": "SHIKI assault plan: the full assault sequence, nothing executes",
     "inputSchema": {"type": "object", "properties": {"target": {"type": "string"},
                                                      "domain": {"type": "string"},
                                                      "url": {"type": "string"}},
                     "required": ["target", "domain"]}},
    {"name": "kaisha_rungs", "description": "KAISHA ladder rungs for a campaign",
     "inputSchema": {"type": "object", "properties": {"target": {"type": "string"}},
                     "required": ["target"]}},
    {"name": "kairo_gene_check", "description": "KAIRO five-gene validator (NO Δ = NO VECTOR)",
     "inputSchema": {"type": "object", "properties": {"target": {"type": "string"}},
                     "required": ["target"]}},
    {"name": "undercroft_probe_table", "description": "UNDERCROFT's 15 NO-GAIN probe plans",
     "inputSchema": {"type": "object", "properties": {}}},
    {"name": "holyshit_surface", "description": "HOLYSHIT attack-surface checklist for a domain",
     "inputSchema": {"type": "object", "properties": {"domain": {"type": "string"}},
                     "required": ["domain"]}},
    {"name": "ledger_triage", "description": "Triager gates over the campaign's finding ledger (scope · evidence · duplicates)",
     "inputSchema": {"type": "object", "properties": {"target": {"type": "string"}},
                     "required": ["target"]}},
    {"name": "chain_detect", "description": "Detect high-impact attack chains from confirmed low findings",
     "inputSchema": {"type": "object", "properties": {"target": {"type": "string"}},
                     "required": ["target"]}},
    {"name": "phases_board", "description": "The 13-phase methodology board (computed from real deliverables)",
     "inputSchema": {"type": "object", "properties": {"target": {"type": "string"}},
                     "required": ["target"]}},
    {"name": "coverage", "description": "Coverage matrix: phases × deliverables × ledger histogram + gaps",
     "inputSchema": {"type": "object", "properties": {"target": {"type": "string"}},
                     "required": ["target"]}},
    {"name": "relay_list", "description": "Remote execution nodes (relay): names + hosts + keypaths",
     "inputSchema": {"type": "object", "properties": {}}},
    {"name": "war_report", "description": "Generate the joint war report (markdown) for a campaign",
     "inputSchema": {"type": "object", "properties": {"target": {"type": "string"}},
                     "required": ["target"]}},
]


def _run(argv):
    try:
        r = subprocess.run(argv, capture_output=True, text=True, timeout=120)
        return (r.stdout + (f"\n[stderr] {r.stderr}" if r.returncode else "")).strip()
    except Exception as e:
        return f"error: {e}"


def call_tool(name, args):
    t = args.get("target", "demo")
    if name == "family_status":
        return _run([sys.executable, SM, "status"])
    if name == "family_verify":
        return _run([sys.executable, SM, "verify"])
    if name == "route_goal":
        return _run([sys.executable, SM, "route", "--goal", args["goal"]])
    if name == "scope_check":
        return _run([sys.executable, SM, "scope", "check", "--value", args["value"]])
    if name == "doctor":
        return _run([sys.executable, SM, "doctor"])
    if name == "bench":
        return _run([sys.executable, SM, "bench"])
    if name == "shukaku_hunt_dryrun":
        return _run([sys.executable, str(SEC / "shukaku/scripts/shukaku.py"),
                     "hunt", "--target", t, "--live", args["url"], "--dry-run"])
    if name == "shiki_plan_only":
        argv = [sys.executable, str(SEC / "shiki/scripts/shiki.py"), "assault",
                "--target", t, "--domain", args["domain"], "--plan-only"]
        if args.get("url"):
            argv += ["--url", args["url"]]
        return _run(argv)
    if name == "kaisha_rungs":
        return _run([sys.executable, str(SEC / "kaisha/scripts/kaisha.py"),
                     "rungs", "--target", t])
    if name == "kairo_gene_check":
        return _run([sys.executable, str(SEC / "kairo/scripts/kairo.py"),
                     "gene", "--check", "--target", t])
    if name == "undercroft_probe_table":
        return _run([sys.executable, str(SEC / "undercroft/scripts/undercroft.py"), "probe"])
    if name == "holyshit_surface":
        return _run([sys.executable, str(SEC / "holyshit-mode/scripts/finder.py"),
                     "surface", "--domain", args["domain"]])
    if name == "ledger_triage":
        return _run([sys.executable, SM, "ledger", "triage", "--target", t])
    if name == "chain_detect":
        return _run([sys.executable, SM, "chain", "detect", "--target", t])
    if name == "phases_board":
        return _run([sys.executable, SM, "phases", "--target", t])
    if name == "coverage":
        return _run([sys.executable, SM, "coverage", "--target", t])
    if name == "relay_list":
        return _run([sys.executable, SM, "relay", "list"])
    if name == "war_report":
        return _run([sys.executable, SM, "report", "--target", t])
    return f"unknown tool: {name}"


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue
        method = req.get("method", "")
        rid = req.get("id")
        if method == "initialize":
            result = {"protocolVersion": "2024-11-05",
                      "capabilities": {"tools": {}},
                      "serverInfo": {"name": "spydermonkey", "version": "3.0.0"}}
        elif method == "notifications/initialized":
            continue
        elif method == "tools/list":
            result = {"tools": TOOLS}
        elif method == "tools/call":
            out = call_tool(req["params"]["name"], req["params"].get("arguments", {}))
            result = {"content": [{"type": "text", "text": out}]}
        elif method == "ping":
            result = {}
        else:
            if rid is not None:
                print(json.dumps({"jsonrpc": "2.0", "id": rid,
                                  "error": {"code": -32601,
                                            "message": f"unknown method {method}"}}),
                      flush=True)
            continue
        if rid is not None:
            print(json.dumps({"jsonrpc": "2.0", "id": rid, "result": result}), flush=True)


if __name__ == "__main__":
    main()
