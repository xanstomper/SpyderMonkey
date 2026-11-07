# Delivery & spoof classes — worker / guest

- source canon: `spydermonkey/mail-canon.md`
- base technique: `spydermonkey-mail-canon-delivery-spoof-classes.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **worker** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

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

## Probe adjustment (worker × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
