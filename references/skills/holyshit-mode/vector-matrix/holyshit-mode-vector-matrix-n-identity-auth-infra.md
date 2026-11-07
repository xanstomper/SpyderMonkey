# N. IDENTITY / AUTH INFRA

- source canon: `holyshit-mode/vector-matrix.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- SAML: XML signature wrapping, assertion replay, audience restriction bypass
- OIDC: nonce/state validation, token exchange abuse, consent phishing surface
- LDAP: anonymous bind, injection in search filters, credential caching on clients
- Kerberos: delegation abuse (unconstrained/constrained/RBCD), ticket lifetime policy
- SCIM: over-scoped provisioning tokens, bulk-user enumeration via SCIM endpoints
- FIDO/WebAuthn: origin validation, attestation bypass, resident-key extraction

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
