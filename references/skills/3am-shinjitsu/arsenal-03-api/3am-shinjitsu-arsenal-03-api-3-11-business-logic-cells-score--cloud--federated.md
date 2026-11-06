# 3.11 Business-logic cells (score 65-85, owned/self-account only) — cloud / federated

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-11-business-logic-cells-score.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- context: **cloud** · auth **federated** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- Race: parallel redeem/withdraw/transfer on ONE connection (single-packet) — operator's own
  funds only, bounded N=5. Payment: negative/zero/decimal price, currency confusion, coupon
  stacking, post-hoc price edit — ONE attempt each on self-account. Subscription: downgrade-
  with-features; trial re-spam = FORBIDDEN (third-party email abuse).
- CONFIRMED WHEN: balance/entitlement mutation on the self-account. Revert-map entry per test.

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
