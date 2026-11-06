# OTP brute window and rate geometry — chain composition

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-otp-brute-window-and-rate-geome.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

OTP validation with per-request cost < lockout threshold is enumerable (6-digit, 10 tries/lockout, no window reset = 1-in-10000 per lockout cycle). Decisive test: measure the exact counters — wrong-OTP responses until lock, lock TTL, and whether attempts decrement on resend. Register the arithmetic; never extract a live OTP.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
