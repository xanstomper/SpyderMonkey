# PostgREST recon (RLS-solid)

- source canon: `holyshit-mode/case-gonka-api.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `/rest/v1/` root → 401 service_role only; per-table anon reads still work.
- Existing tables: `api_keys`, `balances`, `transactions` — all `[]` to anon.
- 42703 column oracle: `api_keys(id,user_id,key,created_at)`,
  `balances(id,user_id,credits_cents)`, `transactions(id,user_id,type,created_at,description)`.
- RLS holds vs tautology `or=(key.neq.null)` / neq filters / `Prefer: count=exact`.
  IDOR by `id=` / `user_id=neq.` negative — scoping is on `auth.jwt()->>'sub'`.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
