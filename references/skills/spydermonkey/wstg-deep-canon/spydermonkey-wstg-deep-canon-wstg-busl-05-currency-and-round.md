# WSTG-BUSL-05 Currency and Rounding

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: rounding direction, currency confusion
- probe: boundary quantities on the lab replica; the math differential is the proof
- wall: lab replica

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
