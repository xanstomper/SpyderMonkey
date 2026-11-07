# Campaign surfaces (authorized only) — gateway / low-priv

- source canon: `spydermonkey/social-canon.md`
- base technique: `spydermonkey-social-canon-campaign-surfaces-authorized-only.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **gateway** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

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

## Probe adjustment (gateway × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
