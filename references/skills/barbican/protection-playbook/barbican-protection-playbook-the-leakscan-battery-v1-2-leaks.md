# The leakscan battery (v1.2 — `leakscan`)

- source canon: `barbican/protection-playbook.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
