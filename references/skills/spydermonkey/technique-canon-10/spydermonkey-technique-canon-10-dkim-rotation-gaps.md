# DKIM rotation gaps

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Stale selectors and missing rotation (canon-III at depth). Decisive test: selector sweep + published-key size = the row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
