# 2.7 Runtime-config bootstrap replay (score 75) — chain composition

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-7-runtime-config-bootstra.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- PATTERN: config-fetch call in bundle (`metadata?uuid=` with hardcoded default) → curl it unauth.
- CONFIRMED WHEN: feature flags, room lists, service domains, ops text ride it unauth; sibling
  `socket-token` mint = decode payload (TTL/aud/claims) — read the auth model, don't guess.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
