# The block — origin app-layer, per-IP, edge-cache passthrough (reusable discriminator) — chain composition

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-the-block-origin-app.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Every dynamic api route: `403 {"error":"Blocked"}` + `retry-after: 86309` (~24h), Caddy origin. Same from curl AND browser stack. Includes `/oauth/login/kick` — login impossible from blocked IP, so "just use my account" does NOT fix an IP ban; say so before asking the user to log in.
- **Block is per-IP, NOT geo/datacenter-detectable**: egress was Comcast residential (67.163.x, ipify+ipinfo verified) and still blocked — likely burned by earlier recon volume. Don't assume "residential IP = unblocked"; check `mullvad status` etc. BEFORE promising the VPN path (this session's Mullvad device was revoked, no funds → dead fallback).
- **Cache discrimination is per-URL, learned empirically**: `/public/gambling/config` HIT even with fresh `last-modified`; `?cb=$RANDOM` on the same path → BYPASS → 403. Bare leaderboards 403 (not cached), bare stocks HIT. No header combo (Origin/Referer/UA/HTTP2/HEAD) changed the outcome — it's CDN cache-state, not request shape. Test each route bare AND busted; don't generalize one route's cacheability.
- **Cached GETs pass**: bare no-query URLs served `cf-cache-status: HIT` before origin sees the request — `/public/gambling/config`, `/public/stock-market/stocks` (bare), `/public/leaderboards` (bare), `/public/stock-market/stocks/{externalId}` all leaked full data.
- **Any query string busts cache → origin → Blocked** (`?page=1`, `?category=...`).
- Discriminator vs CF block: app-layer = JSON body + origin server header + Retry-After; CF block = HTML 1020 + ray ID. Don't hammer a 24h Retry-After — one confirm, move on.
- **Sibling-host escape**: same backend data served unblocked from `event-public` host. Map every host feeding one app before declaring a wall.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
