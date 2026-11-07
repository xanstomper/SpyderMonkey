# 1. Supabase/gateway forged-claim RBAC discriminator (THE key pattern) — linux / hardened

- source canon: `holyshit-mode/control-escalation-negatives.md`
- base technique: `holyshit-mode-control-escalation-negatives-1-supabase-gatewa.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **linux** · auth **hardened** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

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

## Probe adjustment (linux × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
