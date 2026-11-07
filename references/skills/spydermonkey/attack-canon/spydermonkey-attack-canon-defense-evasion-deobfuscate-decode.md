# Defense Evasion Deobfuscate/Decode (T1140)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: decoding on the endpoint
- probe: lab replicas decode the encoded probes; prod never runs decode steps
- wall: analysis-only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
