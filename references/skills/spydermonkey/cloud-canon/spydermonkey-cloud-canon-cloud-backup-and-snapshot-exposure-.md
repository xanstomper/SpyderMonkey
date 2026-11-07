# Cloud Backup and Snapshot Exposure (CLOUD-OBJ-03)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: public/shared snapshots — the volume class
- probe: read-only snapshot attribute inventory of the declared estate
- wall: values never restored; exposure crowned only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
