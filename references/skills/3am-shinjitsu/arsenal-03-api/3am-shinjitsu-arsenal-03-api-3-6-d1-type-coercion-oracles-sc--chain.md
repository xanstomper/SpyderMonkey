# 3.6 D1 / type-coercion oracles (score 70) — chain composition

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-6-d1-type-coercion-oracles-sc.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- D1: JSON object in a string field → `500 D1_TYPE_ERROR ... '[object Object]'` = engine +
  no type-layer sanitization. Variants: `{}`, `[]`, `null`, `true`, `0`. Limiter will lock
  (5/5min class) — accept lockout as negative, document the oracle.
- Generic: object-where-string-expected on every validated endpoint; framework error codes
  name the layer.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
