# Dependency-confusion class

- source canon: `spydermonkey/technique-canon-5.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

Internal package names resolvable from public registries — the CLASS is the name-collision exposure. Decisive test: registry metadata check for an internal-named package (metadata only, never publish) — resolvable = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
