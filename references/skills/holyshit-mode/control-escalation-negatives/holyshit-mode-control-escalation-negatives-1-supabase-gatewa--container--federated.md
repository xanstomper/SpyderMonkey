# 1. Supabase/gateway forged-claim RBAC discriminator (THE key pattern) — container / federated

- source canon: `holyshit-mode/control-escalation-negatives.md`
- base technique: `holyshit-mode-control-escalation-negatives-1-supabase-gatewa.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **federated** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

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

## Probe adjustment (container × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
