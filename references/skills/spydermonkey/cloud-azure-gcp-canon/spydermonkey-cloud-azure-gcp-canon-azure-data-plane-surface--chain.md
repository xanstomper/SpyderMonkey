# Azure data-plane surface — chain composition

- source canon: `spydermonkey/cloud-azure-gcp-canon.md`
- base technique: `spydermonkey-cloud-azure-gcp-canon-azure-data-plane-surface.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Probe | Test | Confirmed-when |
|---|---|---|
| Storage ACLs | `az storage account list` + container ACL (own) | public containers |
| SAS posture | `az storage account show` sas policy (own) | long-lived SAS |
| Key vault config | `az keyvault list` + RBAC (own) | vault accessible to sp |
| VM extensions | `az vm list` + extension inventory (own) | unsafe extensions |
| Managed identity | own VM managed identity → `az` token check (own) | MIMITM surface |
| Function apps | `az functionapp list` (own) | plaintext settings |
| Logic apps | `az logic workflow list` (own) | sensitive connectors |
| App service slots | `az webapp list` (own) | staging slot exposure |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
