# Technique classes (8, keyword-classified at ingest) — edge-node / high-priv

- source canon: `kairo/synthesis-engine.md`
- base technique: `kairo-synthesis-engine-technique-classes-8-keyword-classifie.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **edge-node** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (edge-node × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
