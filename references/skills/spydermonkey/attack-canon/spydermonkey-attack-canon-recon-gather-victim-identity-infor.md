# Recon Gather Victim Identity Information (T1589)

- source canon: `spydermonkey/attack-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- class: email formats, employee names, SSO portals, password policies visible pre-auth
- probe: harvest from public pages + error strings; enumerate the auth surface's hints
- wall: passive-first; no account interaction beyond what scope declares

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
