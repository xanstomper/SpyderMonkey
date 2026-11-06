# 8.1 Identity perimeter map (score 65) — chain composition

- source canon: `3am-shinjitsu/arsenal-08-human-identity.md`
- base technique: `3am-shinjitsu-arsenal-08-human-identity-8-1-identity-perimet.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Which IdP: SSO portal fingerprint from the login page (Azure/Okta/Auth0/Google WS-Fed
  signatures, realm/return_to/ticket params captured BEFORE any form interaction).
- Password-reset flow exposure: information-leak class only — does the flow distinguish
  registered vs unregistered (enumeration oracle)? Token TTL/single-use posture from ToS/docs.
- MFA posture: push-based (fatigue surface) vs number-matching vs FIDO — from public docs +
  login-page fingerprints.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
