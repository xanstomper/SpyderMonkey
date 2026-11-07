# Credentials-over-TLS posture

- source canon: `spydermonkey/technique-canon-11.md`
- bindings: **PTES-PE** · **CWE-522** · **ATT&CK T1555**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Login forms served/posted over http or mixed-content. Decisive test: form action scheme audit from the mirror = the row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
