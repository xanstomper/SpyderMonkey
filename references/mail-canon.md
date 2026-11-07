# SPYDERMONKEY — Mail Canon (v6.0)

Email-infrastructure classes as read-only decisive tests on the operator's
OWN domains/infrastructure (or in-scope estate). Bindings: ATT&CK T1078/T1566
· WSTG applayer.

## DNS posture

| Probe | Test | Confirmed-when |
|---|---|---|
| MX map | `dig MX` (own domain) | mail gateway inventory |
| SPF parse | `dig TXT` → `spf-tools` flatten (own) | ~all / +all present |
| DMARC policy | `dig TXT _dmarc.<d>` (own) | p=none / rua missing |
| DKIM selectors | `dig TXT s1._domainkey` common selectors (own) | signing key missing |
| BIMI | `dig TXT default._bimi.<d>` (own) | no logo record |
| MTA-STS | `dig TXT mta-sts.<d>` + `https://mta-sts.<d>` (own) | no policy file |
| DANE | `dig TLSA _25._tcp.mx` (own) | no TLSA records |
| Subdomain mail | `dnsx` on own domains | mail.* variants |

## SMTP surface

| Probe | Test | Confirmed-when |
|---|---|---|
| Banner | `swaks --server mx` (own mx) | version string |
| Open relay | `swaks` test to own mx with foreign rcpt | relay accepted (own) |
| User enum | `smtp-user-enum VRFY/EXPN` (documented scope) | vrfy accepted |
| STARTTLS | `tlsx -starttls` on own mx | starttls advertised |
| Cipher posture | `testssl --starttls smtp` (own mx) | weak suites |
| Auth brute | `hydra -s 25` (documented scope) | weak creds found |
| Header injection | `swaks` crafted headers to own mailbox | injection reflected (lab) |
| Quota/backscatter | send to own nonexistent user | bounce pattern |

## Delivery & spoof classes

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