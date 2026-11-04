# 3.1 Public schema (score 85, T≈2min) — chain composition

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-1-public-schema-score-85-t-2m.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- FastAPI: `{"detail":...}` 404/405 fingerprint → `/openapi.json /docs /redoc` = full route map.
- ReadMe.io-hosted docs: fetch `/llms.txt` → per-page OpenAPI blocks = complete schema free
  (see `api-schema-mining.md`).
- CONFIRMED WHEN: full route+schema map with zero guessed paths.
- FP: `/openapi.json` behind auth returns 401 JSON — note, don't conclude absent.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
