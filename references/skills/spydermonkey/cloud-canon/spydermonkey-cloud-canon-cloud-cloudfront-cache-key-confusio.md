# Cloud CloudFront Cache Key Confusion (CLOUD-EDGE-02)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **WSTG-ADV-01** · **CWE-444** · **ATT&CK T1190**
- generated: 2026-11-04

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: unkeyed headers/params changing the cached object
- probe: lab replica — the caching differential with harmless markers
- wall: lab only; prod cache is never poisoned

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
