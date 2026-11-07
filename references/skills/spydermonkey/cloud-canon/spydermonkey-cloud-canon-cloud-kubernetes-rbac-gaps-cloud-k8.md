# Cloud Kubernetes RBAC Gaps (CLOUD-K8S-01)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: over-broad service accounts, default SA with verbs
- probe: read-only authn-can-i inventory against the declared cluster
- wall: read-only enumeration, crown the exposure

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
