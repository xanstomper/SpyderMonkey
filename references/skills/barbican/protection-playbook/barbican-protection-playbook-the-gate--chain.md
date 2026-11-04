# The gate — chain composition

- source canon: `barbican/protection-playbook.md`
- base technique: `barbican-protection-playbook-the-gate.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

`posture` must exist before the family engages (`assess` warns; the operator owns
the go). At engagement end: `wipe`. Between: `sanitize` after every artifact-heavy
phase. The first layer never sleeps.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
