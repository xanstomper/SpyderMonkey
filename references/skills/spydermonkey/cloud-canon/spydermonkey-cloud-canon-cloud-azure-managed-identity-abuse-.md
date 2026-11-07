# Cloud Azure Managed Identity Abuse Surface (CLOUD-AZ-01)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: identity-bearing workloads whose endpoints are exposed
- probe: read-only endpoint + identity surface inventory
- wall: nothing tokened; the exposure is priced

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
