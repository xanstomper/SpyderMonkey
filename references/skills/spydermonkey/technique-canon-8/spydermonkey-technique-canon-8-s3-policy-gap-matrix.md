# S3 policy-gap matrix

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-CONF-04** · **CWE-732** · **ATT&CK T1530**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Anonymous GET/LIST/PREFIX-divergence and policy-vs-ACL conflict classes. Decisive test: anonymous LIST on the bucket, one object GET — read-only rows.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
