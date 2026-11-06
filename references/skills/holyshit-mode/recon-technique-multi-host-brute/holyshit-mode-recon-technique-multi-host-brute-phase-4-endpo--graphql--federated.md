# Phase 4: Endpoint Fingerprinting — graphql / federated

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- base technique: `holyshit-mode-recon-technique-multi-host-brute-phase-4-endpo.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **graphql** · auth **federated** · chain role **entry**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- `/api/dashboard` → 200 unauth, 55KB stale telemetry (aggregate node health — no client IP logs)
- JS bundle revealed password-gated endpoints:
  - `x-refresh-password` → `/api/dashboard?refresh=1` (cache-bust)
  - `x-export-password` → `/api/export?days=N` (full data export)
- Both are shared secrets stored in sessionStorage (NOT per-user tokens)

## Probe adjustment (graphql × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- opens the kill chain (first blood) — pairs with the info/harvest/recon findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
