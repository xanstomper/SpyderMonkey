# 2026-11-02 round-3 (Vermes): deep source study — 420-chunk full-client analysis — chain composition

- source canon: `holyshit-mode/case-duelbits-com.md`
- base technique: `holyshit-mode-case-duelbits-com-2026-11-02-round-3-vermes-de.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Route

- probes: `wpscan`, `cmseek`, `droopescan`, `cmsmap`, `nmap-wp-plugins`, `nmap-drupal-enum`
- chains: `cms-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

"Study the source and systems" round. Recovered the missing lazy chunks
(`web3-sign-in-B-om7o8t.js`, `index-CW30_Dqt.js`) and re-mined everything.

**APIConfig = the full hardcoded environment map (verified live):**
- `dev.duelbits.com` / `dev.duelbits.io` / `staging.duelbits.com` / `canary.duelbits.com`
  (canary runs the PROD config!) / `auth-dev.duelbits.com` / `auth-staging.duelbits.com` —
  **ALL Cloudflare Access SSO-gated** (every path returns the Access login page, incl.
  /auth/token mint, /auth/web3/message, /ws/user/bets/live). Definitive: no internal API
  host is reachable without Access credentials, from any vantage.
- Preview families: `deploy-preview-N.r19.ea.*` AND the CMS-discovered second family
  `deploy-preview-4025/7113.ea.duelbits.com` (Netlify AWS edge, wildcard DNS live) — all
  deployments deleted (404 Not-Found-Request-ID). `dev-new.`/`news.duelbits.com` =
  dangling DNS (CMS mentions only). `main.r19.ea`/`dev.r19.ea` = Netlify 401.

**web3 auth = exact code now (the console kit is precise):**
- `POST {domain.token}/web3/message/?publicAddress=<addr>` (POST, no body) → `{message}` =
  flat utf8 personal_sign text, `<nonce>` = 6-digit numeric, NO timestamp/expiry/domain.
- `signIn()`: `personal_sign(utf8ToHex(msg), addr)` then
  `state = JSON.parse(urlParam('state')) -> Xb` — **truthy keys only** spread into BOTH the
  query string AND the POST body `{address, signature, ...state}`. Client-side: no
  whitelist, confirmed line-by-line. Server-side key acceptance = the untested question
  (needs a real signature = operator console).

**Internal vocabulary recovered (for the mass-assignment payloads):**
- User/VIP class enum: `0 Normal, 1 Abuser, 2 PVip, 3 VIPThree, 4 Bad, 5 ExVIP, 6 VIPTwo,
  7 VIPOne, 8 Sponsor, 9 Affiliate, 10 Suspicious` — the `authRole`-adjacent ladder.
- loginTypes enum: `local | google | web3 | steam | telegram` (web3 = only client flow).
- `isInternal` in sportsbook code = internal-MARKET flag (odds markets), NOT privilege —
  discriminator, not a backdoor.

**Clean sweep confirmations:** 420 chunks (incl. the previously-missing web3 + index
entry chunks) — zero hardcoded secrets beyond the known VITE_* env set, zero
`user.id === N` backdoors, zero token/refresh logic leaks in the shell. VITE_RMG_OUTLET_AUTH_KEY
= PerformGroup stream-widget outlet key (semi-public by design, provider media key — LOW).
PaymentIQ merchant 101108001 = the deposit cashier vendor config (standard).

**Verdict of the deep-dive:** every "system" plane behind the public surface is either
(a) CF Access-gated (all internal envs), (b) dead DNS/dead deployments (all preview
families), or (c) the prod API itself behind the region wall. The ONLY remaining
compromise-class chain is the web3 state-param mass-assignment → takes the operator's
signature (self-account console test, exact kit below). No new holy shit from source
study; the source instead proves the client-side passthrough is real and unbounded.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
