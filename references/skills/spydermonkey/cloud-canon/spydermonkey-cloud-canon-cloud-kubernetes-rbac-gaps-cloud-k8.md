# Cloud Kubernetes RBAC Gaps (CLOUD-K8S-01)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- class: over-broad service accounts, default SA with verbs
- probe: read-only authn-can-i inventory against the declared cluster
- wall: read-only enumeration, crown the exposure

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
