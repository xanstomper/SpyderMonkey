# SRI/CSP posture on third-party integrations — container / federated

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-sri-csp-posture-on-third-part.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- context: **container** · auth **federated** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Script integrations without SRI + CSP none = the injection amplifier (SPY-056 class). Decisive test: header posture + script-tag audit of the live page — the posture row is the finding.

## Probe adjustment (container × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
