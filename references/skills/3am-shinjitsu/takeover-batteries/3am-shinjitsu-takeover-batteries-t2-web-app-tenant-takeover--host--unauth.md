# T2 — Web-app tenant takeover — host / unauth

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-t2-web-app-tenant-takeover.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **host** · auth **unauth** · chain role **final**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Cross-tenant IDOR on tenant-scoped resources; tenant-selection confusion
  (X-Tenant-ID vs Host vs path); schema-library IDs for structural tenant mapping;
  subdomain takeover → cookie-domain capture → session of any user (validate ONLY on
  operator-owned records; external dangling domains = third-party action — document
  feasibility instead).
- **DECISIVE PROOF:** a cross-tenant row read (`content-range: */1` on the foreign
  tenant), or proof-of-control page on an OWNED dangling record. Then STOP.

## Probe adjustment (host × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
