# Azure identity surface — chain composition

- source canon: `spydermonkey/cloud-azure-gcp-canon.md`
- base technique: `spydermonkey-cloud-azure-gcp-canon-azure-identity-surface.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
