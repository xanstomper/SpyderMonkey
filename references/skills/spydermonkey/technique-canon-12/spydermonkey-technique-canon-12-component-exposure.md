# Component exposure

- source canon: `spydermonkey/technique-canon-12.md`
- bindings: **MASTG-PLATFORM** · **CWE-927** · **ATT&CK T1546**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Exported activities/receivers/providers/deep-links (canon-X). Decisive test: the harness invocation = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
