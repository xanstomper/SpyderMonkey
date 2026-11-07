# Debug endpoints inventory

- source canon: `spydermonkey/technique-canon-11.md`
- bindings: **WSTG-CONF** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Common debug paths (__debug__, /debug/, actuator family) probed with the control differential. Decisive test: distinct content vs control = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
