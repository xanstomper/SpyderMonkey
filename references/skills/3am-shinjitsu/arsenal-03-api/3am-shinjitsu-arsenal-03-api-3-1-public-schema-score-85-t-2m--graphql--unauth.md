# 3.1 Public schema (score 85, T≈2min) — graphql / unauth

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-1-public-schema-score-85-t-2m.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **graphql** · auth **unauth** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- FastAPI: `{"detail":...}` 404/405 fingerprint → `/openapi.json /docs /redoc` = full route map.
- ReadMe.io-hosted docs: fetch `/llms.txt` → per-page OpenAPI blocks = complete schema free
  (see `api-schema-mining.md`).
- CONFIRMED WHEN: full route+schema map with zero guessed paths.
- FP: `/openapi.json` behind auth returns 401 JSON — note, don't conclude absent.

## Probe adjustment (graphql × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
