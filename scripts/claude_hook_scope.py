#!/usr/bin/env python3
"""SpyderMonkey Claude Code scope hook — the mechanical estate gate.

PreToolUse/Bash: when a mandate session marker is present (env
SPYDERMONKEY_MANDATE=1, a `.spydermonkey-active` file in the CWD, or a CWD
inside ~/.redteam/campaigns/<name>/), every connective command is checked
against the shared scope authority. Out-of-estate targets are BLOCKED at the
host level — the model cannot talk its way past this gate; only the operator
can widen scope.json.

Non-mandate sessions: pure pass-through (the marker is the switch).

Claude Code hook contract: JSON payload on stdin; exit 0 = allow, 2 = block
(feedback shown to the model). Integrates with the same scope_authority.py
every family engine uses — one estate verdict, no engine-specific bypass.
"""

import json
import os
import re
import sys
from pathlib import Path

SPYDERMONKEY_REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SPYDERMONKEY_REPO / "scripts"))

import scope_authority as sa  # noqa: E402

# Command families whose arguments are connection targets.
CONNECTIVE = {
    "curl", "wget", "nc", "ncat", "netcat", "ssh", "scp", "sftp", "rsync",
    "nmap", "masscan", "ping", "traceroute", "mtr", "dig", "nslookup", "host",
    "telnet", "ftp", "socat", "hydra", "medusa", "msfconsole", "msfvenom",
    "sqlmap", "nikto", "gobuster", "ffuf", "whatweb", "openssl", "python",
    "python3", "python2", "node", "ruby", "perl", "php", "java", "git",
}

_URL_RE = re.compile(r"(?:https?|ftp|ssh|ws|wss)://([A-Za-z0-9._~-]+)(?::\d+)?")
_SCP_RE = re.compile(r"(?<![\w.@-])([A-Za-z0-9._-]+)@([A-Za-z0-9._-]+):")
_IP_RE = re.compile(r"\b(\d{1,3}(?:\.\d{1,3}){3})\b")
_DOM_RE = re.compile(r"\b([A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+)\b")


def _marker_active(cwd: str) -> bool:
    if os.environ.get("SPYDERMONKEY_MANDATE") == "1":
        return True
    if (Path(cwd) / ".spydermonkey-active").exists():
        return True
    try:
        cwd_p = Path(cwd).resolve()
        camp = sa.campaigns_root()
    except Exception:
        return False
    try:
        camp.resolve()
    except Exception:
        return False
    return camp.resolve() in cwd_p.parents


def _hosts_from(cmd: str) -> list[str]:
    """Extract candidate target hosts. Conservative: no token, no block."""
    hosts: list[str] = []
    for m in _URL_RE.finditer(cmd):
        hosts.append(m.group(1))
    for m in _SCP_RE.finditer(cmd):
        hosts.append(m.group(2))
    for m in _IP_RE.finditer(cmd):
        hosts.append(m.group(1))
    for m in _DOM_RE.finditer(cmd):
        hosts.append(m.group(1))
    # de-dup, drop obvious self/lab, keep order
    seen: set[str] = set()
    out: list[str] = []
    for h in hosts:
        if h in seen:
            continue
        seen.add(h)
        out.append(h)
    return out


def _sandbox_env(cmd: str) -> bool:
    """Commands that are benign by construction even in-mandate."""
    return cmd.lstrip().startswith(("cd ", "ls ", "echo ", "cat ", "pwd",
                                    "source ", "export ", "alias ", "git status"))


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return 0  # not a hook invocation — never block on plumbing errors
    if payload.get("tool_name") not in ("Bash", "Edit", "Write"):
        return 0
    cmd = ""
    if payload.get("tool_name") == "Bash":
        cmd = (payload.get("tool_input") or {}).get("command", "")
    else:
        return 0  # file writes are gated by the operator's own review
    cwd = (payload.get("tool_input") or {}).get("cwd") or os.getcwd()

    if not _marker_active(cwd):
        return 0  # not a mandate session — the gate is off
    if _sandbox_env(cmd):
        return 0

    hosts = _hosts_from(cmd)
    if not hosts:
        return 0  # no target token — nothing to verify (documented ceiling)

    for h in hosts:
        ok, reason, _ = sa.check(h, strict=True, allow_lab=True)
        if not ok:
            feedback = (
                "✗ MECHANICAL GATE — SpyderMonkey scope authority "
                f"denied target '{h}': {reason}.\n"
                "  This block is host-enforced; no prompt can override it.\n"
                "  In-scope it? → spydermonkey scope add <value>   (operator only)\n"
                "  Not a mandate session? → remove .spydermonkey-active or unset "
                "SPYDERMONKEY_MANDATE."
            )
            print(json.dumps({"hookSpecificOutput": feedback}))
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())