# Findings (ranked, confirmed unless noted) — websocket / unauth

- source canon: `holyshit-mode/case-gamdom-com.md`
- base technique: `holyshit-mode-case-gamdom-com-findings-ranked-confirmed-unle.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **unauth** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- **70 hidden_mode_display_username_leak (THE find)**: "hide statistics" masks `username`→
  "Hidden user" but `display_username` = REAL name verbatim; 39 hidden users (name+id+xp+balance)
  in one 30s anonymous EIO=3 socket capture (457KB): emrakdnz (1.18T xp), psxroolz (9.7B value),
  watersound11 (10.4B), weakerarms (36B). Server-side field-ALIAS masking gap — fix = NULL both
  fields on every feed path when hidden_mode (or drop the row).
- **75 crash_no_preround_commitment**: `game_starting={game_id,time_till_start}`,
  `game_started={bonusPool}` — ZERO hash pre-round; the sha256 ships in `game_crash` WITH the
  result. PF unverifiable on the public wire for crash. BUT the chain itself verifies (see
  negatives) — the exposure is the missing PRE-round publication + the forced-flag escape hatch.
- **55 crash_forced_capability_flag**: `forced:false` in public `game_crash` = staff-side outcome
  control capability exists. A `forced:true` round = the PF escape hatch (watch on re-engage —
  that is the part-2 material).
- **70/65/65 Turkish entrance fossil box (217.23.12.109)**: PHP 5.4.45 (X-Powered-By, EOL 2015),
  **MariaDB 5.5.68 on 0.0.0.0:3306** (version leaks in handshake; EOL 2018; default creds DENIED —
  posture, not open door), VestaCP panel :8083, **authoritative DNS for tr/giris.perabet.com
  served by the SAME box** (recursion refused — not an open resolver), Dovecot+vsFTPd+
  OpenSSH 7.4 (2016). One credential = root + login-page tap + DNS control of the funnel.
- **55 vestacp_panel_analysis**: pre-auth login endpoint (`/api/v1/login/index.php`) mints a
  fresh token unauth EVERY call (anon shell, empty user) AND discloses the full system config
  (VERSION 0.9.8, every subsystem, `VESTA_CERTIFICATE:"admin:giris.perabet.com"`). Gated
  endpoints (list/edit/delete/upload/view-file) REJECT the anon token in all 4 auth shapes —
  custom session check holds. Token travels in URL query params. The panel's own 1.5MB React
  bundle = the full custom API map (`/api/v1/{login,reset,list/*,edit/*,delete/*,upload/?dir=,
  view/file/<path>,bulk/*}`).
- **60 engineio_sid_bearer_attach**: second websocket attached to a LIVE page session by sid
  alone (101 + ping answered). Origin allowlist = client-asserted (fakeable from scripts). Sid
  leak = authed-socket takeover mechanism. Fix: bind socket session to the HTTP session cookie
  server-side.
- **60 crash_hidden_user_live_financials**: `/crash` streams per-play `walletInfo` (LIVE balance
  in real units — SOL_LAMPORT 85.9M→42.9M draining bet-by-bet) for hidden users to anon sockets.
- **65 turkish_funnel_fully_necrotic**: main LOGIN+SIGNUP CTAs → `a.info/pera` = DEAD domain
  (registered, no DNS — connection fails both schemes). Mirror links → parked GoDaddy landers
  (perabet-01/02/03-ampsites.com, batch-registered 2023-01, expire 2027-01). Every link and name
  in the funnel is dead/unregistered/parked; nobody monitoring it.
- **55 golvar8_unregistered_link**: entrance page links `golvar8.com` ("Perabet TV" button) —
  UNREGISTERED. Plus the box's PTR identity `sieveunem.net` — also unregistered. Registration
  takeover of the funnel = live exploit for registrar-fee money.
- **50/40 logerror/pageview_unauth_write**: unauth unthrottled write sinks — 1MB payload, any
  content-type, malformed JSON ok, 20-burst zero 429 — on BOTH brands.
- **45 general_namespace_unauth_feed**: 234KB/15s firehose (leaderboards, bet ticker with user
  id+username+profit+game+date, KOTH prizes, platform stats) — mirrors public UI mostly.
- **45 db_schema_disclosure_in_feed**: `sourceTable` field = crash.plays/dice.plays/hilo.plays/
  roulette.plays/external_games.transactions_v2 handed to anonymous sockets. Strip sourceTable/
  sourceId/refClientId from public events.
- **30s**: unauth_socket_session (engine slots free for anon); clientapi_method_oracle (param
  validation before auth = method-enum via `unknown rpc` vs `Invalid parameters` vs Express
  `Cannot POST`); prod_config_key_leak (`RECAPTCHA_SITE_KEY=6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI`
  = Google's universal always-pass TEST key in the prod bundle; CAPTCHA_TYPE=turnstile);
  stale_records (mail.perabet.com + webmail/smtp → dead IPs; PTR = mail.pronetgaming.com =
  vendor mail dependency).
- **25 docroot_path_redirect_leak**: Apache catch-all 301 leaks `/home/admin/web/<domain>/
  public_html/`; filesystem-as-URL tests fall through to the catch-all (no read primitive).
- **20 userapi_surface**: third prefix `/user-api/*` (softblock-details unauth-readable,
  change-pp avatar upload).
- Open hypotheses: **chat_rpc_role_gate_untested (60)** — adminCommand(nextrain|cooldown|unmute)/
  devCommand/muteUser/tipUser/tipRain/toggleMessagePin/toggleGloballyMessagePin live in the
  server method table, all reject unauth at the session fence; needs ONE session.
  **inteligance_gamdom_host (65)** — internal-named host, cert issued 2026-07-27, DNS stripped
  post-breach, no wayback captures. Needs their DNS/server logs.

## Probe adjustment (websocket × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
