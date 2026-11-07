# customErrors off class

- source canon: `spydermonkey/technique-canon-9.md`
- bindings: **WSTG-BUSL-07** · **CWE-362** · **ATT&CK T1499**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Stack traces on production errors. Decisive test: forced error page content = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
