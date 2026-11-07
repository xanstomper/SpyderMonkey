# SMTP surface — gateway / high-priv

- source canon: `spydermonkey/mail-canon.md`
- base technique: `spydermonkey-mail-canon-smtp-surface.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **gateway** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (gateway × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
