# 2.12 Cache/Web poison quick test (score 55) — windows / low-priv

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-12-cache-web-poison-quick.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **windows** · auth **low-priv** · chain role **pivot**

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- DECISIVE: one request with unkeyed header (`X-Forwarded-Host: evil.com`) on a cacheable path;
  re-fetch plain from another vantage within TTL.
- CONFIRMED WHEN: poisoned content served to the plain fetch. Owned infra: revert = purge.
- FP: CDN strips the header (common) — negative, ledger it.

## Probe adjustment (windows × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
