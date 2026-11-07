# PHASE 6 — INFRA & DEPENDENCY ROT — chain composition

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-phase-6-infra-dependenc.md`
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

- **External dependency health**: Discord invites (dead + undismissable gate = pre-loaded
  lockout), CDN scripts, widget endpoints, third-party SaaS the target depends on.
- **Software supply chain**: version-disclosed frameworks → known-CVE mapping (with
  exploited-or-not verification, not blind CVE spam).
- **Hot-deploy watch**: asset-size baseline diffs; half-shipped scaffolding (zero-call-site
  gates, {"enabled":false} widgets) cataloged as next-regression surface.
- **Mail/DNS records**: SPF/DMARC/DKIM gaps (spoofing), subdomain takeover via TXT/CNAME.
- Deliverable: rot findings, CVE map, regression-watch list.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
