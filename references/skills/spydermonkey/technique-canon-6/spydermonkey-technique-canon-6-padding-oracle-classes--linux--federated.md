# Padding-oracle classes — linux / federated

- source canon: `spydermonkey/technique-canon-6.md`
- base technique: `spydermonkey-technique-canon-6-padding-oracle-classes.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **linux** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

Distinguishable padding errors (status/length/timing) on ciphertext-bearing params — the lab replica proves the oracle shape; live characterization is ONE probe pair against your own ciphertext. The Manger/Vaudenay recovery itself is never executed live (no-gain).

## Probe adjustment (linux × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
