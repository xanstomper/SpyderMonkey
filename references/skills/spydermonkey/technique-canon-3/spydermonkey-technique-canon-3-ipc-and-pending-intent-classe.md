# IPC and pending-intent classes

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-06

## The technique

Implicit intents/pending intents carrying sensitive data between exported components. Decisive test: intent interception in your harness — the data path is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
