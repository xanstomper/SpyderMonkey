# 3.6 D1 / type-coercion oracles (score 70)

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-04

## The technique

- D1: JSON object in a string field → `500 D1_TYPE_ERROR ... '[object Object]'` = engine +
  no type-layer sanitization. Variants: `{}`, `[]`, `null`, `true`, `0`. Limiter will lock
  (5/5min class) — accept lockout as negative, document the oracle.
- Generic: object-where-string-expected on every validated endpoint; framework error codes
  name the layer.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
