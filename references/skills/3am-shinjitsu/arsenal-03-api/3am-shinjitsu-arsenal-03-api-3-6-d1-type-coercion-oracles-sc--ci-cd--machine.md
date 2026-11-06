# 3.6 D1 / type-coercion oracles (score 70) — ci-cd / machine

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-6-d1-type-coercion-oracles-sc.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **ci-cd** · auth **machine** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- D1: JSON object in a string field → `500 D1_TYPE_ERROR ... '[object Object]'` = engine +
  no type-layer sanitization. Variants: `{}`, `[]`, `null`, `true`, `0`. Limiter will lock
  (5/5min class) — accept lockout as negative, document the oracle.
- Generic: object-where-string-expected on every validated endpoint; framework error codes
  name the layer.

## Probe adjustment (ci-cd × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
