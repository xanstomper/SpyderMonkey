# SMTP surface — wireless / guest

- source canon: `spydermonkey/mail-canon.md`
- base technique: `spydermonkey-mail-canon-smtp-surface.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **wireless** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: LAB-ONLY — your own radios and stations; third-party airwaves are the absolute wall
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

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

## Probe adjustment (wireless × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
