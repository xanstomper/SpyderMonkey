# T+25 — auth plane (high-value first, ceiling 15 req) — chain composition

- source canon: `3am-shinjitsu/arsenal-index.md`
- base technique: `3am-shinjitsu-arsenal-index-t-25-auth-plane-high-value-first.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| # | Probe | Test | Confirmed-when |
|---|---|---|---|
| 22 | GoTrue settings | `curl -H 'apikey: <anon>' /auth/v1/settings /auth/v1/health` | providers, autoconfirm flags, version = full auth surface |
| 23 | OAuth state binding | 2× /start → state A,B; `callback?state=A&code=fake` with cookie B | `Invalid OAuth state` = hardened (negative, ledger it) |
| 24 | redirect_uri override | `curl -s -o /dev/null -w '%{redirect_url}' '/auth/v1/authorize?provider=discord&redirect_uri=https://evil.com/cb'` | Location carries attacker URI verbatim → live-intercept (`arsenal-04` §3.2) |
| 25 | Auth-chain rate sweep | 15-20 rapid garbage POSTs per auth endpoint, `-w '%{http_code}'` | zero 429 = brute surface open |
| 26 | WS handshake+frames | real frame exchange (socket+ssl), NOT curl 101 | CLOSE 1008 on first frame = gate works (negative) |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
