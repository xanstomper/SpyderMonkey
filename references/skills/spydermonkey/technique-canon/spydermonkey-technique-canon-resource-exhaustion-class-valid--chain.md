# Resource-exhaustion class (validation-only) — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-resource-exhaustion-class-valid.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Unbounded expensive endpoints (report generation, image resize) — characterize as the class with ONE request's measured cost delta, never a sustained drain.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
