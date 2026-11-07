# Brute-force-resistance verification

- source canon: `spydermonkey/technique-canon-13.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- generated: 2026-11-07

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Lockout/rate geometry measured (the canon-I discipline). Decisive test: the counter/lock TTL map = the control's presence/absence.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
