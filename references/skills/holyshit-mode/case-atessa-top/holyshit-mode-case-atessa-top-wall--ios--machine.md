# Wall — ios / machine

- source canon: `holyshit-mode/case-atessa-top.md`
- base technique: `holyshit-mode-case-atessa-top-wall.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **ios** · auth **machine** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Signup + login captcha-gated server-side (operator declined account creation pre-auth; later supplied key). Remaining authed follow-ups needing a SESSION COOKIE: voucher brute (`/api/vouchers/redeem` + preview oracle), credit-transfer IDOR (`/user/transfer-credits`), key IDOR (`/user/keys/{id}`), reseller RS escalation, mass-assignment JWT persistence. Quota reset 2026-10-07 00:00 UTC gates completion-plane abuse tests.

## Probe adjustment (ios × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
