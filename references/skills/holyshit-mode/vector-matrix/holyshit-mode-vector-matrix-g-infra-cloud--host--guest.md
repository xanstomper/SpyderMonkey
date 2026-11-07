# G. INFRA / CLOUD — host / guest

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-g-infra-cloud.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **host** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- Public buckets: S3/GCS/Azure listing+read+write, backup dirs, credential files
- Metadata endpoints via SSRF: 169.254.169.254 (AWS/GCP/Azure IMDS, IMDSv1 vs v2)
- K8s: API server anonymous, kubelet 10250 auth, etcd 2379 exposure, dashboard public
- Container registries: anonymous pull, :latest overwrite
- CI/CD: public workflow logs with secrets, self-hosted runner exposure, artifact signing gaps
- Mail: SPF/DKIM/DMARC gaps → spoofing; subdomain takeover via orphaned MX/CNAME
- Cloudflare/CDN: Workers KV/D1 exposure via misrouted routes, origin-shield bypass

## Probe adjustment (host × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
