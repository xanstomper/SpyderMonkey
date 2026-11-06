# PostgreSQL unauth and trust-posture

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

5432 reachable + trust/md5 posture revealed by error text. Decisive test: connection attempt reaching the AUTH stage (not network-refused) — the auth-stage response is the inventory finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
