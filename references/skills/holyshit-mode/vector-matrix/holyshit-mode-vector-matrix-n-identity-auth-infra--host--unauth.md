# N. IDENTITY / AUTH INFRA — host / unauth

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-n-identity-auth-infra.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **host** · auth **unauth** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- SAML: XML signature wrapping, assertion replay, audience restriction bypass
- OIDC: nonce/state validation, token exchange abuse, consent phishing surface
- LDAP: anonymous bind, injection in search filters, credential caching on clients
- Kerberos: delegation abuse (unconstrained/constrained/RBCD), ticket lifetime policy
- SCIM: over-scoped provisioning tokens, bulk-user enumeration via SCIM endpoints
- FIDO/WebAuthn: origin validation, attestation bypass, resident-key extraction

## Probe adjustment (host × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
