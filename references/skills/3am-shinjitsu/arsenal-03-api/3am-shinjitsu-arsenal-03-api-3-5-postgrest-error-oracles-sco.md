# 3.5 PostgREST error oracles (score 70, RLS-safe recon)

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- bindings: **WSTG-SESS-01** · **CWE-347** · **ATT&CK T1552**
- generated: 2026-11-04

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- `PGRST205` table absent · `[]` table exists+RLS-gated · `42703` on `?select=<col>` = free
  column-name brute · `22P02` = column TYPE oracle · `PGRST301` = PostgREST uses a DIFFERENT
  JWT trust root than GoTrue (forge against both separately).
- Schema map from errors = coverage finding even when RLS holds.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
