# U05 Identity & access — ios / service

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u05-identity-access.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **ios** · auth **service** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- [ ] SSO/OAuth/OIDC/SAML redirect, state, nonce, audience, and callback binding reviewed
- [ ] Password reset/MFA/recovery and session invalidation paths reviewed
- [ ] Privileged roles, service accounts, secrets rotation, and break-glass access audited
- [ ] Least-privilege and conditional access policies evaluated
- [ ] Token storage, scope, expiry, refresh, and revocation checked

## Probe adjustment (ios × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
