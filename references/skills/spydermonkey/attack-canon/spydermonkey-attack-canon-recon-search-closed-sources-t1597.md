# Recon Search Closed Sources (T1597)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **PTES-PE** · **CWE-522** · **ATT&CK T1555**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: paid/registered intel sources for victim data
- probe: only what the operator legally holds credentials for
- wall: no credential use beyond declared scope; nothing purchased mid-run

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
