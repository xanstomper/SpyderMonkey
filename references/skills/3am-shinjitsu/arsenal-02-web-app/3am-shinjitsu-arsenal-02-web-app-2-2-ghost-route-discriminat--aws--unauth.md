# 2.2 Ghost-route discrimination (score 75 — kills false positives) — aws / unauth

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-2-ghost-route-discriminat.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **aws** · auth **unauth** · chain role **pivot**

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- RULE: status alone proves NOTHING on SPA/CDN deployments. Every path returns 200 text/html.
- REAL = `application/json` (or `text/event-stream`, `application/msgpack`).
- Cloudflare Access wall: `Sign in · Cloudflare Access` title on EVERY path incl. JSON APIs
  = WALL, not response. Record WALL for the phase; verdicts from a gated host are junk.
- Sensitive-file soft-404: identical `DOCTYPE html / charset=utf8 / viewport` 200 = absent.

## Probe adjustment (aws × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
