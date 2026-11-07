# Cloud Object Storage Public Exposure (CLOUD-OBJ-01)

- source canon: `spydermonkey/cloud-canon.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: buckets/containers readable or listable by anyone
- probe: unauthenticated listing + reference probes against the declared estate
- wall: read-only; the HARVEST class rules — files are listed, never downloaded beyond the proof

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
