# PostgreSQL error and CAST channels

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`::int` cast failures and `generate_series` timing — the error text names the query context. Decisive test: cast-error reflection with a marker value embedded.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
