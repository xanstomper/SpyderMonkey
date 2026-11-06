# OAuth code interception (redirect_uri looseness) — ci-cd / federated

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-oauth-code-interception-redirec.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **ci-cd** · auth **federated** · chain role **final**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

A permissive redirect_uri validation (prefix match, wildcard subdomain, open redirect chained) makes the authorization code interceptable. Decisive test: redirect_uri=https://in-scope.host.evil.example — accepted or rejected by the AS; if accepted, the code arrives at your host. The finding is the validation looseness class, proven by one redirect.

## Probe adjustment (ci-cd × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
