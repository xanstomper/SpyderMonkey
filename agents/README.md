# SPYDERMONKEY — any agent, 60 seconds

The family ships as a **mandate contract**, not a chatbot. Any LLM agent
(Claude Code, OpenCode, Cline, Codex, Hermes, Gemini CLI, a raw API loop)
operates under the same walls in one step.

## The walls (non-negotiable, machine-checked)

1. scope-gated: every live probe passes the shared scope authority (`scope.json`) — out-of-estate is an rc=1 refusal, not a judgment call
2. zero documents — the operator's identity never enters engagement data
3. validation-only + NO-GAIN — proofs, never persistence; findings priced, never exfiltrated
4. documented-PoC classes only — novel instances, never novel weapon classes
5. evidence-first: `baseline → attack → diff` or the finding downgrades to hypothesis

## Adopt per agent

| Agent | Step |
|---|---|
| Claude Code | `cp agents/claude-command.md ~/.claude/commands/spydermonkey.md` → `/spydermonkey` |
| OpenCode | paste `agents/AGENT.md` as the agent's system prompt (or register the file as a custom agent) |
| Cline / Codex / any CLI | first message = full contents of `agents/AGENT.md` |
| Hermes | the skill loads from `SKILL.md`; the session contract is `references/mandate-session.md` |
| raw API loop | `agents/AGENT.md` as the system prompt; drive `scripts/spydermonkey.py` with the kernel loop |

**After every contract change, re-deploy the carriers**: `./agents/deploy.sh`
(re-writes `~/.claude/commands/spydermonkey.md` and
`~/.config/opencode/agents/spydermonkey.md` from the current
`references/mandate-session.md`, idempotent). Both deployed agents pin the
contract ID — `grep 'Contract ID:'` tells you which revision a carrier ships.

## The one command that changes how the agent works

```bash
python3 scripts/spydermonkey.py loop --target YOURTARGET --agent-cmd 'your-agent -p'
```

The kernel becomes the agent's operating system: the planner emits ONE
state-driven directive at a time (exact argv + walls), the agent executes,
`absorb` validates the result through the same scope/ledger/evidence gates,
and the planner adapts. The agent stops improvising and starts running a
13-phase methodology with computed statuses, hash-chained evidence, and
purple-team mirroring of every confirmed attack.

## Fleet activation (real arsenal power)

```bash
python3 scripts/fleet_provision.py --emit   # on YOUR machine: emits the script
bash fleet-provision.sh                     # on a FLEET VM only — never the operator box
```

Activates 934/1,605 arsenal wrappers on a Kali fleet box (4 host packages +
71 direct installs + 853 wrappers riding with nmap/msf/nuclei/impacket).

## Verify everything

```bash
python3 scripts/spydermonkey.py selftest        # 30 checks, throwaway HOME
python3 scripts/leakscan.py                     # no engagement data ships
python3 scripts/spydermonkey.py verify          # live 3-gate proof
```
