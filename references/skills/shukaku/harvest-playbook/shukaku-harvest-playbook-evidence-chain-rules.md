# Evidence-chain rules

- source canon: `shukaku/harvest-playbook.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

1. Every crown entry: `SOURCE → PROOF → SCOPE → CLASS → VALUE → DISCLOSE`.
2. SOURCE must be a real finding ID (3AM chain, case file, ledger entry) — a harvest
   entry with no source is a fabrication.
3. PROOF must be reproducible read-only (command ref, output hash reference).
4. SCOPE is counts, never contents; samples ≤3, redacted, hashed.
5. VALUE carries basis; DISCLOSE carries the obligation + timeline + prerequisite.
6. Re-verify reach before re-asserting (drift first; findings decay).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
