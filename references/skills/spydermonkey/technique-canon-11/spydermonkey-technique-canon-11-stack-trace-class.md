# Stack-trace class

- source canon: `spydermonkey/technique-canon-11.md`
- bindings: **WSTG-BUSL-07** · **CWE-362** · **ATT&CK T1499**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Debug traces on prod errors (canon-IX framework depth). Decisive test: forced error content = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
