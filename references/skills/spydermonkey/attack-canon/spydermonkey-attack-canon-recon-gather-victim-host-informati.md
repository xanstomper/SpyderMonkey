# Recon Gather Victim Host Information (T1592)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: passive host inventory — software, roles, versions reachable from the outside
- probe: banners, headers, TLS certs, favicon hashes — zero-touch reads
- wall: NO-GAIN — the dossier feeds downstream planning, nothing executes

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
