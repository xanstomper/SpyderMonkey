# 3.11 Business-logic cells (score 65-85, owned/self-account only) — chain composition

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-11-business-logic-cells-score.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Race: parallel redeem/withdraw/transfer on ONE connection (single-packet) — operator's own
  funds only, bounded N=5. Payment: negative/zero/decimal price, currency confusion, coupon
  stacking, post-hoc price edit — ONE attempt each on self-account. Subscription: downgrade-
  with-features; trial re-spam = FORBIDDEN (third-party email abuse).
- CONFIRMED WHEN: balance/entitlement mutation on the self-account. Revert-map entry per test.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
