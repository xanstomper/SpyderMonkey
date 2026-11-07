# Blob anonymous access

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **PTES-CON** · **CWE-250** · **ATT&CK T1611**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Container public-access levels (blob/container). Decisive test: anonymous container LIST = the inventory.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
