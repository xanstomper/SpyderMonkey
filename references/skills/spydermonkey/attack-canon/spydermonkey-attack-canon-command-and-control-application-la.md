# Command and Control Application Layer Protocol (T1071)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: C2 over 443/dns/http
- probe: out of family walls entirely
- wall: REFUSED — no C2 infrastructure, ever

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
