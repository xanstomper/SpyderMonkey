# GCP identity surface — chain composition

- source canon: `spydermonkey/cloud-azure-gcp-canon.md`
- base technique: `spydermonkey-cloud-azure-gcp-canon-gcp-identity-surface.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
