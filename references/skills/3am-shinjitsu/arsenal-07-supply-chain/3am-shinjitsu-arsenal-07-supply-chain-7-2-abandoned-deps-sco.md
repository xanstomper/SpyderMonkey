# 7.2 Abandoned deps (score 70)

- source canon: `3am-shinjitsu/arsenal-07-supply-chain.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

- Bundle imports of unmaintained libs (last release >2y) with known CVE classes; dead CDN
  scripts (→ §5.6 hijackable references); `@deprecated` admin scaffolding left deployed.
- DECISIVE: version pin in lockfile/bundle header → advisory cross-check.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
