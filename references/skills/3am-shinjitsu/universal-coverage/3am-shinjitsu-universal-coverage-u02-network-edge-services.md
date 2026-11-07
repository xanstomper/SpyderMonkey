# U02 Network edge & services

- source canon: `3am-shinjitsu/universal-coverage.md`
- bindings: **WSTG-ADV-01** · **CWE-444** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- [ ] Live services and versions inventoried from banners/config, not guesswork
- [ ] EOL/default/unpatched edge and admin planes identified
- [ ] Exposure of admin/DB/queue/cache/monitoring ports checked
- [ ] VPN/firewall/SSH/RDP policy and MFA coverage reviewed
- [ ] Segmentation and management-plane isolation verified

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
