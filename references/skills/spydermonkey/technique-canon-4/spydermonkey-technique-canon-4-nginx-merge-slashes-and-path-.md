# Nginx merge_slashes and path normalization differentials

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

merge_slashes off plus auth-by-location lets //admin bypass location checks. Decisive test: doubled-slash and %-decoded variants of a protected path — one variant 200s where the canonical 401s = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
