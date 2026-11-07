# SSL pinning bypass class (runtime, own app)

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Frida/objection pinning defeats on YOUR OWN app builds — the class writeup maps the app's trust chain. Decisive test: pinning observable and the defeat reproducible on your build.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
