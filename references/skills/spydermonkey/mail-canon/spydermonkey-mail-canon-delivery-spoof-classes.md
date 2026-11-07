# Delivery & spoof classes

- source canon: `spydermonkey/mail-canon.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Spoof test | `swaks` from own domain to own mailbox | SPF/DKIM/DMARC verdict |
| Lookalike domains | `dnstwist --registered` on own brand | registered lookalikes |
| Typosquat take | `can-i-take-over-xyz` on lookalike | dangling mx/cname |
| Bimi icon | own logo file check | brand abuse surface |
| Google/outlook postmaster | deliverability report (own domain) | spam score data |

Walls: enumeration and probe traffic target the operator's own mail estate.
Auth brute only against accounts the operator controls (their own). No
harvesting, no credential theft from third parties — ever.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
