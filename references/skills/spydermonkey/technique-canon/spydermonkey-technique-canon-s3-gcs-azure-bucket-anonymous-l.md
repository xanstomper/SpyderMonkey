# S3/GCS/Azure bucket anonymous list

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

Bucket LIST permission without auth is read-only inventory. Decisive test: anonymous LIST (s3 ls / public GET) — the listing = the finding; never write.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
