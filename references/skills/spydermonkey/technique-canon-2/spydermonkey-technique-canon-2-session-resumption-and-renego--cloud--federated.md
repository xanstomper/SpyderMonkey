# Session resumption and renegotiation posture — cloud / federated

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-session-resumption-and-renego.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **cloud** · auth **federated** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Resumption across IPs and insecure renegotiation accepted = posture findings. Decisive test: openssl -reconnect session-reuse behavior, renegotiation error class.

## Probe adjustment (cloud × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
