# Impact Network Denial of Service (T1498)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- generated: 2026-11-04

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: volumetric DoS
- probe: REFUSED — rate-limit bypass classes are proven with 2 requests, never a flood
- wall: proof = the differential, not the outage

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
