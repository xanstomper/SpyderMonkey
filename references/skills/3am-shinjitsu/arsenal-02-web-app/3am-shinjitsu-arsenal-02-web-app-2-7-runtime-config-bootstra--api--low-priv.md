# 2.7 Runtime-config bootstrap replay (score 75) — api / low-priv

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-7-runtime-config-bootstra.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **api** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- PATTERN: config-fetch call in bundle (`metadata?uuid=` with hardcoded default) → curl it unauth.
- CONFIRMED WHEN: feature flags, room lists, service domains, ops text ride it unauth; sibling
  `socket-token` mint = decode payload (TTL/aud/claims) — read the auth model, don't guess.

## Probe adjustment (api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
