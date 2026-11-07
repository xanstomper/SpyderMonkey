# GCP identity surface — worker / machine

- source canon: `spydermonkey/cloud-azure-gcp-canon.md`
- base technique: `spydermonkey-cloud-azure-gcp-canon-gcp-identity-surface.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **worker** · auth **machine** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

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

## Probe adjustment (worker × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
