# Withdrawal threshold and fee dodge — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-withdrawal-threshold-and-fee-do.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Min-withdrawal/fee logic enforced client-side (button disable, computed fee in JS) while the API accepts the raw request. Decisive test: submit the raw withdrawal POST for 1 cent below threshold on a test account — acceptance = the class; the payload is never the point, the server's acceptance is.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
