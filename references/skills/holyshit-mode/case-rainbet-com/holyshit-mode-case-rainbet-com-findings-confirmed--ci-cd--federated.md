# Findings (confirmed) — ci-cd / federated

- source canon: `holyshit-mode/case-rainbet-com.md`
- base technique: `holyshit-mode-case-rainbet-com-findings-confirmed.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **ci-cd** · auth **federated** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

1. **Arbitrary cookie-toss gadget on the main domain — media.rainbet.com (score 80).**
   The page writes EVERY `?param` as a cookie `Domain=rainbet.com; Path=/; Max-Age=90d;
   SameSite=None; Secure` (≤25 params/visit). Reserved list = exact-match
   {session, sid, token, jwt, auth, csrf, xsrf, PHPSESSID, stag} — **misses the real session
   family `stel_token`/`stel_ssid`/`stel_acid`, the FingerprintJS `client-context`, and
   `referralCode`**. Verified live in chromium: `?testparam=hello123&client-context=1111...`
   both land in `document.cookie`. Any link to `media.rainbet.com/?<name>=<value>` = attacker
   cookie on the casino's origin for 90 days.
2. **Fingerprint hijack via the same gadget (score 70).** `client-context` =
   FingerprintJS Pro v4 visitorId (fpjscdn.net, region us). SPA: `if (cookie.get("client-context")) return;`
   — cookie present ⇒ fingerprint generation SKIPPED, attacker value adopted. Ban-evasion +
   risk-model poisoning primitive (`er_risk_level` exists server-side).
3. **Affiliate-attribution hijack (score 65).** `stag` cookie = the affiliate tag
   (`getAffiliateTag: () => cookie.get("stag")`), consumed at sign-up attribution.
   `clever.rainbet.com?stag=<tag>` tosses it for 7d (SameSite=None). media.rainbet.com
   FORCE-sets `stag=58916_6a29c69394efb819d8945edf` on every visitor (affiliate 58916 = their
   own ad pipeline default).
4. **Metamask auth open pre-auth (score 60).** `POST /v1/auth/metamask/initiate
   {address, stage:1}` → 201 `{success, hash:8-char}` with NO captcha/Turnstile. Verify =
   `POST /v1/auth/metamask/verify {address, localized_message, signature, stage:2}` (personal_sign
   over `localized_message + " " + hash`). Solana wallet auth shares the error family
   (`er_sol_signature_verification_failed`). Rate limit on the auth plane is IP-keyed and LONG
   (er_rate_limit 429 persisted >30 min after a probe burst — see runner).
5. **Unauth cross-user bet feeds (score 45).** socket namespaces `/recent-bets`,
   `/recent-wins`, `/recent-high-bets` stream to GUESTS: per-bet UUID, user UUID, masked
   username (4 chars + "…"), rank (e.g. platinum-ii), amounts/currency/multiplier, 32-char
   per-bet token (server-seed-family), game/provider slug. Anonymization is inconsistent —
   some items omit `u.i`/`u.n` entirely. `/player-bets` guest connect → CONNECT_ERROR
   `er_spectator_not_allowed`; `/chat` guest joins silently dropped. Connection gate:
   replica sockets (identical frames, same cookies) are closed ~1.2s after the first packet;
   frames injected onto the SPA's own trusted connection are processed normally.
6. **TLS-impersonation apex bypass (score 75, tradecraft).** The JA3-keyed block falls to
   curl-impersonate; the whole `/_next` asset tree + SSR + services plane become reachable.
7. **`/v1/public/active-races` 500 er_database_error** on services for all `type` params while
   SSR fetches the same data internally — routing/regression inconsistency.
8. **Public profile ID oracle (score 55).** `/v1/public/profile?id=<str>` — short strings/ints
   → `404 er_no_user_found`; arrays → `400 er_field_validation_id`; UUIDs rejected
   (`er_field_validation_id`). IDs ride `?user=` on the bets page. Real publicId format still
   unknown (feed UUIDs are NOT it).
9. **Internet-exposed AMQP: rbtmq-stg.rainbet.com (159.203.53.157) :5672** — protocol-header
   exchange leaks broker capabilities (publisher_confirms, exchange routing). Banner-level
   only per doctrine. Siblings rbtmq-preprod(-us) = port 22 only.
10. **Official mirror fleet: rainbet.com/.live/rainbet1.com/rainbet.us** ("the same account,
    balance, and history"). .live/.rainbet1 = managed challenge wall for the DC vantage;
    rainbet.us = geo-403 JS-redirect wall EXCEPT `/api/analytics/account-id` (401 leaks through).

## Probe adjustment (ci-cd × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
