# Ledger state

- source canon: `holyshit-mode/case-obsidian-y-api-pg-bypass.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`holyleadger` target `obsidian-y-api-r4xe.onrender.com`:
- `pg_chat_unauthenticated_free_ai` confirmed score 90
- `pg_chat_no_rate_limit` confirmed score 70
- `pg_hidden_50k_system_prompt` hypothesis score 55 (decisive next: reasoning-field extraction)
- `pg_stream_passthrough` confirmed score 35
- Chain: `free_ai_abuse`: pg_chat_no_auth → unlimited_completions → no_rate_limit →
  free_upstream_inference (confirmed)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
