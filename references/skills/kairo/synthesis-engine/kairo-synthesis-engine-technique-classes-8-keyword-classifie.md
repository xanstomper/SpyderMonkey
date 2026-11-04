# Technique classes (8, keyword-classified at ingest)

- source canon: `kairo/synthesis-engine.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
