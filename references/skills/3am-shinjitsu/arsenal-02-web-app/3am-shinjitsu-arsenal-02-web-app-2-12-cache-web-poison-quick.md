# 2.12 Cache/Web poison quick test (score 55)

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- DECISIVE: one request with unkeyed header (`X-Forwarded-Host: evil.com`) on a cacheable path;
  re-fetch plain from another vantage within TTL.
- CONFIRMED WHEN: poisoned content served to the plain fetch. Owned infra: revert = purge.
- FP: CDN strips the header (common) — negative, ledger it.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
