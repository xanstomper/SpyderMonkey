# Damaging confirmed findings (pre-auth, 2026-10-04 session) — chain composition

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-damaging-confirmed-findings-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. **No rate limiting on handoff-code exchange** (score 55): `POST /api/auth/platform-handoff/exchange` on chat+platform hosts — 20 rapid garbage codes in a shell loop, zero 429s, no lockout, no captcha. This endpoint exchanges a one-time handoff code for Supabase access+refresh tokens; uniform `401 invalid_handoff_code`. If code entropy is low or TTL long, session-hijack brute vector.
2. **No rate limiting on OAuth token endpoint** (score 50): `POST /platform/api/oauth/token` — 15 rapid invalid codes, zero 429s. PKCE S256 with random verifiers mitigates blind brute; the finding is the absent brute defense in the login chain.
3. **signup_unconfirmed_row** (score 40): signup creates a real user row with `role:authenticated` + `aud:authenticated` persisted PRE-confirmation (login blocked by `email_not_confirmed`). Probe: supabomb_probe_1@mailinator.com. Operator declined bootstrap; row left unconfirmed, no login attempts after "stop".
4. `/api/public/billing/config` leaks Stripe `pk_live_...` + `billingMode: live` + fingerprint (publishable = public by design; LOW/info).
5. GoTrue settings/health exposure (info, score 30): provider map (discord/google/email/phone), `phone_autoconfirm:true`, GoTrue v2.186.0.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
