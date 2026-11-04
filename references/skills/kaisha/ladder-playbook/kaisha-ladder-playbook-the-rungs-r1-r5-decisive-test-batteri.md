# The rungs (R1–R5) — decisive-test batteries

- source canon: `kaisha/ladder-playbook.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

### R1 — identity inventory (read-only)
- whoami-class: current principal, groups count (descriptions only)
- key files: `~/.ssh/` count + fingerprints (never private material)
- env markers: count of credential-bearing vars (names only)

### R2 — surface inventory (read-only)
- listening services: address:port + process name (own host)
- banners: exact strings → feed `kaisha cve --banner`

### R3 — era-stack mapping
- banners → era → documented classes → the rung-4 plan inherits the canon

### R4 — privesc classes (four batteries)
| Rung | Class | The ONE decisive test | Wall |
|---|---|---|---|
| R4a | sudo misconfig | `sudo -l` → match documented NO_PASSWD/safe-echo classes | listed, never executed for gain |
| R4b | SUID/cred-file | SUID + world-readable cred inventory (counts) | paths only, never contents |
| R4c | token/key-reuse | inventory → reuse-check against OWN second host | one shot, reversed |
| R4d | unit/path-trust | systemd unit + PATH inventory → trust classes | read-only, no modification |

### R5 — lateral (the top of the ladder)
- Basis: the harvest register's CRED rows + documented reuse classes
  (flaw 10 entropy/forge · seam C auth<->backend-binding)
- The plan: `from → to` on OWN declared hosts only; ONE validation shot each,
  reversed; on CONFIRM the new vantage feeds shukaku (reason → hunt → crown).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
