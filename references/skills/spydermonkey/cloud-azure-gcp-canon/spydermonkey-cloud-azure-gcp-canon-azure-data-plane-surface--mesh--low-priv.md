# Azure data-plane surface — mesh / low-priv

- source canon: `spydermonkey/cloud-azure-gcp-canon.md`
- base technique: `spydermonkey-cloud-azure-gcp-canon-azure-data-plane-surface.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **mesh** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

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

## Probe adjustment (mesh × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
