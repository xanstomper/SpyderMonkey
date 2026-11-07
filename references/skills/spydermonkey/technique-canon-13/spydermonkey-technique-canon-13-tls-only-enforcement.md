# TLS-only enforcement

- source canon: `spydermonkey/technique-canon-13.md`
- bindings: **WSTG-INPV-06** · **CWE-601** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

http→https redirect + HSTS on every tier. Decisive test: the http variant serving content = the absence.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
