# XS-Leaks (error/timing/referrer oracles)

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Response-length, status-error, and frame-count oracles reading cross-origin state. Decisive test: the oracle's binary answer about YOUR OWN two records — the measurable delta is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
