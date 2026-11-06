# 3.3 IDOR structural scan (score 85) — chain composition

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-3-idor-structural-scan-score-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- From §3.2 shapes: every cross-user identifier (`walletId`, `ownerId`, `userId`, `accountId`).
- DECISIVE: operator's own two accounts (or one ephemeral self-account) — swap ONLY the id,
  keep the valid session. Cross-account read/write = CONFIRMED.
- Numeric-id ladders on admin routes: `/users/1` `/grants/1` unauth + low-priv (GET then
  PATCH as own-id). All 401/403 uniform = negative.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
