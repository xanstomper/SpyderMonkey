# 4.7 SSO anchors (score 65, fingerprint-first)

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

- SAML: signature wrapping, assertion replay, audience restriction. OIDC: nonce/state
  validation, token-exchange abuse, consent-phishing surface. SCIM: over-scoped tokens,
  bulk enumeration. LDAP/Kerberos classes from vector-matrix N (owned infra).
- Capture the FULL external-IdP authorize URL before touching the form (realm/return_to/
  ticket, loginN infra series).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
