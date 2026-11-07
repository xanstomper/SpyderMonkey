# Geoblocking/WAF-tier inconsistency

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **PTES-OPSEC** · **CWE-200** · **ATT&CK T1070**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Differential treatment by region/ASN (the partial-remediation drift class, SPY-096): a 503-gated transport with a still-200 sibling mint = partial closure. Decisive test: same probe, two regions/ASNs on the sanctioned vantages — the matrix is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
