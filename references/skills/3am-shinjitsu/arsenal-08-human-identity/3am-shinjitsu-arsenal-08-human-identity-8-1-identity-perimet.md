# 8.1 Identity perimeter map (score 65)

- source canon: `3am-shinjitsu/arsenal-08-human-identity.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- Which IdP: SSO portal fingerprint from the login page (Azure/Okta/Auth0/Google WS-Fed
  signatures, realm/return_to/ticket params captured BEFORE any form interaction).
- Password-reset flow exposure: information-leak class only — does the flow distinguish
  registered vs unregistered (enumeration oracle)? Token TTL/single-use posture from ToS/docs.
- MFA posture: push-based (fatigue surface) vs number-matching vs FIDO — from public docs +
  login-page fingerprints.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
