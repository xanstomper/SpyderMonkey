# WSTG-CLNT-07 Cross Origin Resource Sharing

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **PTES-PE** · **CWE-522** · **ATT&CK T1555**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: ACAO: * with credentials, reflected origins
- probe: Origin header differentials on the lab replica
- wall: read-only headers

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
