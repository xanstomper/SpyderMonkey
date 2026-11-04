# Full working auth-flow notes (reusable) — graphql / low-priv

- source canon: `holyshit-mode/case-gratisfy-reengagement2.md`
- base technique: `holyshit-mode-case-gratisfy-reengagement2-full-working-auth-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **graphql** · auth **low-priv** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Handoff start: `POST /api/auth/platform-handoff/start` — `Authorization: Bearer <supabase AT>` header, body `{refresh_token, next, target}` ONLY. Response: `{code, expiresAt, redirectUrl}` with 32-hex code. Exchange: `POST /api/auth/platform-handoff/exchange {code}` → full platform session tokens. One-time.
- Email confirm end-to-end: signup → mailinator inbox API → scrape `token=` → **GET** `/auth/v1/verify?token=..&type=signup&email=..` (JSON POST may reject valid tokens with otp_expired) → 303 fragment carries AT+RT. One-time token.
- Password grant errors: `email_not_confirmed` pre-confirm; `invalid_credentials` uniform post.
- api host: uniform `Invalid API key` (no format oracle); session JWT rejected as Bearer (separate trust root, correct); 15-20 rapid junk-Bearer = zero 429.
- PostgREST public schema: ONLY `profiles` (user_id, created_at, updated_at, email_verified) + `chat_messages` (id, user_id, conversation_id, role, content, created_at). RPC sweep all PGRST202. Storage `[]`, edge functions 503.
- magiclink: rate-limited (429, ~60s) — the ONE working email limiter; but `/auth/v1/verify` itself unthrottled.
- CF challenge on inference POSTs is per-request random (403 HTML / 502 vs real 400 JSON with identical headers) — judge by body type, retry spaced.

## Probe adjustment (graphql × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
