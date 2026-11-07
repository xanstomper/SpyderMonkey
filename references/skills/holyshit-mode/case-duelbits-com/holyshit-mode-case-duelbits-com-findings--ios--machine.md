# Findings — ios / machine

- source canon: `holyshit-mode/case-duelbits-com.md`
- base technique: `holyshit-mode-case-duelbits-com-findings.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **ios** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

1. **APIConfig chunk = the whole fleet topology** (`/assets/APIConfig-<hash>.js`). Per-brand
   domains ship `{token, auth, oAuth, websocket, gamesocket}` URLs: `/auth` + `/ws` + `/gs`
   on the main domain, with the OAUTH pointed at a SISTER BRAND (switchflips.com). Fleet:
   duelbits.com/.io/.net/.bet + sportsbits.com + switchflips.com. Grep every fetched chunk
   for a config-by-name chunk (`APIConfig-*`, `env-*`) before probing blind — the topology
   comes free.
2. **Internal env naming in the config**: `dev.r19.ea.duelbits.(com|io)` and a
   `deploy-preview-N.r19.ea.duelbits.(com|io)` regex = live Netlify preview routes.
   Enumerate `deploy-preview-<N>` as live internal surfaces.
3. **Compiled env chunk leaks** (`env-*.js`): Contentful delivery token + space id +
   `VITE_CONTENTFUL_ENVIRONMENT: release-candidate` — PROD PULLS STAGING CMS CONTENT. The
   delivery token works live: 13k entries, 123 types (rewardConfiguration x1547,
   countryRestrictions with dev leftovers, telegramUser config). Marketing-class only; a
   delivery token is semi-public by design, so rate the RC-on-prod as the finding, not the
   token.
4. **NestJS fingerprint**: errors are `{statusCode, code:'general.NotFound'}` — a JSON 404
   under `/auth/*` = REAL routing with wrong subpaths (vs the SPA shell 200 text/html =
   ghost). Fingerprint the error format before declaring an endpoint dead.
5. **`/ws/config/currencies` = 200 unauth** while `/ws/config` = 403 — per-path WAF rules;
   sweep siblings of any open config endpoint.
6. **Web3-wallet-only auth chain (the whole login surface):** there is NO email/password
   auth — the SPA's `web3-sign-in-*.js` chunk ships the full flow: (1) `POST
   /auth/web3/message/?publicAddress=<addr>` returns the sign-message; (2) the wallet signs
   via `personal_sign`; (3) `POST /auth/web3` body `{address, signature, ...state}` returns
   the session token. Three queued vectors, each one fetch from a page context: **nonce
   replay** (call the message endpoint twice for one address — identical message = one
   captured signature is a permanent login), **address-registration oracle** (verify-endpoint
   error differences for registered vs unregistered wallets), and **state-param forwarding**
   (the client forwards arbitrary URL state params into the auth POST body = mass-assignment
   injection point). All WAF-blocked from the burned vantage — hand the live tests to the
   operator's console (kit below).
   LIVE CHALLENGE FORMAT: the sign-message is a FLAT personal_sign utf8 string — "You are
   authenticating on <brand> using address <addr>. Do not share this message with anyone!
   <nonce>" — NO timestamp, NO expiry, NO domain binding, 6-digit numeric nonce (one sample).
   The signed credential therefore has NO intrinsic time bound; replay protection is purely
   the server's nonce-consumption policy, and every absent binding field is itself an audit
   finding.
   Console handoff kit (ordered by decisiveness, all self-account, non-destructive):
   1. Signature replay — Network tab → the login's `POST /auth/web3` → Copy as fetch → run
      TWICE. Copy-as-fetch preserves the client's real headers = byte-faithful replay. Both
      200 = one captured signature is a reusable login; nonce-error on the 2nd = single-use.
   2. Signature↔address binding swap — same body with a random address. Accepted = no
      binding = total auth bypass; expect rejection (that IS the test).
   3. Challenge determinism — message endpoint ×3 same address: identical = static challenge;
      rotating = sequence-check the trailing nonce for counter/timestamp derivation.
   4. Registration oracle — message endpoint for the operator's address vs a fresh random
      one; different status/shape = wallet-existence enumeration oracle.
   5. State-param forwarding — replay body + extra keys (role/is_admin/balance/vipLevel) and
      `?isAdmin=true`, then reload and diff the user/me endpoint for anything that stuck.
   Handoff hygiene: instruct the operator NOT to paste the minted session token back —
   statuses and error bodies only.
7. **One CMS delivery token read FOUR environments** (master, release-candidate, staging,
   development) — the token is space-scoped, not env-scoped. The development env held MORE
   entries than master, with dev-test leftovers dated the day before recon. Enumerate
   `<env>` in the Contentful URL for every env name you can guess; the staging/development
   layers are where drafts and internal tests live.

## Probe adjustment (ios × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
