# 6.2 Sister-brand shared infra (score 80) — api / unauth

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- base technique: `3am-shinjitsu-arsenal-06-infra-hosting-6-2-sister-brand-shar.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **api** · auth **unauth** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Identical CDN IPs + VERBATIM error envelopes across sister brands = shared backend.
- Ledger the cross-brand session-replay hypothesis (cookie domain scope, shared `state`).
- Sister-brand CT logs surface staging hosts (`stagsrv` class) and dangling routes.
- Family orbit = the compromisable surface when the core is hardened (gamdom lesson).

## Probe adjustment (api × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
