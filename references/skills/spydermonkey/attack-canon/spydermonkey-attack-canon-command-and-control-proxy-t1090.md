# Command and Control Proxy (T1090)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: tunneling through proxies
- probe: the family maps proxy headers (x-forwarded chains) as inventory only
- wall: read-only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
