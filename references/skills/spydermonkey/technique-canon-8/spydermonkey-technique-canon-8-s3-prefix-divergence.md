# S3 prefix divergence

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **WSTG-CONF-04** · **CWE-732** · **ATT&CK T1530**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Public prefix (`/public/*`) with private siblings sharing the bucket policy. Decisive test: anonymous listing at the public prefix vs bucket root — the divergence = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
