# Azure data-plane surface

- source canon: `spydermonkey/cloud-azure-gcp-canon.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-07

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
