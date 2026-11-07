# Cloud Cross-Account Resource Share (CLOUD-IAM-04) — kubernetes / service

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-cross-account-resource-share-.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **kubernetes** · auth **service** · chain role **final**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- class: shares/principal policies open to foreign accounts
- probe: read-only share inventory
- wall: read-only

## Probe adjustment (kubernetes × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
