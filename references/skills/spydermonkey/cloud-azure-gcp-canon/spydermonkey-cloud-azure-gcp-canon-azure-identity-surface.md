# Azure identity surface

- source canon: `spydermonkey/cloud-azure-gcp-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
