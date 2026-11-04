# The leakscan battery (v1.2 — `leakscan`) — chain composition

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-the-leakscan-battery-v1-2-leaks.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
