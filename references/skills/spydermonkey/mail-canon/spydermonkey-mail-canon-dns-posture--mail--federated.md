# DNS posture — mail / federated

- source canon: `spydermonkey/mail-canon.md`
- base technique: `spydermonkey-mail-canon-dns-posture.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- context: **mail** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

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

## Probe adjustment (mail × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
