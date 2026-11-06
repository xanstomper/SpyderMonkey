# CMS staging/debug artifacts

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

debug.log, install.php residual, backup SQL dumps under webroot. Decisive test: control-path differential (never trust a 200 shell) — distinct content = the harvest finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
