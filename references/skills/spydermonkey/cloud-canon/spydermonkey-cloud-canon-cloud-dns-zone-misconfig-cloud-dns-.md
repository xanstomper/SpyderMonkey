# Cloud DNS Zone Misconfig (CLOUD-DNS-01)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- generated: 2026-11-07

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: public zone records pointing to deprovisioned services
- probe: the takeover engine — dangling record inventory
- wall: NO-GAIN

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
