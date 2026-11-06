# Redis pub/sub and staging keys — graphql / federated

- source canon: `spydermonkey/technique-canon-4.md`
- base technique: `spydermonkey-technique-canon-4-redis-pub-sub-and-staging-key.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **graphql** · auth **federated** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Subscribe-to-internal-channels class (read-only listen on YOUR session channel) — the channel taxonomy is the finding.

## Probe adjustment (graphql × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
