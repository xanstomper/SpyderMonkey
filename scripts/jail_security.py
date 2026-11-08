#!/usr/bin/env python3
"""SpyderMonkey jail security — integrity monitor for the takeover stack.

`jail status`   — verify every enforcement layer is armed and untampered.
`jail arm`      — record the expected state (contracts + hooks + settings).
`jail check`    — one-shot tamper report (rc=1 on any discrepancy).
`jail watch`    — background watcher: re-checks on an interval; restores
                  removed hooks ONLY with --restore (operator opt-in).

What it defends: the contract files (mandate-session/mandate/AGENTS.md), the
Claude Code hook wiring (~/.claude/settings.json), the deployed carriers
(~/claude/commands, ~/.config/opencode/agents), and the marker semantics.
Detection beats prevention: an attacker (or a drifted agent) that touches
these files is caught in seconds, and the fingerprint is the same SM8.3
contract ID the session announces.
"""

import argparse
import hashlib
import json
import os
import socket
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SUPERVISED = [
    REPO / "references" / "mandate-session.md",
    REPO / "references" / "mandate.md",
    REPO / "agents" / "AGENTS.md",
    REPO / "scripts" / "claude_hook_scope.py",
    REPO / "scripts" / "claude_hook_sessionstart.py",
    Path.home() / ".claude" / "settings.json",
    Path.home() / ".claude" / "commands" / "spydermonkey.md",
    Path.home() / ".config" / "opencode" / "agents" / "spydermonkey.md",
]
ARM_FILE = Path.home() / ".redteam" / ".jail-arm.json"


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16]


def _state() -> dict:
    out = {}
    for p in SUPERVISED:
        out[str(p)] = _sha(p) if p.exists() else None
    return out


def _required_hooklines() -> list[str]:
    return ["claude_hook_scope.py", "claude_hook_sessionstart.py"]


def _hook_status() -> list[dict]:
    s = Path.home() / ".claude" / "settings.json"
    res = []
    if not s.exists():
        return []
    try:
        data = json.loads(s.read_text(encoding="utf-8"))
    except Exception as e:
        return [{"hook": "settings.json", "present": False, "detail": str(e)}]
    text = s.read_text(encoding="utf-8")
    for hook in _required_hooklines():
        res.append({"hook": hook, "present": hook in text})
    res.append({"hook": "settings.json", "present": True,
                "detail": ",".join((data.get("hooks") or {}).keys())})
    return res


def cmd_jail(args) -> int:
    action = args.action

    if action == "arm":
        ARM_FILE.parent.mkdir(parents=True, exist_ok=True)
        ARM_FILE.write_text(json.dumps(
            {"state": _state(), "hooks": [h["present"] for h in _hook_status()],
             "armed": time.strftime("%Y-%m-%dT%H:%M:%S%z")},
            indent=2), encoding="utf-8")
        print(f"⚙ JAIL ARMED — {len(_state())} supervised files")
        return 0

    if action == "status":
        hooks = _hook_status()
        print("═══ SPYDERMONKEY JAIL ═══")
        print(f"  contract:   {next((l for l in (REPO / 'references' / 'mandate-session.md').read_text(encoding='utf-8').splitlines() if l.startswith('Contract ID:')), 'unknown')}")
        for h in hooks:
            mark = "✓" if h["present"] else "✗"
            print(f"  hook:       {mark} {h['hook']} {h.get('detail', '')}")
        print(f"  armed:      {'YES (jail-arm.json)' if ARM_FILE.exists() else 'no — run: smk jail arm'}")
        if not args.json:
            return 0
        print(json.dumps({"hooks": hooks,
                          "contract": [l for l in (REPO / "references" / "mandate-session.md").read_text(encoding="utf-8").splitlines() if l.startswith("Contract ID:")][0]}))
        return 0

    if action == "check":
        bad = []
        if not ARM_FILE.exists():
            print("✗ jail not armed — run: smk jail arm", file=sys.stderr)
            return 1
        expected = json.loads(ARM_FILE.read_text(encoding="utf-8"))
        want_state = expected["state"]
        want_hooks = expected.get("hooks", [])
        for path, want in want_state.items():
            p = Path(path)
            now = _sha(p) if p.exists() else None
            if now != want:
                bad.append(f"{path}: {'MISSING' if now is None else 'TAMPERED'}")
        now_hooks = [h["present"] for h in _hook_status()]
        if now_hooks != want_hooks:
            bad.append("hook wiring changed "
                       f"(armed={want_hooks} now={now_hooks})")
        if bad:
            print("✗ JAIL BREACH:")
            for b in bad:
                print(f"    {b}")
            return 1
        print("✓ JAIL INTACT — all layers verified")
        return 0

    if action == "watch":
        interval = args.interval
        print(f"⚙ jail watch every {interval}s (Ctrl-C to stop)…")
        try:
            while True:
                rc = cmd_jail(argparse.Namespace(action="check", json=False))
                if rc != 0:
                    msg = "✗ JAIL BREACH DETECTED at " + time.strftime("%H:%M:%S")
                    print(msg)
                    if args.restore:
                        _restore()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nwatch stopped")
        return 0

    return 2


def _restore() -> None:
    """Re-wire the Claude hooks from the repo carriers (operator opted in)."""
    s = Path.home() / ".claude" / "settings.json"
    data = json.loads(s.read_text(encoding="utf-8")) if s.exists() else {}
    hooks = data.setdefault("hooks", {})
    pre = hooks.setdefault("PreToolUse", [])
    if not any("claude_hook_scope" in h.get("command", "")
               for e in pre for h in e.get("hooks", [])):
        pre.append({"matcher": "Bash", "hooks": [{"type": "command",
                    "command": f"python3 {REPO}/scripts/claude_hook_scope.py"}]})
    ss = hooks.setdefault("SessionStart", [])
    if not any("claude_hook_sessionstart" in h.get("command", "")
               for e in ss for h in e.get("hooks", [])):
        ss.append({"hooks": [{"type": "command",
                   "command": f"python3 {REPO}/scripts/claude_hook_sessionstart.py"}]})
    s.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print("⚙ hooks re-wired")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(prog="smk jail")
    ap.add_argument("action", choices=("status", "arm", "check", "watch"))
    ap.add_argument("--interval", type=int, default=30)
    ap.add_argument("--restore", action="store_true",
                    help="watch: re-wire removed hooks automatically")
    ap.add_argument("--json", action="store_true")
    sys.exit(cmd_jail(ap.parse_args()))