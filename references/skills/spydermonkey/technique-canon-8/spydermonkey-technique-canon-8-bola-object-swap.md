# BOLA object-swap

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Endpoint returning objects by id accepts another tenant's/owner's id (the IDOR family). Decisive test: baseline with your object, attack with a sibling id you control — swapped content = CONFIRMED.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
