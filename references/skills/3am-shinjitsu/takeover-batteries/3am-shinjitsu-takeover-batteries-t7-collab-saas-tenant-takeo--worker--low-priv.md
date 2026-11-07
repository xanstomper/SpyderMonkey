# T7 — Collab/SaaS tenant takeover — worker / low-priv

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-t7-collab-saas-tenant-takeo.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **worker** · auth **low-priv** · chain role **final**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- OAuth over-grant → full-tenant scope; webhook SSRF → internal admin API; external
  sharing links with elevated defaults; tenant-to-tenant app install (operator-owned
  tenants only); helpdesk trust (documentation only).
- **DECISIVE PROOF:** one read-only tenant-admin API call under the abused grant. Then
  STOP.

## Probe adjustment (worker × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
