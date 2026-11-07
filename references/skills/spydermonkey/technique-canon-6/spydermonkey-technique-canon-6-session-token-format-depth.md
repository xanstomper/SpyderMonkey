# Session-token format depth

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Opaque-token structure decoding (canon-I), JWT families (canon-II), PASETO/other formats misused, cross-tier token sharing. Decisive test: token decode + cross-tier acceptance probe on your own tokens.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
