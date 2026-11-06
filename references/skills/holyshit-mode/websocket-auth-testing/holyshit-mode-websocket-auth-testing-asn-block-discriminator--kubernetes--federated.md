# ASN-block discriminator (block page ≠ solvable challenge) — kubernetes / federated

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-asn-block-discriminator.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **kubernetes** · auth **federated** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

A 403 "Attention Required!" that PERSISTS for a real headless chromium while
`cdn-cgi/challenge-platform/...` assets return 200 is an ASN/datacenter block, not
a challenge — the JS runs, the wall stays. No header/TLS/cookie stack clears it; the
plane is reachable only from residential egress, which is a sanctioned-vantage
decision for the operator, never a home-IP technique. Record the class negative
with the discriminator evidence and move on.

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
