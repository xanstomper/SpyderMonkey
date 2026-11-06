# Employee/artifact-string exposure (zero-document boundary) — kubernetes / federated

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-employee-artifact-string-expo.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **kubernetes** · auth **federated** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Public artifact strings (git emails, doc metadata) — barbican's protect/sanitize canon applied OFFENSIVELY as recon: what does the ESTATE leak about itself. Decisive test: the string source URL — each leak is a row. Zero-document rule: no people-targeting, estate-artifacts only.

## Probe adjustment (kubernetes × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
