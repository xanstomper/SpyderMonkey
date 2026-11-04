# Negatives (do not re-probe w/o code change) — chain composition

- source canon: `holyshit-mode/case-atessa-top.md`
- base technique: `holyshit-mode-case-atessa-top-negatives-do-not-re-probe-w-o-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Turnstile server-verified: bypass matrix (missing/empty/null/dummy/obj) all rejected; dummy → `Invalid CAPTCHA` ≠ `missing` = server verify confirmed cheaply.
- Google OAuth hardened: redirect_uri hardcoded (override ignored), state cookie-bound (cross-cookie callback → auth_failed). client_id `805021536698-smja1uiljue78kr2k3qfif15ki7iiitv`.
- Stripe webhook signature enforced (uniform 400 `Invalid signature` for empty/no-sig/bad-sig).
- CORS allow-list (`allow-credentials:true` present but no ACAO reflection for evil.com).
- Admin `/admin/login` SQLi negative, server-rendered form, French errors.
- SPA ghost shell (1583B HTML) everywhere outside `/api/*` + `/v1/*`.
- Reset/verify token endpoints: uniform `invalid or has expired` for garbage tokens.
- Public pricing/announcements/tutorials endpoints are data-only (pricing JSON leaks tier config + `slots_remaining` — observation, not compromise).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
