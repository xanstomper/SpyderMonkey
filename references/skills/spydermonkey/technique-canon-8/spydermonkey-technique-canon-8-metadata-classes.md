# Metadata classes

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-INPV-10** · **CWE-918** · **ATT&CK T1190**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

metadata.google.internal with flavor-header enforcement — the guard's presence/absence IS the row. Decisive test: SSRF probe honoring the header = the posture.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
