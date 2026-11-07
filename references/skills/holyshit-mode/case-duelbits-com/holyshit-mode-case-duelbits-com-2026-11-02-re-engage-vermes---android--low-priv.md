# 2026-11-02 re-engage (Vermes VM vantage): sockets, PF verification, region wall — android / low-priv

- source canon: `holyshit-mode/case-duelbits-com.md`
- base technique: `holyshit-mode-case-duelbits-com-2026-11-02-re-engage-vermes-.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **android** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

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

## Probe adjustment (android × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
