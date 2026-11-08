#!/bin/bash
# Deploy the SpyderMonkey agent carriers — run after every contract change.
# Idempotent. Covers: Claude Code command, OpenCode agent, Cline wrapper
# (reads the contract live — nothing to do).
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Claude Code: /spydermonkey command embeds the session contract
mkdir -p ~/.claude/commands
{ sed -n '1,7p' "$HERE/agents/claude-command.md"; echo; cat "$HERE/references/mandate-session.md"; } > /tmp/sm-claude-cmd.md
sed -i '8{/^$/d}' /tmp/sm-claude-cmd.md
cp /tmp/sm-claude-cmd.md ~/.claude/commands/spydermonkey.md
rm -f /tmp/sm-claude-cmd.md
echo "✓ ~/.claude/commands/spydermonkey.md (Claude Code /spydermonkey)"

# OpenCode: /spydermonkey primary agent embeds the session contract
mkdir -p ~/.config/opencode/agents
{
  echo "---"
  echo "description: 'SPYDERMONKEY engagement dispatcher (HolyShit family). Session-wide mandate - routes goals to the ten mandates, drives the real engines, family walls intact. Use /spydermonkey to activate.'"
  echo "mode: primary"
  echo "---"
  echo
  cat "$HERE/references/mandate-session.md"
} > ~/.config/opencode/agents/spydermonkey.md
echo "✓ ~/.config/opencode/agents/spydermonkey.md (OpenCode /spydermonkey)"

echo "✓ carriers at contract revision: $(grep 'Contract ID:' "$HERE/references/mandate-session.md" | cut -d' ' -f3)"
echo "done — restart opencode/claude sessions to pick up the new agent definition."