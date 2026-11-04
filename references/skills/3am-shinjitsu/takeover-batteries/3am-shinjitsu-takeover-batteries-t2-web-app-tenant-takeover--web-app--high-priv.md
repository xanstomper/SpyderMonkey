# T2 — Web-app tenant takeover — web-app / high-priv

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-t2-web-app-tenant-takeover.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **web-app** · auth **high-priv** · chain role **final**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Cross-tenant IDOR on tenant-scoped resources; tenant-selection confusion
  (X-Tenant-ID vs Host vs path); schema-library IDs for structural tenant mapping;
  subdomain takeover → cookie-domain capture → session of any user (validate ONLY on
  operator-owned records; external dangling domains = third-party action — document
  feasibility instead).
- **DECISIVE PROOF:** a cross-tenant row read (`content-range: */1` on the foreign
  tenant), or proof-of-control page on an OWNED dangling record. Then STOP.

## Probe adjustment (web-app × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
