# R2 — surface inventory (read-only)

- source canon: `kaisha/ladder-playbook.md`
- bindings: **MASTG-RES** · **CWE-798** · **ATT&CK T1552**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- listening services: address:port + process name (own host)
- banners: exact strings → feed `kaisha cve --banner`

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
