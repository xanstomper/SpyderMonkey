# Reset host-header poisoning — kubernetes / federated

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-reset-host-header-poisoning.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **kubernetes** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

The reset email's link built from the Host header (or X-Forwarded-Host) redirects the token to attacker infrastructure. Decisive test: request a reset for YOUR OWN account with Host=your.domain, read the emailed link's host — proof is in your own inbox, never a third party's.

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
