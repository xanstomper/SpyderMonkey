# CSP absent / base-uri + script-src gaps

- source canon: `spydermonkey/technique-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

CSP missing base-uri or allowing script-src with a JSONP/file-upload host = injectable. Decisive test: CSP header parse + one blocked/allowed probe — the header itself is the finding when dangerous sinks exist.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
