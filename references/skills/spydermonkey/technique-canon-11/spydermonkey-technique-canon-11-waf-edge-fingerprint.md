# WAF/edge fingerprint

- source canon: `spydermonkey/technique-canon-11.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Malicious-probe detection class and vendor markers in challenge pages. Decisive test: nmap-waf-detect/fingerprint + the challenge anatomy = the posture row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
