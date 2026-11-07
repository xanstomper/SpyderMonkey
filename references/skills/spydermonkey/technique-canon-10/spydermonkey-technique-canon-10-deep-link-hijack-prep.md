# Deep-link hijack prep

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **MASTG-PLATFORM** · **CWE-927** · **ATT&CK T1546**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

App links without assetlinks verification. Decisive test: the verification file 404 on the domain = hijack-prep row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
