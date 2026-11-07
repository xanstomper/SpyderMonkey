# T4 — Cloud account takeover

- source canon: `3am-shinjitsu/takeover-batteries.md`
- bindings: **WSTG-INPV-10** · **CWE-918** · **ATT&CK T1190**
- generated: 2026-11-04

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Secret leak → `sts get-caller-identity` success in the target account; bucket/object
  keys → deeper IAM; metadata/SSRF → instance role credential (one `get-caller-identity`,
  owned infra only for the decisive call); exposed snapshot/AMI → root volume → secrets;
  OIDC federation misconfig (documented-PoC); over-scoped service principals.
- **DECISIVE PROOF:** the harvested identity resolves to the target account and lists
  one resource. Then STOP.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
