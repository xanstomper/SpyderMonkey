# Cloud Container Registry Exposure (CLOUD-REG-01)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- class: anonymous pull of images — layers leak source/secrets
- probe: unauth manifest read of the declared registry; layer inventory only
- wall: NO-GAIN — layers are inventoried, not mined wholesale

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
