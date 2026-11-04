# 8.3 Vishing/sim-swap/MFA-fatigue EXPOSURE ratings (score 55, never executed) — dns / low-priv

- source canon: `3am-shinjitsu/arsenal-08-human-identity.md`
- base technique: `3am-shinjitsu-arsenal-08-human-identity-8-3-vishing-sim-swap.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- context: **dns** · auth **low-priv** · chain role **pivot**

## Context

- platform: record/cname surface — the domtake chain starts here
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Rated from artifacts only: which MFA method, whether office refs are public, SIM-portal
  exposure of the org (carrier domain in email headers is documentation, not targeting).
- MITRE anchors for the report: T1598/T1566/T1621/T1656 noted as EXPOSURE, not attempts.

## Probe adjustment (dns × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
