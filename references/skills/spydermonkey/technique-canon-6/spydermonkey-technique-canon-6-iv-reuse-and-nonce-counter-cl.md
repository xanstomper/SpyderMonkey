# IV reuse and nonce-counter classes

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

Deterministic ciphertext prefixes across messages (ECB-class visual repetition) and IV/nonce reuse detectable from ciphertext pairs of YOUR OWN test material. Decisive test: two same-prefix plaintexts → ciphertext prefix delta (ECB) or equality (IV reuse).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
