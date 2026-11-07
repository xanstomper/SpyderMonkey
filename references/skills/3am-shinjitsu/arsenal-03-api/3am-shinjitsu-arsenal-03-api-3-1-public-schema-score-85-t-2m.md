# 3.1 Public schema (score 85, T≈2min)

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- FastAPI: `{"detail":...}` 404/405 fingerprint → `/openapi.json /docs /redoc` = full route map.
- ReadMe.io-hosted docs: fetch `/llms.txt` → per-page OpenAPI blocks = complete schema free
  (see `api-schema-mining.md`).
- CONFIRMED WHEN: full route+schema map with zero guessed paths.
- FP: `/openapi.json` behind auth returns 401 JSON — note, don't conclude absent.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
