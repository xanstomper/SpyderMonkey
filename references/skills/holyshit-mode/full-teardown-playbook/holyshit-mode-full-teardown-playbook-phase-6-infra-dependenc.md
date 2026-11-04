# PHASE 6 — INFRA & DEPENDENCY ROT

- source canon: `holyshit-mode/full-teardown-playbook.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

- **External dependency health**: Discord invites (dead + undismissable gate = pre-loaded
  lockout), CDN scripts, widget endpoints, third-party SaaS the target depends on.
- **Software supply chain**: version-disclosed frameworks → known-CVE mapping (with
  exploited-or-not verification, not blind CVE spam).
- **Hot-deploy watch**: asset-size baseline diffs; half-shipped scaffolding (zero-call-site
  gates, {"enabled":false} widgets) cataloged as next-regression surface.
- **Mail/DNS records**: SPF/DMARC/DKIM gaps (spoofing), subdomain takeover via TXT/CNAME.
- Deliverable: rot findings, CVE map, regression-watch list.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
