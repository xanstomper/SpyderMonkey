# Campaign surfaces (authorized only) — worker / machine

- source canon: `spydermonkey/social-canon.md`
- base technique: `spydermonkey-social-canon-campaign-surfaces-authorized-only.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **worker** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (worker × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
