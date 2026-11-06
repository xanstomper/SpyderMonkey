# 8.3 Vishing/sim-swap/MFA-fatigue EXPOSURE ratings (score 55, never executed) — mail / machine

- source canon: `3am-shinjitsu/arsenal-08-human-identity.md`
- base technique: `3am-shinjitsu-arsenal-08-human-identity-8-3-vishing-sim-swap.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- context: **mail** · auth **machine** · chain role **pivot**

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Rated from artifacts only: which MFA method, whether office refs are public, SIM-portal
  exposure of the org (carrier domain in email headers is documentation, not targeting).
- MITRE anchors for the report: T1598/T1566/T1621/T1656 noted as EXPOSURE, not attempts.

## Probe adjustment (mail × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
