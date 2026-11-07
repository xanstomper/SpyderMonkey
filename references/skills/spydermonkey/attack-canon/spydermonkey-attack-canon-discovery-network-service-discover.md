# Discovery Network Service Discovery (T1046)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-ATHN-04** · **CWE-307** · **ATT&CK T1110**
- generated: 2026-11-07

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: service/port enumeration
- probe: scope-bounded sweep, rate-capped
- wall: out-of-scope hosts refuse at the socket layer

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
