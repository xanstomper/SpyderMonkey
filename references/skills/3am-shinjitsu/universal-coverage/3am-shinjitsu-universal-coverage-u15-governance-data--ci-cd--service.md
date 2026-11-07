# U15 Governance & data — ci-cd / service

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u15-governance-data.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **ci-cd** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- [ ] Data map, classification, residency, retention, encryption, and deletion verified
- [ ] Vendor/third-party access reviewed against least privilege and expiry
- [ ] Backup/DR and incident communication paths tested or tabletop-reviewed
- [ ] Privacy controls for exports, support tooling, and analytics verified
- [ ] Exception register and risk acceptance have owners and expiry dates

## Probe adjustment (ci-cd × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
