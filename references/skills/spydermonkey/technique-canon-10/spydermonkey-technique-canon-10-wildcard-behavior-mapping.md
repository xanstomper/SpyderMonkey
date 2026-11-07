# Wildcard behavior mapping

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Wildcard responses masking enumeration — the wildcard-detection discipline (fierce/dnswalk canon). Decisive test: random-label response uniformity = the negative/positive row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
