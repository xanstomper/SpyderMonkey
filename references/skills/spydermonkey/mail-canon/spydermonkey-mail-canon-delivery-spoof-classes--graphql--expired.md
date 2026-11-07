# Delivery & spoof classes — graphql / expired

- source canon: `spydermonkey/mail-canon.md`
- base technique: `spydermonkey-mail-canon-delivery-spoof-classes.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **graphql** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Spoof test | `swaks` from own domain to own mailbox | SPF/DKIM/DMARC verdict |
| Lookalike domains | `dnstwist --registered` on own brand | registered lookalikes |
| Typosquat take | `can-i-take-over-xyz` on lookalike | dangling mx/cname |
| Bimi icon | own logo file check | brand abuse surface |
| Google/outlook postmaster | deliverability report (own domain) | spam score data |

Walls: enumeration and probe traffic target the operator's own mail estate.
Auth brute only against accounts the operator controls (their own). No
harvesting, no credential theft from third parties — ever.

## Probe adjustment (graphql × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
