# PHP unserialize pop-chain DNS proof

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-06

## The technique

`unserialize` entry points proven with a DNS-only pop chain (file_put → phar stream wrappers documented as the escalation class). Decisive test: OOB DNS from the phar/jdbc-style wrapper.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
