# REPLAY — webhook, replay, idempoten, callback, dedup — chain composition

- source canon: `kairo/technique-classes.md`
- base technique: `kairo-technique-classes-replay-webhook-replay-idempoten-call.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- REPLAY
- webhook, replay, idempoten, callback, dedup
- 5/B
- STATE

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
