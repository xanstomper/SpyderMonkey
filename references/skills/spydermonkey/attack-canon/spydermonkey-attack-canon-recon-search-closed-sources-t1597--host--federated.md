# Recon Search Closed Sources (T1597) — host / federated

- source canon: `spydermonkey/attack-canon.md`
- base technique: `spydermonkey-attack-canon-recon-search-closed-sources-t1597.md`
- bindings: **PTES-PE** · **CWE-522** · **ATT&CK T1555**
- context: **host** · auth **federated** · chain role **entry**

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- class: paid/registered intel sources for victim data
- probe: only what the operator legally holds credentials for
- wall: no credential use beyond declared scope; nothing purchased mid-run

## Probe adjustment (host × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
