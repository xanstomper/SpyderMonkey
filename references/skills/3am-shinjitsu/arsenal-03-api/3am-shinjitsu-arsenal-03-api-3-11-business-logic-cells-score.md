# 3.11 Business-logic cells (score 65-85, owned/self-account only)

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

- Race: parallel redeem/withdraw/transfer on ONE connection (single-packet) — operator's own
  funds only, bounded N=5. Payment: negative/zero/decimal price, currency confusion, coupon
  stacking, post-hoc price edit — ONE attempt each on self-account. Subscription: downgrade-
  with-features; trial re-spam = FORBIDDEN (third-party email abuse).
- CONFIRMED WHEN: balance/entitlement mutation on the self-account. Revert-map entry per test.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
