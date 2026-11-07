# Cache-key manipulation at CDN tiers

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-ADV-01** · **CWE-444** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Vary/Age/Cache-Control behaviors, query-string normalization gaps — the poisoning/deception family (canon-I) at the CDN layer. Decisive test: header telemetry over paced requests — the cache-key model is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
