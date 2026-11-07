# The leakscan battery (v1.2 — `leakscan`) — container / high-priv

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-the-leakscan-battery-v1-2-leaks.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **container** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

| Pattern | Class | Severity | Why it matters |
|---|---|---|---|
| `Name <email>` | identity | HIGH | full operator attribution in one string |
| raw email | identity | HIGH | personal email = personal life in artifacts |
| `AKIA…` / `sk-…` / `ghp_…` / `xox…-…` / `-----BEGIN` | secret | HIGH | live credentials in the compartment |
| `/home/<user>/…` | path | MEDIUM | username + machine layout leak |
| `<host>.local` / `.ts.net` | identity | MEDIUM | machine hostname = routable identity |
| `AI_*` / `AGENT_*` env markers | tooling | MEDIUM | proves an agent ran it — de-anonymizes the operator class |
| RFC1918 private IPs | infra | LOW | network topology hints |

- Scope: default = the target's opsec + campaign dirs; `--deep` = the whole
  `~/.redteam/` canon. Snippets are REDACTED in output — the scan never prints a
  full secret back.
- HIGH hits demand action: `sanitize --write` → re-posture → re-scan. HIGH count
  zero is the only acceptable pre-assault state.
- `check --target T` runs the trail/alias summary inline — the pre-flight is the
  whole shield in four lines.

## Probe adjustment (container × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
