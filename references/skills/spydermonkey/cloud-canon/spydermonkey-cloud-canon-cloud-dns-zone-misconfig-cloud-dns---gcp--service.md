# Cloud DNS Zone Misconfig (CLOUD-DNS-01) — gcp / service

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-dns-zone-misconfig-cloud-dns-.md`
- bindings: **WSTG-CONF-09** · **CWE-350** · **ATT&CK T1584**
- context: **gcp** · auth **service** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: IAM/service-account surface — read-only enumeration
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- class: public zone records pointing to deprovisioned services
- probe: the takeover engine — dangling record inventory
- wall: NO-GAIN

## Probe adjustment (gcp × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
