# Simulated-campaign protocol

- source canon: `spydermonkey/social-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Scope triple-check | mandate + scope.json + written authorization | all three present |
| Noise budget | campaign plan caps sends/hour | within budget |
| Consent tokens | recipient list includes opt-in flags | explicit consent |
| Proof of click | landing page logs only click+no-gain | click confirmed, nothing taken |
| Reporting | `report` includes campaign rows | chain closed in ledger |

Walls: no real credentials are harvested, no real sessions hijacked — the
campaign proves reachability/click rates within the authorized scope and
stops. Recipients outside the declared engagement = the wall (rc=1). The
family NEVER conducts phishing against third parties.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
