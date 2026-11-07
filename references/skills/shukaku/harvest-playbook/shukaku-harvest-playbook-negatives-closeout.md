# Negatives & closeout

- source canon: `shukaku/harvest-playbook.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- A finding with no data reach is EXCLUDED with the reason, not padded.
- The SHUKAKU report is the P5 impact layer: register + valuation summary +
  disclosure map + remediation prerequisites (what must happen before the
  organization can call the breach closed).
- Never move data, never copy, never threaten. The register IS the harvest.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
