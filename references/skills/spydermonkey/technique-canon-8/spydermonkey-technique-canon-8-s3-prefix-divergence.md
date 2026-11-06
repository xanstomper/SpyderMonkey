# S3 prefix divergence

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-CONF-04** · **CWE-732** · **ATT&CK T1530**
- generated: 2026-11-06

## The technique

Public prefix (`/public/*`) with private siblings sharing the bucket policy. Decisive test: anonymous listing at the public prefix vs bucket root — the divergence = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
