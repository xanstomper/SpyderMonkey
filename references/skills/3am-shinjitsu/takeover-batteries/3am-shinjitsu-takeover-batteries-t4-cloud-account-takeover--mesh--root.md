# T4 — Cloud account takeover — mesh / root

- source canon: `3am-shinjitsu/takeover-batteries.md`
- base technique: `3am-shinjitsu-takeover-batteries-t4-cloud-account-takeover.md`
- bindings: **WSTG-INPV-10** · **CWE-918** · **ATT&CK T1190**
- context: **mesh** · auth **root** · chain role **final**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

- Secret leak → `sts get-caller-identity` success in the target account; bucket/object
  keys → deeper IAM; metadata/SSRF → instance role credential (one `get-caller-identity`,
  owned infra only for the decisive call); exposed snapshot/AMI → root volume → secrets;
  OIDC federation misconfig (documented-PoC); over-scoped service principals.
- **DECISIVE PROOF:** the harvested identity resolves to the target account and lists
  one resource. Then STOP.

## Probe adjustment (mesh × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
