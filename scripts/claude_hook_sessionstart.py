#!/usr/bin/env python3
"""SpyderMonkey SessionStart hook — mechanical mandate injection.

Claude Code SessionStart: when a mandate marker is active (env
SPYDERMONKEY_MANDATE=1, `.spydermonkey-active` in the session CWD, or a CWD
inside ~/.redteam/campaigns/<name>/), the ambient takeover brief
(agents/AGENTS.md) is injected into the session context at start — the
takeover engages without anyone typing the trigger and without relying on the
model finding the contract itself.

Non-mandate sessions: pure pass-through (no output, exit 0).

Claude Code hook contract: JSON payload on stdin; exit 0 always (SessionStart
cannot block); hookSpecificOutput is added to the session context.
"""

import json
import os
import sys
from pathlib import Path

SPYDERMONKEY_REPO = Path(__file__).resolve().parent.parent


def _marker_active(payload: dict) -> bool:
    if os.environ.get("SPYDERMONKEY_MANDATE") == "1":
        return True
    cwd = (payload.get("session") or {}).get("cwd") or os.getcwd()
    if (Path(cwd) / ".spydermonkey-active").exists():
        return True
    try:
        sys.path.insert(0, str(SPYDERMONKEY_REPO / "scripts"))
        import scope_authority as sa
        camp = sa.campaigns_root().resolve()
        return camp in Path(cwd).resolve().parents
    except Exception:
        return False


def _brief() -> str:
    p = SPYDERMONKEY_REPO / "agents" / "AGENTS.md"
    if not p.exists():
        return ""
    text = p.read_text(encoding="utf-8")
    start = text.find("---8<--- AMBIENT TAKEOVER")
    end = text.find("---8<--- END AMBIENT TAKEOVER")
    if start == -1 or end == -1:
        return text
    return text[start:end + len("---8<--- END AMBIENT TAKEOVER ---8<---")]


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return 0
    if not _marker_active(payload):
        return 0
    brief = _brief()
    if not brief:
        return 0
    print(json.dumps({"hookSpecificOutput": brief}))
    return 0


if __name__ == "__main__":
    sys.exit(main())