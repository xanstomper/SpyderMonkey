# Dangling/superseded client versions

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

Older app versions still served (APK mirrors, cached chunks) exposing retired endpoints/auth shapes. Decisive test: old-version bundle diff against live — retired-surface presence = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
