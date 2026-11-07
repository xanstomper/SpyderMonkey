# SPYDERMONKEY — Cloud Canon: Azure & GCP (v6.0)

Azure/GCP security classes as read-only decisive tests in the OPERATOR'S OWN
tenant/subscriptions/projects (or in-scope estate). Bindings: ATT&CK
T1526/T1580 · CWE-732.

## Azure identity surface

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

## Azure data-plane surface

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

## GCP identity surface

| Probe | Test | Confirmed-when |
|---|---|---|
| Project inventory | `gcloud projects list` (own org) | project map |
| IAM bindings | `gcloud projects get-iam-policy` (own) | over-privileged SA/roles |
| SA keys | `gcloud iam service-accounts keys list` (own) | long-lived keys |
| KMS posture | `gcloud kms keys list` (own) | auto-rotation off |
| Org policies | `gcloud org-policies list` (own) | constrains gaps |
| Audit logs | `gcloud logging read` own project | no audit enabled |
| GKE RBAC | `gcloud container clusters describe` (own) | workload identity gaps |
| Cloud functions | `gcloud functions list` (own) | plaintext env vars |

## Cross-cloud attack paths (own estate)

| Probe | Test | Confirmed-when |
|---|---|---|
| Cloud_enum | `cloud_enum -k` (own org) | exposed buckets/domains |
| Stratus detonations | `stratus-red-team detonate` (own account, lab) | detection coverage proof |
| Prowler rows | `prowler aws` (own account) | control failures |
| ScoutSuite | `scoutsuite` (own provider account) | posture summary |
| Pacu exec | `pacu --exec` with own confirmed creds (lab) | post-exploit surface |
| AzureHound | `azurehound` (own tenant) | attack path graph |

Walls: everything runs in the operator's own tenant/project. Nothing touches
third-party cloud estate (scope gate refuses). Detonations run in dedicated
lab subscriptions/projects and are cleaned up after proof.