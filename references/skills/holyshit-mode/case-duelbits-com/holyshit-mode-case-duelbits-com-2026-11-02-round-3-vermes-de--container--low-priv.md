# 2026-11-02 round-3 (Vermes): deep source study — 420-chunk full-client analysis — container / low-priv

- source canon: `holyshit-mode/case-duelbits-com.md`
- base technique: `holyshit-mode-case-duelbits-com-2026-11-02-round-3-vermes-de.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **container** · auth **low-priv** · chain role **final**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

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

## Probe adjustment (container × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
