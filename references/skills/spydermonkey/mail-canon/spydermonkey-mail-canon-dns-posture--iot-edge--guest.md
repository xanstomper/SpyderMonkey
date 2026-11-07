# DNS posture — iot-edge / guest

- source canon: `spydermonkey/mail-canon.md`
- base technique: `spydermonkey-mail-canon-dns-posture.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- context: **iot-edge** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: device-adjacent runtime at the edge — own devices, lab network
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

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

## Probe adjustment (iot-edge × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
