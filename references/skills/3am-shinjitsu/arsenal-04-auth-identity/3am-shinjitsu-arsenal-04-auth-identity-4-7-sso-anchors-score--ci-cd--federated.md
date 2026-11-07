# 4.7 SSO anchors (score 65, fingerprint-first) — ci-cd / federated

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- base technique: `3am-shinjitsu-arsenal-04-auth-identity-4-7-sso-anchors-score.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **ci-cd** · auth **federated** · chain role **entry**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- SAML: signature wrapping, assertion replay, audience restriction. OIDC: nonce/state
  validation, token-exchange abuse, consent-phishing surface. SCIM: over-scoped tokens,
  bulk enumeration. LDAP/Kerberos classes from vector-matrix N (owned infra).
- Capture the FULL external-IdP authorize URL before touching the form (realm/return_to/
  ticket, loginN infra series).

## Probe adjustment (ci-cd × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
