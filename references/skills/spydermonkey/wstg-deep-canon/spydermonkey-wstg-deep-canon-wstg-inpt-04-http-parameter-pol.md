# WSTG-INPT-04 HTTP Parameter Pollution

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **WSTG-BUSL-02** · **CWE-840** · **ATT&CK T1565**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: duplicate params — parser disagreement between tiers
- probe: duplicated keys with different values; the DIFFERENT parsed value is the proof
- wall: lab replica

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
