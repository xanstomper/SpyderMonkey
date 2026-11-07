# Campaign surfaces (authorized only)

- source canon: `spydermonkey/social-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
