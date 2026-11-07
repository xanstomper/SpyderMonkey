# Cloud CloudTrail/Log Coverage Gaps (CLOUD-DET-01)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- generated: 2026-11-04

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: regions/actions without logging — the blind spot map
- probe: read-only trail config inventory
- wall: the finding is the gap, not an action in the gap

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
