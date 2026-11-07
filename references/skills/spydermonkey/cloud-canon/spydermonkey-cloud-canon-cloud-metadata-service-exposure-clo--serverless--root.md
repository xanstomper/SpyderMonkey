# Cloud Metadata Service Exposure (CLOUD-SSRF-01) — serverless / root

- source canon: `spydermonkey/cloud-canon.md`
- base technique: `spydermonkey-cloud-canon-cloud-metadata-service-exposure-clo.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **serverless** · auth **root** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: function identity + env surface — read-only enumeration, crowns as the control-plane class
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- class: 169.254.169.254 reachable through an in-scope app — the SSRF crown
- probe: the SSRF battery's metadata targets — the differential proves the reach
- wall: proof-of-reach only; metadata contents beyond the marker are never dumped

## Probe adjustment (serverless × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
