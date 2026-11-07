# DNS posture — chain composition

- source canon: `spydermonkey/mail-canon.md`
- base technique: `spydermonkey-mail-canon-dns-posture.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
