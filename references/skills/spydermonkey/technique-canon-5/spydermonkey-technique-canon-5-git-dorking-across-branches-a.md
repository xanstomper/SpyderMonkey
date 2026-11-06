# Git-dorking across branches and dangling objects

- source canon: `spydermonkey/technique-canon-5.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

`git log --all --diff-filter=D`, dangling blobs via rev-list --objects, deleted verify pages recoverable. Decisive test: the recovered object content — provenance-stamped.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
