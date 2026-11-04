# 2026-11-02 re-engage (Vermes VM vantage): sockets, PF verification, region wall

- source canon: `holyshit-mode/case-duelbits-com.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

Full client decode from the CURRENT build (`index-CW30_Dqt.js` era, rolldown-vite, 416 chunks):

- **Web3 flow verbatim** (`web3-sign-in-*.js`): `POST {domain.token}/web3/message/?publicAddress=<addr>`
  (no headers/body) → `.json().message`; `personal_sign([utf8ToHex(msg), addr])`; state =
  `JSON.parse(url.state||'{}')` through `Xb` = **pure passthrough, NO whitelist** → truthy keys
  become BOTH the auth URL query AND body spread: `POST {domain.token}/web3?${qs}` body
  `{address, signature, ...state}`; response must be `{access, refresh, user}`. APIConfig:
  prod oAuth = switchflips.com; **duelbits.bet config self-labels `duelbits.net`** (their bug).
- **`POST /auth/token?scope=X` mints RS256 JWTs UNAUTH for ANY scope** — sub=admin/mod/internal/
  system all sign (30s TTL, aud=duelbits.com, `id`=stable per-session hash). ws+gs sockets accept
  any sub. No privilege gate at mint; no admin channel in the public client.
- **`GET /ws/user/bets/live` = 200 UNAUTH cross-user feed** (all/large/lucky/wins): displayName,
  internal UUID, registered(ms), level, verified, authRole, bet/win/game. The /ws socket streams
  the same as `bet`/`win` events live (partial user:null anonymization). Config siblings 404;
  `/ws/config` clean.
- **PF verified CORRECT (high-coverage negative):** roulette daily seeds `sha256(seed)==hash`
  49/49 closed periods; crash seeds are a REVERSE chain (`sha256(seed[N+1])==seed[N]` 99/99 —
  safe direction, future = preimage). Live-period record bug: seed==hash in both fields until
  reveal (cosmetic/verification-flow bug, no prediction gain — derive outcomes from the real
  seed, published only after close).
- **Region wall proven, not assumed:** Oracle VM geolocates DE → `/auth/web3` 403 on every
  signature/casing/state variant (ws pushes `blocked:{reason:region_page,location:de}`); missing
  geo fields → unhandled 500 (geo preflight crashes pre-consumption). Dev/staging/canary auth
  APIs = CF Access. The queued replay/binding/mass-assignment tests REQUIRE a residential
  unrestricted vantage (operator browser). Challenge layer: rotates per fetch, zero validation
  (`zzzz` → 201), no cookies, no oracle at message layer.
- **Ops lessons:** /dev/shm is noexec on OL9 (venv on disk, artifacts in RAM tmpfs);
  WAF pacing 3.5-6.5s held on API paths while HTML paths challenge on partial headers — full
  spoof stack is mandatory; socket.io polling needs strict POST→single-long-GET alternation or
  the sid dies (`Session ID unknown`); kit = `~/holyshit-mode/scripts/duel_kit.py` (phases:
  vantage/bundle/determinism/oracle/auth/replay/binding/state_forward/postauth_oracle).

### 2026-11-02 exploit round: minted-Bearer bypass + room authz + full-spectrum sweep (all negative on compromise)

- **Minted-token bearer bypass: HELD.** `/ws/user/bets/my`, `/ws/games/keno/history`,
  `/ws/games/hilo/history`, `/ws/user/profile`, `/ws/user/transactions` all 403 with
  minted `sub=user/admin/mod/system` JWTs in EVERY delivery variant (Bearer, `?token=`,
  cookie). The /ws guard requires real wallet-login claims — the scope mint is inert on HTTP.
- **Room authz: HOLDS.** Real vocabulary: `user:bet`/`user:bonus`/`user:notification`/
  `user:update` personal channels, `internal:` = sportsbook CONTEST prefix (not admin),
  `game:${id}`, `tournament:*`. Joining `internal:*` + `user:<harvested-uuid>` with elevated
  subs returns only the global feed — silent empty joins = server-side membership check.
- **16 unauth-200 endpoints mapped** (`endpoint_probe.json`): betradar odds/event feeds,
  `config/levels` (full VIP economics), `games/v2/plinko` (full probability tables),
  tap-trading bets/price-history, `leaderboard` (69KB standings w/ internal UUIDs + registered
  ms + amounts — same leak class as bets/live). `/auth/blockCheck` = the region oracle
  (`{reason:region_page,location:de}`; `?ip=` is client-display-only).
- **Zero rate limiting** on `/auth/token` mint + `/ws/user/bets/live` (15-burst at 0.25s: all
  201/200, no 429) — unthrottled anon minting + unthrottled feed scraping.
- **Security headers: absent** (no HSTS/CSP/XFO/XCTO on root); duelbits.com cert = apex-only
  SAN. Bundle secrets CLEAN (416 chunks, all key-pattern hits false positives).
- **Unauth surface EXHAUSTED.** Every compromise-class vector now sits behind (a) the
  restricted-region wall (residential unrestricted IP needed) or (b) a real wallet session.
  The operator's console remains the unlock for the replay/binding/mass-assignment chain.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
