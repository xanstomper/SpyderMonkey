# WSTG-ERRH-01 Error Code and Message Analysis

- source canon: `spydermonkey/wstg-deep-canon.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- generated: 2026-11-04

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: stack traces, sql fragments, paths in errors
- probe: malformed inputs forcing 500s on the lab replica; harvest the trace class
- wall: read-only

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
