# Negatives (do not re-probe w/o code change) — graphql / high-priv

- source canon: `holyshit-mode/case-atessa-top.md`
- base technique: `holyshit-mode-case-atessa-top-negatives-do-not-re-probe-w-o-.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **graphql** · auth **high-priv** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Turnstile server-verified: bypass matrix (missing/empty/null/dummy/obj) all rejected; dummy → `Invalid CAPTCHA` ≠ `missing` = server verify confirmed cheaply.
- Google OAuth hardened: redirect_uri hardcoded (override ignored), state cookie-bound (cross-cookie callback → auth_failed). client_id `805021536698-smja1uiljue78kr2k3qfif15ki7iiitv`.
- Stripe webhook signature enforced (uniform 400 `Invalid signature` for empty/no-sig/bad-sig).
- CORS allow-list (`allow-credentials:true` present but no ACAO reflection for evil.com).
- Admin `/admin/login` SQLi negative, server-rendered form, French errors.
- SPA ghost shell (1583B HTML) everywhere outside `/api/*` + `/v1/*`.
- Reset/verify token endpoints: uniform `invalid or has expired` for garbage tokens.
- Public pricing/announcements/tutorials endpoints are data-only (pricing JSON leaks tier config + `slots_remaining` — observation, not compromise).

## Probe adjustment (graphql × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
