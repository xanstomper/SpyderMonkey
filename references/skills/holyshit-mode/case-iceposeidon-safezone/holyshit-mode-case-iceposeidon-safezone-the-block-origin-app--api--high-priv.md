# The block — origin app-layer, per-IP, edge-cache passthrough (reusable discriminator) — api / high-priv

- source canon: `holyshit-mode/case-iceposeidon-safezone.md`
- base technique: `holyshit-mode-case-iceposeidon-safezone-the-block-origin-app.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **api** · auth **high-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Every dynamic api route: `403 {"error":"Blocked"}` + `retry-after: 86309` (~24h), Caddy origin. Same from curl AND browser stack. Includes `/oauth/login/kick` — login impossible from blocked IP, so "just use my account" does NOT fix an IP ban; say so before asking the user to log in.
- **Block is per-IP, NOT geo/datacenter-detectable**: egress was Comcast residential (67.163.x, ipify+ipinfo verified) and still blocked — likely burned by earlier recon volume. Don't assume "residential IP = unblocked"; check `mullvad status` etc. BEFORE promising the VPN path (this session's Mullvad device was revoked, no funds → dead fallback).
- **Cache discrimination is per-URL, learned empirically**: `/public/gambling/config` HIT even with fresh `last-modified`; `?cb=$RANDOM` on the same path → BYPASS → 403. Bare leaderboards 403 (not cached), bare stocks HIT. No header combo (Origin/Referer/UA/HTTP2/HEAD) changed the outcome — it's CDN cache-state, not request shape. Test each route bare AND busted; don't generalize one route's cacheability.
- **Cached GETs pass**: bare no-query URLs served `cf-cache-status: HIT` before origin sees the request — `/public/gambling/config`, `/public/stock-market/stocks` (bare), `/public/leaderboards` (bare), `/public/stock-market/stocks/{externalId}` all leaked full data.
- **Any query string busts cache → origin → Blocked** (`?page=1`, `?category=...`).
- Discriminator vs CF block: app-layer = JSON body + origin server header + Retry-After; CF block = HTML 1020 + ray ID. Don't hammer a 24h Retry-After — one confirm, move on.
- **Sibling-host escape**: same backend data served unblocked from `event-public` host. Map every host feeding one app before declaring a wall.

## Probe adjustment (api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
