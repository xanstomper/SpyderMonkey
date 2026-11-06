# Express stack-trace class

- source canon: `spydermonkey/technique-canon-9.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-06

## The technique

Error handler dumping stack/cwd/env fragments. Decisive test: forced error on a non-route = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
