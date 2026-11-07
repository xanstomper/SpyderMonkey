# Negatives (do not re-probe w/o code change)

- source canon: `holyshit-mode/case-atessa-top.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Turnstile server-verified: bypass matrix (missing/empty/null/dummy/obj) all rejected; dummy → `Invalid CAPTCHA` ≠ `missing` = server verify confirmed cheaply.
- Google OAuth hardened: redirect_uri hardcoded (override ignored), state cookie-bound (cross-cookie callback → auth_failed). client_id `805021536698-smja1uiljue78kr2k3qfif15ki7iiitv`.
- Stripe webhook signature enforced (uniform 400 `Invalid signature` for empty/no-sig/bad-sig).
- CORS allow-list (`allow-credentials:true` present but no ACAO reflection for evil.com).
- Admin `/admin/login` SQLi negative, server-rendered form, French errors.
- SPA ghost shell (1583B HTML) everywhere outside `/api/*` + `/v1/*`.
- Reset/verify token endpoints: uniform `invalid or has expired` for garbage tokens.
- Public pricing/announcements/tutorials endpoints are data-only (pricing JSON leaks tier config + `slots_remaining` — observation, not compromise).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
