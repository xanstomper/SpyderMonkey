# OTP multi-submit race — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-otp-multi-submit-race.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The verify endpoint that accepts concurrent submits can validate one OTP across N sessions. Decisive test: same OTP payload fanned to 5 parallel requests with distinct session tokens — >1 success = the class. The race is measured in the lab replica first (dojo replica reproduces the semantics).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
