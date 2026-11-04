# 2.11 Injected-input classes (score per-cell, from vector-matrix B) — web-app / unauth

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-11-injected-input-classes.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **web-app** · auth **unauth** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- One decisive probe per class, on ONE parameter, once: SQLi (error/boolean/time), NoSQLi
  (`{"$ne":null}` in JSON fields), SSTI (`{{7*7}}` in rendered/report fields), path traversal
  (`../%2e%2e` on filename/range/zip-entry), open redirect (`//evil`, `/\evil`, `@evil`),
  prototype pollution (`__proto__` in JSON merges), XXE (OOB DNS canary only).
- CONFIRMED WHEN: oracle in response (diff, error, canary callback). No spraying: one param,
  one class, one probe; a twice-failed approach is dead.
- CSV/formula injection in export features (`=cmd`); webhooks unsigned/replayable.

## Probe adjustment (web-app × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
