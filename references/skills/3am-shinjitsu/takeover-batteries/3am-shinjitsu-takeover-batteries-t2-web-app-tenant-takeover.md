# T2 — Web-app tenant takeover

- source canon: `3am-shinjitsu/takeover-batteries.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

- Cross-tenant IDOR on tenant-scoped resources; tenant-selection confusion
  (X-Tenant-ID vs Host vs path); schema-library IDs for structural tenant mapping;
  subdomain takeover → cookie-domain capture → session of any user (validate ONLY on
  operator-owned records; external dangling domains = third-party action — document
  feasibility instead).
- **DECISIVE PROOF:** a cross-tenant row read (`content-range: */1` on the foreign
  tenant), or proof-of-control page on an OWNED dangling record. Then STOP.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
