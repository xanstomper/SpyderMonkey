# T5 — Container/cluster takeover — edge-node / unauth

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-t5-container-cluster-takeov.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **edge-node** · auth **unauth** · chain role **final**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- kubelet unauth → pod list → pod token → kube-apiserver (one read-only call with the
  token); Docker socket → exec (one `id`); etcd keys → service-account secrets; registry
  pull → image secrets; CI runner token → pipelines.
- **DECISIVE PROOF:** API server accepts the harvested token read-only, `docker exec id`,
  or etcd key read. Then STOP.

## Probe adjustment (edge-node × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
