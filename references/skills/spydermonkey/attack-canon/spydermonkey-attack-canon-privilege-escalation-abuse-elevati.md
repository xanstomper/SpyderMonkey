# Privilege Escalation Abuse Elevation Control (T1548)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: sudo/sudoers misconfiguration abuse
- probe: `sudo -n -l` inventory — what can THIS principal do
- wall: read-only; rung climbing stops at the exposure statement (kaisha)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
