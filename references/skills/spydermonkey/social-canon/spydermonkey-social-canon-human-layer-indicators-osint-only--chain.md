# Human-layer indicators (OSINT only) — chain composition

- source canon: `spydermonkey/social-canon.md`
- base technique: `spydermonkey-social-canon-human-layer-indicators-osint-only.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Probe | Test | Confirmed-when |
|---|---|---|
| Employee footprint | `theHarvester`/`maigret` PUBLIC data in scope | accounts/emails public |
| Breach posture | `h8mail` with own/official corpus (in-scope) | compromised creds (authorized) |
| MFA enrollment | `o365spray` validation mode (documented scope) | mfa absent (auth nt only) |
| Helpdesk vector | engagement scope doc review | social vector allowed by scope |
| Vendor/phish scope | `scope check` on every candidate | in-estate only |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
