# 7.4 Dependency confusion (score 80, OWNED namespace only)

- source canon: `3am-shinjitsu/arsenal-07-supply-chain.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## The technique

- Operator's private package names probed on public registries (npm/PyPI) — availability =
  confusion primitive. Typosquat detection on the operator's brand names.
- Workflow: query registry, never publish/register anything.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
