# 3.12 Public-endpoint PII sweep (score 80 — easy HIGH wins live here) — chain composition

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-12-public-endpoint-pii-sweep-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- SET: `/api/leaderboard/*`, `/api/health`, `/api/models/status`, `/api/catalog`,
  `/api/version`, `/api/ping`, `/profile/{username}/public`-shaped, bet feeds (`/ws/user/bets/live`).
- CONFIRMED: cross-user PII, internal UUIDs + registration-ms + authRole alongside public
  fields, per-user FINANCIALS (deposits/withdrawals/per-game profit) + username-enumeration
  oracle (200/404/422).
- Boolean payload flags lie until read at the CONSUMER — semantics live at the use site.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
