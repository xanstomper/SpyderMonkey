# Technique classes (8, keyword-classified at ingest) — chain composition

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-technique-classes-8-keyword-classifie.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Class | Keywords | Flaw/Seam (3AM) | Craft class (undercroft) |
|---|---|---|---|
| BOUNDARY | org_id, tenant, workspace, plan, seat | 6/C | IDOR |
| REPLAY | webhook, replay, idempoten, callback, dedup | 5/B | STATE |
| STATEBYPASS | state, transition, workflow, approval | 5/B | STATE |
| MATH | refund, fee, rounding, precision, conversion, payout | 10/C | MATH |
| ENTITLEMENT | coupon, trial, promo, bonus, referral, claim | 1/C | IDOR |
| AUTHBYPASS | token, jwt, session, otp, auth, cookie | 1/C | OTHER |
| HWFLASH | firmware, uart, jtag, spi, flash, ota | 17/L | OTHER |
| HDRADIO | ble, rfid, nfc, radio, sdr, zigbee | 18/M | OTHER |

Unclassifiable findings default to AUTHBYPASS and are flagged for operator review.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
