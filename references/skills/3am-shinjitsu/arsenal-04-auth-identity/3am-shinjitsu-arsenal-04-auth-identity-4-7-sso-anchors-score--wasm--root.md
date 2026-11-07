# 4.7 SSO anchors (score 65, fingerprint-first) — wasm / root

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- base technique: `3am-shinjitsu-arsenal-04-auth-identity-4-7-sso-anchors-score.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **wasm** · auth **root** · chain role **entry**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- SAML: signature wrapping, assertion replay, audience restriction. OIDC: nonce/state
  validation, token-exchange abuse, consent-phishing surface. SCIM: over-scoped tokens,
  bulk enumeration. LDAP/Kerberos classes from vector-matrix N (owned infra).
- Capture the FULL external-IdP authorize URL before touching the form (realm/return_to/
  ticket, loginN infra series).

## Probe adjustment (wasm × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
