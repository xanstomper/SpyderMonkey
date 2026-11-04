# 2026-11-02 round-4 (Vermes): OAuth plane + state-cookie mechanism

- source canon: `holyshit-mode/case-duelbits-com.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

Past-vuln/leak research (Halborn Feb-2024 "security vulnerability", Sep-2026 $7M key
compromise, NO post-mortem either time; on-chain artifacts 0x3559ee...4a84f369/2024 +
0x8db9d7f0...c20C306/2026; $190.6M/85k depositors scale) — no publicly disclosed WEB-layer
vuln exists to re-test; the two breaches were both wallet-infra. So round-4 attacked the
OAuth plane (new) + a discovered state-injection mechanism:

- **OAuth starters on duelbits.com are NOT region-gated (open from DC):** `GET /auth/steam`
  → 302 Steam OpenID (`openid.return_to`/`realm` HARDCODED to switchflips.com; attacker
  `return_to` values ignored — fast negative). `GET /auth/google` → 302 Google OAuth
  (redirect_uri HARDCODED `https://switchflips.com/google/redirect`, client_id
  913811036467-...; **NO state param** → OAuth login-CSRF hypothesis ~35). Switchflips is
  reachable with NO WAF from DC: google code-exchange consumer live (garbage code → 500,
  `error=access_denied` → 401), steam OpenID consumer live (cancel → 401; EVERY id_res
  variant incl. well-formed-bad-sig → 500 = unhandled-exception fingerprint; sig
  verification exists → no forge without Steam's key).
- **`switchflips.com/token` = a SECOND open anon mint** (`sub=websocket`, 30s TTL, same
  aud/iss; `id` = GLOBAL CONSTANT across every request). Decisive closeout of the mint
  chain: tested bearer+query against bets/my, profile, transactions, keno/hilo history —
  403 EVERYWHERE, completing the sub matrix {user, admin, mod, internal, system,
  websocket}: **the unvalidated scope mint is definitively inert on the HTTP plane.**
- **`query_state` cookie — CONFIRMED injection mechanism (the round's big find):**
  `?state=<anything>` — any string or arbitrary JSON — on `/auth/google` or `/auth/steam`
  is persisted verbatim into the `query_state` cookie (`{"state":"<raw>"}`). The web3
  signIn code (round-3) then JSON.parses `state` and **spreads truthy keys into both the
  query and the auth POST body**. Full attacker chain: crafted link with
  `?state={"isAdmin":true,"authRole":"Sponsor","accountLevel":8}` → victim's browser holds
  query_state → any subsequent login (web3/Google/Steam — all three read the mechanism)
  ships attacker keys to the server. Client-side chain is PROVEN; the single remaining
  gate is whether the server DTO applies unknown keys (gratisfy/gonka precedent: two
  targets persisted claims but RLS-gated them — needs the one console test).
- **`header_state` cookie = topology/geo echo** (XFF chain client→CF→CloudFront, proto
  http:80, x-amzn-trace-id, cf-iplongitude/region): observation-class leak; also proves
  the region gate reads real CF geo (unspoofable).
- Negatives logged: no password/local/telegram/discord/otp routes exist (404); steam
  OpenID return_to pivot dead; google redirect_uri override dead (hardcoded); mint+cookie
  chains on gated HTTP dead.

**Console kit v3 (the single ask — 5 minutes, self-account, non-destructive):**
1. Fresh browser → `duelbits.com/auth/google?state={"isAdmin":true,"authRole":"Sponsor","accountLevel":8,"verified":true}`
   → log in with ANY Google account → then check `/user/me` (or profile page) for stuck
   keys + note the account the session holds (2nd Google acct optional for the login-CSRF
   half). Statuses only.
2. Web3: existing Copy-as-fetch replay ×2 on `POST /auth/web3`, then + the same state JSON.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
