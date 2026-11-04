# Cloud IAM Wildcard Policy (CLOUD-IAM-01)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## The technique

- class: `*` actions/resources in identity policies — the over-privileged principal
- probe: read-only policy inventory for every principal the scope declares
- wall: shukaku hunt semantics — inventory + pricing only, nothing assumed

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
