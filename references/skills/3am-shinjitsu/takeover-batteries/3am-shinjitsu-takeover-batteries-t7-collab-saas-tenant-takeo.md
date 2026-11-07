# T7 — Collab/SaaS tenant takeover

- source canon: `3am-shinjitsu/takeover-batteries.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- OAuth over-grant → full-tenant scope; webhook SSRF → internal admin API; external
  sharing links with elevated defaults; tenant-to-tenant app install (operator-owned
  tenants only); helpdesk trust (documentation only).
- **DECISIVE PROOF:** one read-only tenant-admin API call under the abused grant. Then
  STOP.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
