# SMTP surface — chain composition

- source canon: `spydermonkey/mail-canon.md`
- base technique: `spydermonkey-mail-canon-smtp-surface.md`
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
| Banner | `swaks --server mx` (own mx) | version string |
| Open relay | `swaks` test to own mx with foreign rcpt | relay accepted (own) |
| User enum | `smtp-user-enum VRFY/EXPN` (documented scope) | vrfy accepted |
| STARTTLS | `tlsx -starttls` on own mx | starttls advertised |
| Cipher posture | `testssl --starttls smtp` (own mx) | weak suites |
| Auth brute | `hydra -s 25` (documented scope) | weak creds found |
| Header injection | `swaks` crafted headers to own mailbox | injection reflected (lab) |
| Quota/backscatter | send to own nonexistent user | bounce pattern |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
