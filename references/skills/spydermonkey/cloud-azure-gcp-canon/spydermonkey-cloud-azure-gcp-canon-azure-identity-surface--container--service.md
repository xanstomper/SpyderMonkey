# Azure identity surface — container / service

- source canon: `spydermonkey/cloud-azure-gcp-canon.md`
- base technique: `spydermonkey-cloud-azure-gcp-canon-azure-identity-surface.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **container** · auth **service** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| Tenant inventory | `az account list` (own tenant) | subscription map |
| AAD enumeration | `roadrecon gather` (own tenant) | users/apps/groups graph |
| ROADtools views | `roadrecon auth` + views (own) | privileged roles mapped |
| Dynamic groups | `roadrecon` group analysis (own) | privesc candidates |
| Service principals | `az ad sp list` (own) | dormant sp with rights |
| Application permissions | `az ad app list` + delegated perms (own) | over-scoped apps |
| Cert/secret expiry | `az ad sp credential list` (own) | stale creds alive |
| Conditional access | `az rest` conditional access policies (own) | gaps in mfa coverage |
| Passwordless | `az ad user list` auth methods (own) | weak auth methods |

## Probe adjustment (container × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
