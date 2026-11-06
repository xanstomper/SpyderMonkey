# 2.5 Source maps (score 90 when present)

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-04

## The technique

- DECISIVE: append `.map` to every fetched bundle/chunk; HTTP 200 + JSON = full source recovery.
- CONFIRMED WHEN: original TS/JS with comments, server-only constants, internal endpoints.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
