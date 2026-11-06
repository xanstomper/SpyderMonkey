# Wire-format replication recipe — chain composition

- source canon: `spydermonkey/technique-canon-7.md`
- base technique: `spydermonkey-technique-canon-7-wire-format-replication-recip.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Custom-binary protocol replication (the bc.game t1→/test/→t2 chain): mirror the app's packet TYPES exactly — mis-framing reads as a false gate (the SPY-069 lesson). Decisive test: handshake ACCEPTED with sid issued = protocol replication proven; wrong-ack ≠ server gate.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
