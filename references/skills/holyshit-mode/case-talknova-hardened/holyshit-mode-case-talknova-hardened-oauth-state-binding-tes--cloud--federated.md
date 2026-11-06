# OAuth state-binding test (5 curls, decisive) — cloud / federated

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-oauth-state-binding-tes.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **cloud** · auth **federated** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

1. GET `/api/auth/google/start?attempt=x1` → capture state cookie A.
2. GET start again → cookie B. Then `callback?state=A&code=fake` with cookie B → hardened if `Invalid OAuth state`.
3. Matched cookie + fake code → expect token-exchange failure.
4. `returnTo=https://evil.com` on /start → hardened if Location still goes only to Google.
5. Callback with no cookie / no state → expect 400.

## Probe adjustment (cloud × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
