# Human-layer indicators (OSINT only) — cloud / root

- source canon: `spydermonkey/social-canon.md`
- base technique: `spydermonkey-social-canon-human-layer-indicators-osint-only.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **cloud** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Employee footprint | `theHarvester`/`maigret` PUBLIC data in scope | accounts/emails public |
| Breach posture | `h8mail` with own/official corpus (in-scope) | compromised creds (authorized) |
| MFA enrollment | `o365spray` validation mode (documented scope) | mfa absent (auth nt only) |
| Helpdesk vector | engagement scope doc review | social vector allowed by scope |
| Vendor/phish scope | `scope check` on every candidate | in-estate only |

## Probe adjustment (cloud × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
