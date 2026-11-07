# DNSSEC and CAA absence

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-CONF** · **CWE-693** · **ATT&CK T1014**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Unsigned zones and missing CAA = issuance-posture classes. Decisive test: record lookups — the absence documented as the posture row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
