# The harvest surface (GET-only, `hunt --live`)

- source canon: `shukaku/harvest-playbook.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

backup archives (`backup.zip|tar.gz|sql`, `dump.sql`, `db.sqlite`…), env/config
leaks (`.env`, `.git/config`, `config.*.bak`), admin/admin-export paths,
`api/export(s)`, `debug/vars`, `server-status`. Data plane only — route probing is
UNDERCROFT's. 200s register CONFIRMED with body sizes; **nothing is downloaded**.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
