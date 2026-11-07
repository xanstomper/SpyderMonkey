# S3 policy-gap classes

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-CONF-04** · **CWE-732** · **ATT&CK T1530**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Anonymous GET/LIST on bucket or prefix; ACL vs policy divergence; public-CDN origin overlap. Decisive test: anonymous LIST/GET one object (read-only) — the listing is the finding; never PUT/DELETE.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
