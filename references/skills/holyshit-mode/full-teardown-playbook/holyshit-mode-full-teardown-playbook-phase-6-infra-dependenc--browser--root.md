# PHASE 6 — INFRA & DEPENDENCY ROT — browser / root

- source canon: `holyshit-mode/full-teardown-playbook.md`
- base technique: `holyshit-mode-full-teardown-playbook-phase-6-infra-dependenc.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **browser** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- **External dependency health**: Discord invites (dead + undismissable gate = pre-loaded
  lockout), CDN scripts, widget endpoints, third-party SaaS the target depends on.
- **Software supply chain**: version-disclosed frameworks → known-CVE mapping (with
  exploited-or-not verification, not blind CVE spam).
- **Hot-deploy watch**: asset-size baseline diffs; half-shipped scaffolding (zero-call-site
  gates, {"enabled":false} widgets) cataloged as next-regression surface.
- **Mail/DNS records**: SPF/DMARC/DKIM gaps (spoofing), subdomain takeover via TXT/CNAME.
- Deliverable: rot findings, CVE map, regression-watch list.

## Probe adjustment (browser × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
