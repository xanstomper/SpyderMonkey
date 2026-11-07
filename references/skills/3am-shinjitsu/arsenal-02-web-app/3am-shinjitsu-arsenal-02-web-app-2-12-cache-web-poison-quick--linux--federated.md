# 2.12 Cache/Web poison quick test (score 55) — linux / federated

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-12-cache-web-poison-quick.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **linux** · auth **federated** · chain role **pivot**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: read-only inventory first (kaisha rungs), then the documented class match
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- DECISIVE: one request with unkeyed header (`X-Forwarded-Host: evil.com`) on a cacheable path;
  re-fetch plain from another vantage within TTL.
- CONFIRMED WHEN: poisoned content served to the plain fetch. Owned infra: revert = purge.
- FP: CDN strips the header (common) — negative, ledger it.

## Probe adjustment (linux × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
