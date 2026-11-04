# Cloud GCP Service Account Keys in Code (CLOUD-GCP-01) — azure / unauth

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-gcp-service-account-keys-in-c.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **azure** · auth **unauth** · chain role **pivot**

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: downloadable SA keys committed
- probe: harvest scan of declared repos/buckets for key material
- wall: redact on capture

## Probe adjustment (azure × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
