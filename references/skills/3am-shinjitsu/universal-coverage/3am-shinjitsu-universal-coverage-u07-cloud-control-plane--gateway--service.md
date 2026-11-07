# U07 Cloud control plane — gateway / service

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u07-cloud-control-plane.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **gateway** · auth **service** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- [ ] Organization/account structure, IAM roles, policies, and trust relationships reviewed
- [ ] Public buckets/queues/functions/snapshots/endpoints inventoried
- [ ] Network security groups, peering, flow logs, and egress controls reviewed
- [ ] KMS/keys, secrets managers, certificates, and rotation audited
- [ ] Admin/break-glass access and audit trails verified

## Probe adjustment (gateway × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
