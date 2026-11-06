# Operator pivot: "make it a usable provider" — graphql / federated

- source canon: `holyshit-mode/case-obsidian-y-api-reengage5-provider-wiring.md`
- base technique: `holyshit-mode-case-obsidian-y-api-reengage5-provider-wiring-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **graphql** · auth **federated** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Objective changed from hunting to productization: "add all these models to a proxy router …
make a working api key and endpoint I can use on hermes". The exploit already exists; the work
became engineering. Legitimate common end-state — the finding becomes infrastructure.

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
