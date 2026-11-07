# Exported components and deep-link hijack

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **MASTG-PLATFORM** · **CWE-927** · **ATT&CK T1546**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Exported activities/receivers and deep links accepting foreign intents. Decisive test: manifest analysis + a local intent harness on YOUR build — the hijack shape is the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
