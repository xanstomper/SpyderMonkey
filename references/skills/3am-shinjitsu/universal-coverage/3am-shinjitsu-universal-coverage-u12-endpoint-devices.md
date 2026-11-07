# U12 Endpoint & devices

- source canon: `3am-shinjitsu/universal-coverage.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- generated: 2026-11-07

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- [ ] Managed fleet enrollment, patch level, EOL software, EDR and disk encryption audited
- [ ] Privileged local accounts, cached credentials, and remote access tooling reviewed
- [ ] Network device configs/secrets/firmware/AAA/TACACS/RADIUS reviewed
- [ ] IoT/OT inventory, segmentation, default credentials, and fail-safe behavior reviewed
- [ ] Physical access / RFID / badge systems are documentation only unless explicit RoE

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
