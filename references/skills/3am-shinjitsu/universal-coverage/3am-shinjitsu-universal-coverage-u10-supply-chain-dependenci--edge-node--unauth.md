# U10 Supply chain & dependencies — edge-node / unauth

- source canon: `3am-shinjitsu/universal-coverage.md`
- base technique: `3am-shinjitsu-universal-coverage-u10-supply-chain-dependenci.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- context: **edge-node** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- [ ] SBOM generated for every deployed artifact
- [ ] Direct/transitive dependencies matched to current advisories
- [ ] CI/CD permissions, runners, caches, artifacts, and deployment approvals reviewed
- [ ] Source repo protections, signing, provenance, and secret scanning verified
- [ ] Third-party packages/build actions pinned and reviewed

## Probe adjustment (edge-node × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
