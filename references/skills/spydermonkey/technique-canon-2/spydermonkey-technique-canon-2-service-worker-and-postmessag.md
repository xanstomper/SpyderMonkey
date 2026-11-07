# Service-worker and postMessage depth

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

SW scope hijack class (register SW from a writable path) and postMessage targetOrigin='*' with sensitive payloads. Decisive test: message received from YOUR origin — the acceptance IS the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
