# Currency and price-mismatch substitution — kubernetes / federated

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-currency-and-price-mismatch-sub.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- context: **kubernetes** · auth **federated** · chain role **final**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

A client-supplied currency code (or price object) re-priced by the server at a stale rate is a rounding/repricing seam. Decisive test: switch currency mid-checkout and diff the converted line prices against the live FX the page displays — persistent mismatch = the finding.

## Probe adjustment (kubernetes × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
