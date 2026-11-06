# 2.2 Ghost-route discrimination (score 75 — kills false positives) — azure / machine

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-2-ghost-route-discriminat.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **azure** · auth **machine** · chain role **pivot**

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- RULE: status alone proves NOTHING on SPA/CDN deployments. Every path returns 200 text/html.
- REAL = `application/json` (or `text/event-stream`, `application/msgpack`).
- Cloudflare Access wall: `Sign in · Cloudflare Access` title on EVERY path incl. JSON APIs
  = WALL, not response. Record WALL for the phase; verdicts from a gated host are junk.
- Sensitive-file soft-404: identical `DOCTYPE html / charset=utf8 / viewport` 200 = absent.

## Probe adjustment (azure × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
