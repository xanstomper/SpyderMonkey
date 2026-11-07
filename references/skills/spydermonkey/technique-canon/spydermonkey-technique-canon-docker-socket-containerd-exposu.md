# Docker socket / containerd exposure

- source canon: `spydermonkey/technique-canon.md`
- bindings: **PTES-CON** · **CWE-250** · **ATT&CK T1611**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Socket mounted or TCP-exposed = full host control class — characterize as the exposure (never execute the escape).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
