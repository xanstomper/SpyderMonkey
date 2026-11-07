# SPYDERMONKEY — Social & Phishing Canon (v6.0)

Social-engineering classes for AUTHORIZED engagements — red-team exercises
with written scope. Every simulated-campaign test targets accounts the
operator controls or systems named in the engagement scope. Bindings:
ATT&CK T1566/T1598.

## Campaign surfaces (authorized only)

| Probe | Test | Confirmed-when |
|---|---|---|
| Email gateway | `swaks` authenticity check to OWN mailbox | SPF/DKIM/DMARC alignment |
| SPF posture | `dig TXT spf` (own domain) | permissive mechanisms |
| DMARC policy | `dig TXT _dmarc` (own domain) | p=none / weak |
| DKIM selector | `dig TXT selector._domainkey` (own) | signing gap |
| MTA-STS/BIMI | `dig TXT mta-sts` + bimi (own domain) | no policy = spoofable |
| Open redirects | `nuclei-redirects` on in-scope hosts | redirector candidates |
| Login clone | `evilginx2` on OWN domain (engagement) | 2FA token captured (lab) |
| Attachment macro | `macro_pack` on own doc + lab scanner | AV evasion measured (own) |
| Link crawler | `linkfinder`/`katana` in-scope pages | link inventory |

## Human-layer indicators (OSINT only)

| Probe | Test | Confirmed-when |
|---|---|---|
| Employee footprint | `theHarvester`/`maigret` PUBLIC data in scope | accounts/emails public |
| Breach posture | `h8mail` with own/official corpus (in-scope) | compromised creds (authorized) |
| MFA enrollment | `o365spray` validation mode (documented scope) | mfa absent (auth nt only) |
| Helpdesk vector | engagement scope doc review | social vector allowed by scope |
| Vendor/phish scope | `scope check` on every candidate | in-estate only |

## Simulated-campaign protocol

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