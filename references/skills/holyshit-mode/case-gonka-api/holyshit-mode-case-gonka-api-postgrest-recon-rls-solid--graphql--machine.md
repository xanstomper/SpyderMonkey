# PostgREST recon (RLS-solid) — graphql / machine

- source canon: `holyshit-mode/case-gonka-api.md`
- base technique: `holyshit-mode-case-gonka-api-postgrest-recon-rls-solid.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **graphql** · auth **machine** · chain role **entry**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- `/rest/v1/` root → 401 service_role only; per-table anon reads still work.
- Existing tables: `api_keys`, `balances`, `transactions` — all `[]` to anon.
- 42703 column oracle: `api_keys(id,user_id,key,created_at)`,
  `balances(id,user_id,credits_cents)`, `transactions(id,user_id,type,created_at,description)`.
- RLS holds vs tautology `or=(key.neq.null)` / neq filters / `Prefer: count=exact`.
  IDOR by `id=` / `user_id=neq.` negative — scoping is on `auth.jwt()->>'sub'`.

## Probe adjustment (graphql × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
