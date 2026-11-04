# Cloud Azure Managed Identity Abuse Surface (CLOUD-AZ-01) — gcp / low-priv

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-azure-managed-identity-abuse-.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **gcp** · auth **low-priv** · chain role **pivot**

## Context

- platform: IAM/service-account surface — read-only enumeration
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- class: identity-bearing workloads whose endpoints are exposed
- probe: read-only endpoint + identity surface inventory
- wall: nothing tokened; the exposure is priced

## Probe adjustment (gcp × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
