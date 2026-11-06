# 3.4 Mass-assignment (score 80) — cloud / machine

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-4-mass-assignment-score-80.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **cloud** · auth **machine** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- DECISIVE: signup/write with `data:{role:"admin",is_admin:true,tier:"enterprise",balance:999999}`.
- THE GATE (3 targets confirmed negative): persistence into `user_metadata`/JWT ≠ escalation.
  Exploitability = does ANY backend authorize on the planted key? Check the real table read +
  RLS `auth.jwt()->>'sub'` scoping + DTO discard. Persisted-but-untrusted = hardening note ~55.
- PostgREST UPDATE discriminator: 204 ≠ rows changed — send
  `Prefer: return=representation,count=exact`, read `content-range: */0` = ZERO rows. INSERT
  blocks = `42501`.

## Probe adjustment (cloud × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
