# 8.1 Identity perimeter map (score 65) — worker / high-priv

- source canon: `3am-shinjitsu/arsenal-08-human-identity.md`
- base technique: `3am-shinjitsu-arsenal-08-human-identity-8-1-identity-perimet.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **worker** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Which IdP: SSO portal fingerprint from the login page (Azure/Okta/Auth0/Google WS-Fed
  signatures, realm/return_to/ticket params captured BEFORE any form interaction).
- Password-reset flow exposure: information-leak class only — does the flow distinguish
  registered vs unregistered (enumeration oracle)? Token TTL/single-use posture from ToS/docs.
- MFA posture: push-based (fatigue surface) vs number-matching vs FIDO — from public docs +
  login-page fingerprints.

## Probe adjustment (worker × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
