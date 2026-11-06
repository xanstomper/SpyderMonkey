# Magic-link entropy and single-use semantics

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

Magic login links with short token entropy or replayable semantics are the passwordless brute. Decisive test: request two links, compare token structure/entropy (e.g. 22-char base62 ≈ 128-bit = NOT enumerable — bank the negative), and replay the consumed link for a second auth.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
