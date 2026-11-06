# Full working auth-flow notes (reusable) — chain composition

- source canon: `holyshit-mode/case-gratisfy-reengagement2.md`
- base technique: `holyshit-mode-case-gratisfy-reengagement2-full-working-auth-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Handoff start: `POST /api/auth/platform-handoff/start` — `Authorization: Bearer <supabase AT>` header, body `{refresh_token, next, target}` ONLY. Response: `{code, expiresAt, redirectUrl}` with 32-hex code. Exchange: `POST /api/auth/platform-handoff/exchange {code}` → full platform session tokens. One-time.
- Email confirm end-to-end: signup → mailinator inbox API → scrape `token=` → **GET** `/auth/v1/verify?token=..&type=signup&email=..` (JSON POST may reject valid tokens with otp_expired) → 303 fragment carries AT+RT. One-time token.
- Password grant errors: `email_not_confirmed` pre-confirm; `invalid_credentials` uniform post.
- api host: uniform `Invalid API key` (no format oracle); session JWT rejected as Bearer (separate trust root, correct); 15-20 rapid junk-Bearer = zero 429.
- PostgREST public schema: ONLY `profiles` (user_id, created_at, updated_at, email_verified) + `chat_messages` (id, user_id, conversation_id, role, content, created_at). RPC sweep all PGRST202. Storage `[]`, edge functions 503.
- magiclink: rate-limited (429, ~60s) — the ONE working email limiter; but `/auth/v1/verify` itself unthrottled.
- CF challenge on inference POSTs is per-request random (403 HTML / 502 vs real 400 JSON with identical headers) — judge by body type, retry spaced.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
