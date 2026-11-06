# Logs secret echo

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## The technique

Logcat echoing tokens/PII during normal use (SPY-532 canon). Decisive test: logcat capture during one action — the echoed secret = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
