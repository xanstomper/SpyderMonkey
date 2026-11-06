# Kafka anonymous and advertised-config leak

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

PLAINTEXT listeners unauth metadata reads. Decisive test: metadata fetch listing topics — the topic inventory = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
