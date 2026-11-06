# MySQL unauth and skip-grant residue

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

3306 reachable; error text reveals auth plugin posture. Decisive test: handshake banner + one anonymous connect attempt's error class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
