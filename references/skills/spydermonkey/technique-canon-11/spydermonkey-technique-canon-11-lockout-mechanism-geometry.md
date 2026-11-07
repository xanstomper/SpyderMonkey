# Lockout-mechanism geometry

- source canon: `spydermonkey/technique-canon-11.md`
- bindings: **WSTG-ATHN-08** · **CWE-521** · **ATT&CK T1110**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Wrong-password counters, lock TTL, and reset behavior mapped. Decisive test: 5+1 attempts measuring the geometry = the row (the arithmetic, not a crack).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
