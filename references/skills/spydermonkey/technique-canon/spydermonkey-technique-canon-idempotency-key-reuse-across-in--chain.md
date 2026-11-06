# Idempotency-key reuse across intents — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-idempotency-key-reuse-across-in.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The same idempotency key replayed for a DIFFERENT operation that the server accepts = cross-intent replay. Decisive test: key K on op-A then op-B — op-B returns op-A's cached result = the finding.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
