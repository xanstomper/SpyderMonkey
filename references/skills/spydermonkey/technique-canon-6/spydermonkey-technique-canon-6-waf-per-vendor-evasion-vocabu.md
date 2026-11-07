# WAF per-vendor evasion vocabulary (documented classes)

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

The encoding vocabulary exists FOR the WAF tier (canon-I hardened state): double-encode, unicode, case-split, comment-split — one variant per request, the differential must clear WITHOUT tripping. Decisive test: variant-acceptance vs WAF-flag delta on your own benign probe.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
