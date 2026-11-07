# Impact Data Destruction (T1485)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: wiping victim data
- probe: ABSOLUTE REFUSAL — this is the family's hardest wall
- wall: no code path exists that reaches this class

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
