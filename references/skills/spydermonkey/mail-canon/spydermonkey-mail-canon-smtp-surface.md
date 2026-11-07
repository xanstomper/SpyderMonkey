# SMTP surface

- source canon: `spydermonkey/mail-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
