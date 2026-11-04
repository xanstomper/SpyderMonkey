# Damaging confirmed findings (pre-auth, 2026-10-04 session) — web-app / high-priv

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-damaging-confirmed-findings-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **high-priv** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

1. **No rate limiting on handoff-code exchange** (score 55): `POST /api/auth/platform-handoff/exchange` on chat+platform hosts — 20 rapid garbage codes in a shell loop, zero 429s, no lockout, no captcha. This endpoint exchanges a one-time handoff code for Supabase access+refresh tokens; uniform `401 invalid_handoff_code`. If code entropy is low or TTL long, session-hijack brute vector.
2. **No rate limiting on OAuth token endpoint** (score 50): `POST /platform/api/oauth/token` — 15 rapid invalid codes, zero 429s. PKCE S256 with random verifiers mitigates blind brute; the finding is the absent brute defense in the login chain.
3. **signup_unconfirmed_row** (score 40): signup creates a real user row with `role:authenticated` + `aud:authenticated` persisted PRE-confirmation (login blocked by `email_not_confirmed`). Probe: supabomb_probe_1@mailinator.com. Operator declined bootstrap; row left unconfirmed, no login attempts after "stop".
4. `/api/public/billing/config` leaks Stripe `pk_live_...` + `billingMode: live` + fingerprint (publishable = public by design; LOW/info).
5. GoTrue settings/health exposure (info, score 30): provider map (discord/google/email/phone), `phone_autoconfirm:true`, GoTrue v2.186.0.

## Probe adjustment (web-app × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
