# L5 — TIMELINE — chain composition

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-l5-timeline.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Audit | Synthesis |
|---|---|
| engagement pacing patterns (burst = fingerprint) | bursts chunked + paused (same discipline as noise budgets) |
| time-of-day correlation with the operator's routine | schedule around it; the vantage's timezone is the opsec timezone |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
