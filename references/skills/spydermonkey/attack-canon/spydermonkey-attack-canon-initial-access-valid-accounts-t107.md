# Initial Access Valid Accounts (T1078)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **PTES-PE** · **CWE-522** · **ATT&CK T1555**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: default/leaked/reused credentials
- probe: only credentials the SCOPE FILE declares; never a live brute against prod
- wall: brute classes run against the dojo replica; prod runs are refusals

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
