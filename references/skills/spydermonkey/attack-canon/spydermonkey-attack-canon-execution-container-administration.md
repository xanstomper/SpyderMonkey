# Execution Container Administration Command (T1609)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **PTES-CON** · **CWE-250** · **ATT&CK T1611**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: exec into running containers
- probe: read-only inventory of the container surface; NO exec
- wall: REFUSED — namespace escape execution is outside every wall

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
