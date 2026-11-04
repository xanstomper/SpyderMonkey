# N. IDENTITY / AUTH INFRA — windows / low-priv

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-n-identity-auth-infra.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **windows** · auth **low-priv** · chain role **pivot**

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- SAML: XML signature wrapping, assertion replay, audience restriction bypass
- OIDC: nonce/state validation, token exchange abuse, consent phishing surface
- LDAP: anonymous bind, injection in search filters, credential caching on clients
- Kerberos: delegation abuse (unconstrained/constrained/RBCD), ticket lifetime policy
- SCIM: over-scoped provisioning tokens, bulk-user enumeration via SCIM endpoints
- FIDO/WebAuthn: origin validation, attestation bypass, resident-key extraction

## Probe adjustment (windows × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
