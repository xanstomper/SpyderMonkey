# 8.1 Identity perimeter map (score 65) — iac / root

- source canon: `3am-shinjitsu/arsenal-08-human-identity.md`
- base technique: `3am-shinjitsu-arsenal-08-human-identity-8-1-identity-perimet.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iac** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: template/state files are the infrastructure inventory — read-only crown of the exposure
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- Which IdP: SSO portal fingerprint from the login page (Azure/Okta/Auth0/Google WS-Fed
  signatures, realm/return_to/ticket params captured BEFORE any form interaction).
- Password-reset flow exposure: information-leak class only — does the flow distinguish
  registered vs unregistered (enumeration oracle)? Token TTL/single-use posture from ToS/docs.
- MFA posture: push-based (fatigue surface) vs number-matching vs FIDO — from public docs +
  login-page fingerprints.

## Probe adjustment (iac × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
