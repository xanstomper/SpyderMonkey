# R1 — identity inventory (read-only)

- source canon: `kaisha/ladder-playbook.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- whoami-class: current principal, groups count (descriptions only)
- key files: `~/.ssh/` count + fingerprints (never private material)
- env markers: count of credential-bearing vars (names only)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
