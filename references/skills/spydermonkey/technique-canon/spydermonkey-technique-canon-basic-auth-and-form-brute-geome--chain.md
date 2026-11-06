# Basic-auth and form brute geometry — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-basic-auth-and-form-brute-geome.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The brute class is a RATE problem before it is a CREDENTIAL problem: lockout windows, per-IP vs per-account throttling, and response-length uniformity decide feasibility. Decisive test: 5 wrong-password requests on one account, one on the next — a lockout on the first and none on the second means per-account throttling with per-IP rotation potential. Register the geometry (window, scope, response delta), never a harvested credential.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
