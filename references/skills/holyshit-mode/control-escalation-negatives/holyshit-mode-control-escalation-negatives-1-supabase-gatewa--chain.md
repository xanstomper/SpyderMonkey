# 1. Supabase/gateway forged-claim RBAC discriminator (THE key pattern) — chain composition

- source canon: `holyshit-mode/control-escalation-negatives.md`
- base technique: `holyshit-mode-control-escalation-negatives-1-supabase-gatewa.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Findings feed mass-assignment into signup `data`. The decisive control test is whether the forged
claims are *honored* by any server component — not merely whether they persist.

**Test sequence:**
1. `POST /auth/v1/signup` with `data: {"role":"admin","is_admin":true,"is_super_admin":true,"balance":999999999,"tier":"enterprise"}`.
2. Confirm persistence: the SIGNED `access_token` `user_metadata` carries all of it verbatim
   (`email_verified:true`, `is_super_admin:true`, `role:admin`). Signature is valid — GoTrue authenticates it.
3. Probe each data plane with that authed token:
   - **PostgREST `/rest/v1/<table>` with `Authorization: Bearer <authed>` → `{"message":"Invalid API key"}`.**
     PostgREST uses a SEPARATE JWT secret/trust root from GoTrue. Your forged claims are never
     evaluated there. Do not chase — the row of `401` IS the result.
   - **Edge function `/functions/v1/<slug>` with the authed token → `Invalid API key`.**
     Edge functions require a separate service-issued `sk_` key, not the GoTrue JWT.
   - Unauthenticated anon key: `settings` may be world-readable (config leak), but `api_keys`,
     `balances`, `transactions` return `[]` (RLS holds) — and anon `<table>?select=*` on the
     sensitive tables returns `[]`, never data.
4. **Verdict:** forged metadata surviving a valid signature = **UI/decorative only, NOT a privilege
   escalator**. Layout: the SPA `/admin` route reuses the SAME auth-guard component as `/dashboard`,
   so it gates on authentication, not role — but you can't even get past the edge-fn `sk_` gate with
   the forged token. Report the negative; it's the answer to "did we gain control."

**Auth token mechanics (GoTrue):** `grant_type` goes in the **query string**;
credentials in the JSON **body**. Body-without-grant_type → `unsupported_grant_type`;
grant_type in body → `bad_json`/`could not parse`. Correct: `POST /auth/v1/token?grant_type=password`
with body `{"email","password"}` → 200 access_token. Confirm-email token is one-time; consume via
`GET /auth/v1/verify?token=...&type=signup`.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
