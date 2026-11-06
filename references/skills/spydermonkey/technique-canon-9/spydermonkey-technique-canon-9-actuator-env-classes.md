# Actuator env classes

- source canon: `spydermonkey/technique-canon-9.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-06

## The technique

/env /actuator/env returning config with secrets masked-or-not. Decisive test: response key inventory — unmasked secret keys = the crown.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
