# SPYDERMONKEY — Domain Takeover Canon (v6.0)

Subdomain takeover classes as read-only decisive tests — dangling DNS records
on the operator's OWN domains or in-scope estate. Bindings: ATT&CK T1584 ·
CWE-350.

## Fingerprint inventory

| Probe | Test | Confirmed-when |
|---|---|---|
| CNAME map | `dnsx -cname` (own domains) | cname rows collected |
| Provider check | `can-i-take-over-xyz` lookup on cname target | provider in takeover table |
| Status code | `httpx -sc` on the host | 404/NoSuchBucket signatures |
| Edge cert | `tlsx -san -cn` on the host | cert for dead service |
| NS delegation | `dig NS` on dangling sub (own) | delegated but dead |
| Mail takeover | `dig MX` on sub (own) | mx name claimable |
| Service tick | probe service endpoint (own sub) | claimable marker |

## Takeover classes

| Probe | Test | Confirmed-when |
|---|---|---|
| AWS S3 bucket | `s3scanner` check bucket name == cname (own) | bucket missing/claimable |
| Azure blob | `az storage container` existence probe (own) | container absent |
| GitHub pages | `curl` expected 404 signature (own) | pages site dormant |
| Heroku/Glitch | status code + body fingerprint (own) | app name free |
| Elastic IP | `whois`/`ipinfo` on cname (own) | eip released |
| Shopify/Wordpress | fingerprint strings (own) | storename claimable |
| Zendesk/Cargo | body markers (own) | subdomain free |
| Dead CDN | edge cert + 526/530 codes (own) | origin missing |

## Verification discipline

| Probe | Test | Confirmed-when |
|---|---|---|
| Scope gate | `scope check` on every candidate fqdn | in estate |
| No registration | candidate recorded, NEVER registered (unless disclosed) | ledger row, no claim |
| Owner contact | `whois` owner == operator/estate | ownership confirmed |
| Disclosure path | engagement report row for each candidate | documented |

Walls: a confirmed claimable subdomain is a FINDING, not a prize: the family
registers nothing on third-party names without written authorization —
verification is a fingerprint + ledger row, never an actual takeover of a
domain outside the engagement.