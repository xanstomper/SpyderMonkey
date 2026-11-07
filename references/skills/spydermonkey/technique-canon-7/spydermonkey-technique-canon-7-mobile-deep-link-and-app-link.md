# Mobile deep-link and app-link hijack (depth)

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **MASTG-PLATFORM** · **CWE-927** · **ATT&CK T1546**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

App-links without domain verification (assetlinks absent) = hijack-prep. Decisive test: the verification file's absence on the domain — 404/missing = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
