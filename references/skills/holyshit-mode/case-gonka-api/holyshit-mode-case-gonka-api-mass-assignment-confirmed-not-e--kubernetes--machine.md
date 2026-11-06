# Mass-assignment: confirmed, NOT exploitable (gate re-confirmed) — kubernetes / machine

- source canon: `holyshit-mode/case-gonka-api.md`
- base technique: `holyshit-mode-case-gonka-api-mass-assignment-confirmed-not-e.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **kubernetes** · auth **machine** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- `/auth/v1/signup` `data:{role:"admin",is_admin:true,balance:999999,tier:"enterprise"}`
  persists VERBATIM into `user_metadata`, survives email confirmation into the
  verified JWT. `app_metadata` stays clean (GoTrue protects it).
- Gate: PostgREST RLS ignores `user_metadata`; edge-function billing reads real
  `balances.credits_cents` — a 2000-token completion deducted −0.002 from the
  20¢ balance. No backend authorizes on `user_metadata.role`. Score ~55
  hardening note, not a holy shit.

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
