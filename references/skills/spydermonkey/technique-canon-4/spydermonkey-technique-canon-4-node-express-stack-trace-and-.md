# Node/Express stack-trace and source disclosure

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Error handlers dumping stack + cwd, sourcemaps (already canon-I), .map on chunk files. Decisive test: forced error on a non-route — stack text with paths = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
