# 4.1 GoTrue/Supabase chain (score 90 — THE standard ladder) — iac / machine

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- base technique: `3am-shinjitsu-arsenal-04-auth-identity-4-1-gotrue-supabase-c.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iac** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: template/state files are the infrastructure inventory — read-only crown of the exposure
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- FINGERPRINT: `www-authenticate: Basic realm="service"` + `x-kong-response-latency` +
  `x-kong-request-id` + ACAH contains `apikey` = Kong-fronted Supabase.
- 1. Mine anon key from bundles: `VITE_SUPABASE_ANON_KEY:` (itself an HS256 JWT `role:anon`).
- 2. `GET /auth/v1/settings` + `/auth/v1/health` WITH `apikey: <anon>` = providers, autoconfirm
  (email/phone), disable_signup, sms_provider, GoTrue version. Everything 401 without it.
- 3. Signup with planted privilege keys (§3.4 mass-assignment gate — persistence ≠ trust).
- 4. Email-confirm end-to-end (self-bootstrapped, no operator creds): public-inbox API
  (mailinator `/api/v2/domains/public/inboxes/<u>` → `/messages/<id>`; harakirimail
  `/api/v1/inbox/<n>` → `/api/v1/email/<_id>` → `bodyhtmltext`) → regex `token=([a-f0-9]{40,})`
  → consume ONCE via `GET /auth/v1/verify?token=...&type=signup&email=...` (303 → capture
  `#access_token=...&refresh_token=...` from `%{redirect_url}` fragment — one-time).
  JSON `POST /auth/v1/verify` may reject VALID tokens (`otp_expired`) — use the GET route.
- 5. Decode JWT: does `user_metadata.role` survive into claims? Then the §3.4 trust gate.
- 6. Confirm-email `redirect_to` param = mirror-host leak (Lovable.app mirrors etc.).
- Signup persists unconfirmed row (`role:authenticated`, blocked only by `email_not_confirmed`)
  = LOW unless a post-confirm API trusts `aud` without `email_verified`.

## Probe adjustment (iac × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
