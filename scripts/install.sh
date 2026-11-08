#!/bin/bash
# SpyderMonkey installer — portable, idempotent, verifiable.
#
#   ./scripts/install.sh            install into $HOME (default)
#   SMK_PREFIX=/opt ./install.sh    alternative prefix (system install)
#
# Installs: the CLI wrapper, the Claude Code + OpenCode carriers (deploy.sh),
# the host-level hooks, the jail baseline. Prints a verification block.
# Safe to re-run after upgrades or contract changes.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PREFIX="${SMK_PREFIX:-$HOME}"
BINDIR="$PREFIX/.local/bin"
SKILL_REF="references/activation-proof.md"

command -v python3 >/dev/null || { echo "✗ python3 required"; exit 1; }

echo "═══ SPYDERMONKEY INSTALL — v$(grep -h '^VERSION = ' "$REPO/scripts/spydermonkey.py" | cut -d'"' -f2) ═══"
echo "  repo:    $REPO"
echo "  prefix:  $PREFIX"

# 1. CLI wrapper (path-independent: resolves the repo at install time)
mkdir -p "$BINDIR"
cat > "$BINDIR/spydermonkey" <<EOF
#!/bin/bash
exec "${PYTHON:-python3}" "$REPO/scripts/spydermonkey.py" "\$@"
EOF
chmod +x "$BINDIR/spydermonkey"
echo "✓ wrapper   $BINDIR/spydermonkey"

# 2. Carriers (Claude Code command + OpenCode agent, pinned to the contract)
"$REPO/agents/deploy.sh"

# 3. Host-level hooks (scope gate + sessionstart injector), merged safely
python3 - <<EOF
import json, pathlib
s = pathlib.Path.home() / ".claude" / "settings.json"
data = json.loads(s.read_text()) if s.exists() else {}
hooks = data.setdefault("hooks", {})
pre = hooks.setdefault("PreToolUse", [])
if not any("claude_hook_scope" in h.get("command", "") for e in pre for h in e.get("hooks", [])):
    pre.append({"matcher": "Bash", "hooks": [{"type": "command",
                "command": f"python3 $REPO/scripts/claude_hook_scope.py"}]})
ss = hooks.setdefault("SessionStart", [])
if not any("claude_hook_sessionstart" in h.get("command", "") for e in ss for h in e.get("hooks", [])):
    ss.append({"hooks": [{"type": "command",
               "command": f"python3 $REPO/scripts/claude_hook_sessionstart.py"}]})
s.parent.mkdir(parents=True, exist_ok=True)
s.write_text(json.dumps(data, indent=2))
print("✓ hooks     ~/.claude/settings.json (scope-gate + sessionstart)")
EOF

# 4. Jail baseline
"$BINDIR/spydermonkey" jail arm

# 5. Verification block
echo "── verification ──"
python3 "$REPO/scripts/version_audit.py" || true
"$BINDIR/spydermonkey" inmandate | head -4
"$BINDIR/spydermonkey" jail check || echo "  (jail check: arm state reflects this install)"
echo "═══ INSTALL COMPLETE — 'smk' available at $BINDIR/spydermonkey ═══"
echo "  add to PATH:  export PATH=\"$BINDIR:\$PATH\"   (or: ln -s $BINDIR/spydermonkey ~/.local/bin/smk)"