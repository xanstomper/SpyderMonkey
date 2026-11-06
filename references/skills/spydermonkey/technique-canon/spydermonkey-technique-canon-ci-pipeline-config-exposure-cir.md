# CI pipeline config exposure (.circleci/.github workflows)

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-CONF-04** · **CWE-538** · **ATT&CK T1552**
- generated: 2026-11-06

## The technique

Runner configs with secrets referenced (not values) map the secret inventory. Decisive test: workflow YAML naming secrets + the pull-request trigger surface = the supply-chain finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
