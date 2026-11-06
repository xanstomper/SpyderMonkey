# Error-code vocabulary = the API feature map — mobile-api / federated

- source canon: `holyshit-mode/client-bundle-source-study.md`
- base technique: `holyshit-mode-client-bundle-source-study-error-code-vocabula.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mobile-api** · auth **federated** · chain role **pivot**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Grep all chunks for the platform's error-code prefix (e.g. `er_[a-z0-9_]+`) and sort: every
`er_<feature>_<failure>` names an endpoint family that may not appear in any fetch site
(kick, telegram, sol, kyc/persona, vault+2fa, raffles, seeds, party). 150+ codes = a full
hidden-surface inventory; score only after probing, but USE the map to pick probe targets
(and to spot auth methods the current UI hides, e.g. sol-wallet sign-in codes without a UI
button).

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
