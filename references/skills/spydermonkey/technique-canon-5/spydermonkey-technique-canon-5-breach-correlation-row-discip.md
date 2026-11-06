# Breach-correlation row discipline

- source canon: `spydermonkey/technique-canon-5.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-06

## The technique

Leak claims need ROW-LEVEL correlation (the engagement-ops rule): decisive test is `username == masked` AND `display_username == real` on the SAME row — counts alone are hypothesis. Report masked → correlated → unique-id funnel.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
