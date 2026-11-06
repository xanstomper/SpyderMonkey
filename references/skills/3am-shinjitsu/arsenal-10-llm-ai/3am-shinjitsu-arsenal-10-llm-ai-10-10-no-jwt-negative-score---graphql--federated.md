# 10.10 No-JWT negative (score 50 — stop chasing) — graphql / federated

- source canon: `3am-shinjitsu/arsenal-10-llm-ai.md`
- base technique: `3am-shinjitsu-arsenal-10-llm-ai-10-10-no-jwt-negative-score-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **graphql** · auth **federated** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- Uniform `invalid_api_key` for EVERY bearer/JWT/alg-none/Basic/key-prefix variant = NO JWT
  auth path exists. Log it. Pivot to server-side secret paths or closeout.

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
