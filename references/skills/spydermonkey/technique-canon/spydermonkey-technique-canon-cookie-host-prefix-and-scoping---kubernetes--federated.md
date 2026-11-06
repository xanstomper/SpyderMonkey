# Cookie __Host- prefix and scoping regressions — kubernetes / federated

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-cookie-host-prefix-and-scoping-.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **kubernetes** · auth **federated** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Missing `__Host-`, missing Secure, or Domain=.parent leaves cookies portable across sibling hosts. Decisive test: set a cookie on sub.in-scope.host and read it from sibling.in-scope.host over HTTPS — cross-subdomain readability is the finding.

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
