# WSTG API Testing (WSTG-API)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-APIT-10** · **CWE-1321** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: graphql introspection, mass assignment, rate limits, versioning
- probe: the MASSASSIGN POST battery + graphql alias/batch checks
- wall: documented classes; no data modification beyond the proof request

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
