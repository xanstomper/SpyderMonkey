# DNS posture

- source canon: `spydermonkey/mail-canon.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- generated: 2026-11-07

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
