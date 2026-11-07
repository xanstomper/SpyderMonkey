# CMS staging/debug artifacts

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

debug.log, install.php residual, backup SQL dumps under webroot. Decisive test: control-path differential (never trust a 200 shell) — distinct content = the harvest finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
