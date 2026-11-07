# CI pipeline config exposure (.circleci/.github workflows)

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-CONF-04** · **CWE-538** · **ATT&CK T1552**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Runner configs with secrets referenced (not values) map the secret inventory. Decisive test: workflow YAML naming secrets + the pull-request trigger surface = the supply-chain finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
