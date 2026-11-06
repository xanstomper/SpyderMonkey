# 2.5 Source maps (score 90 when present) — ci-cd / unauth

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-5-source-maps-score-90-wh.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **ci-cd** · auth **unauth** · chain role **final**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- DECISIVE: append `.map` to every fetched bundle/chunk; HTTP 200 + JSON = full source recovery.
- CONFIRMED WHEN: original TS/JS with comments, server-only constants, internal endpoints.

## Probe adjustment (ci-cd × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
