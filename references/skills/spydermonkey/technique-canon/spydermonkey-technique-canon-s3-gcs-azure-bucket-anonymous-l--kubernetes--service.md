# S3/GCS/Azure bucket anonymous list — kubernetes / service

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-s3-gcs-azure-bucket-anonymous-l.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **kubernetes** · auth **service** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

Bucket LIST permission without auth is read-only inventory. Decisive test: anonymous LIST (s3 ls / public GET) — the listing = the finding; never write.

## Probe adjustment (kubernetes × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
