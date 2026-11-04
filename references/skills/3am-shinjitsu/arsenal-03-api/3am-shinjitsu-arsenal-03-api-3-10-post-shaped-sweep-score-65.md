# 3.10 POST-shaped sweep (score 65)

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

- One pass: replay every discovered path with `-X POST -d '{}'`. 404 = method-bound ghost;
  200/201/400/500 = real POST surface. Log 500s as regressions.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
