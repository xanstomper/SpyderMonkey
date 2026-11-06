# Password reset token reuse and non-expiry — kubernetes / machine

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-password-reset-token-reuse-and-.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **kubernetes** · auth **machine** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

The reset flow that accepts the same token twice (or after password change) fails single-use semantics. Decisive test: request a reset, consume it, replay it — a second 200 (vs 400/410) is the class. Crown: token TTL and whether the OLD password still works after reset.

## Probe adjustment (kubernetes × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
