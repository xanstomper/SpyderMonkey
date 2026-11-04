# Key facts (upstream source + live confirmation)

- source canon: `holyshit-mode/case-apimart-newapi-fork.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

- **TurnstileCheck() reads `c.Query("turnstile")`** — token goes in the QUERY STRING even for POST
  routes: `POST /api/user/register?turnstile=TOKEN`.
- **`GET /api/status`** dumps admin module map (SidebarModulesAdmin: ipPool/channel/models/user/
  setting/errorLogs/dailyStats), OAuth client IDs, Turnstile sitekey, version commit hash, email
  verification flag, invite cashback config — all unauth.
- **`GET /api/setup`** returns `{status, root_init, database_type}`. status:true = setup complete;
  root_init is only populated when status:false. Don't false-positive "root not initialized".
  `POST /api/setup` on a completed target: "System has already been initialized."
- **`GET /api/oauth/state`** mints states unauth but state is session-cookie-bound (hardened).
- **`GET /api/pricing/models/all`** dumps the FULL model catalog with internal margins, discount
  ratios, membership tiers unauth when pricing.requireAuth=false — observation-class competitive
  intel, NOT a compromise (473KB on apimart).
- **Rate limits:** `CriticalRateLimit` = 20 req / 20 min per IP (upstream default,
  common/constants.go), SHARED across all critical routes (register/login/reset/verification —
  a burst on one locks all). Most app errors return HTTP 200 with `success:false` — 429 detection
  MUST read bodies, not status codes.
- **Password reset flow:** `GET /api/reset_password?email=X` (Turnstile-gated) emails a 32-hex UUID
  token; `POST /api/user/reset {email, token}` (NO Turnstile — only CriticalRateLimit) returns the
  NEW PASSWORD verbatim in `data`. Email-verification codes are `GenerateVerificationCode(6)` =
  first 6 UUID-hex chars (~1M space, brute-able ONLY if register's Turnstile is bypassable).
  `GET /api/verification?email=` (6-digit codes) IS Turnstile-gated. Reset tokens are NOT
  brute-able (32 hex). Realistic fork-level chain: free-trial farming via IPv6 rotation +
  disposable email, gated on Turnstile solving.
- **In-memory verification map** (common/verification.go): global map, `removeExpiredPairs()` only
  purges EXPIRED entries — inserts ALWAYS happen, so no eviction primitive (memory growth only).
  Do not chase an eviction DoS there.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
