# Simulated-campaign protocol — chain composition

- source canon: `spydermonkey/social-canon.md`
- base technique: `spydermonkey-social-canon-simulated-campaign-protocol.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
