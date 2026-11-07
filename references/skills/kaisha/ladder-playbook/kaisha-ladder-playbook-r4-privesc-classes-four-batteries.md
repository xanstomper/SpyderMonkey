# R4 — privesc classes (four batteries)

- source canon: `kaisha/ladder-playbook.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Rung | Class | The ONE decisive test | Wall |
|---|---|---|---|
| R4a | sudo misconfig | `sudo -l` → match documented NO_PASSWD/safe-echo classes | listed, never executed for gain |
| R4b | SUID/cred-file | SUID + world-readable cred inventory (counts) | paths only, never contents |
| R4c | token/key-reuse | inventory → reuse-check against OWN second host | one shot, reversed |
| R4d | unit/path-trust | systemd unit + PATH inventory → trust classes | read-only, no modification |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
