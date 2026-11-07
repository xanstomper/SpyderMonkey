# Cloud Kubernetes Secret Mounts (CLOUD-K8S-02)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- generated: 2026-11-07

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: secrets mounted where workloads can read — inventory of WHICH
- probe: read-only workload spec inventory
- wall: values never read; names and bindings only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
