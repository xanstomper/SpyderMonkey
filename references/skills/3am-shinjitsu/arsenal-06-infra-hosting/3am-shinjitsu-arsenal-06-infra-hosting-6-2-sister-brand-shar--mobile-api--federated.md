# 6.2 Sister-brand shared infra (score 80) — mobile-api / federated

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- base technique: `3am-shinjitsu-arsenal-06-infra-hosting-6-2-sister-brand-shar.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **mobile-api** · auth **federated** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- Identical CDN IPs + VERBATIM error envelopes across sister brands = shared backend.
- Ledger the cross-brand session-replay hypothesis (cookie domain scope, shared `state`).
- Sister-brand CT logs surface staging hosts (`stagsrv` class) and dangling routes.
- Family orbit = the compromisable surface when the core is hardened (gamdom lesson).

## Probe adjustment (mobile-api × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
