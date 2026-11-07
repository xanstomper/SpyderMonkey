# Simulated-campaign protocol — mesh / guest

- source canon: `spydermonkey/social-canon.md`
- base technique: `spydermonkey-social-canon-simulated-campaign-protocol.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **mesh** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

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

## Probe adjustment (mesh × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
