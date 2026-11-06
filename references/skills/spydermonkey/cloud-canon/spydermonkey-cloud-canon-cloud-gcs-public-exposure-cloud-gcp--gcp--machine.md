# Cloud GCS Public Exposure (CLOUD-GCP-03) — gcp / machine

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-gcs-public-exposure-cloud-gcp.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **gcp** · auth **machine** · chain role **pivot**

## Context

- platform: IAM/service-account surface — read-only enumeration
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- class: listable/public GCS buckets
- probe: unauth listing probes
- wall: read-only, HARVEST rules

## Probe adjustment (gcp × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
