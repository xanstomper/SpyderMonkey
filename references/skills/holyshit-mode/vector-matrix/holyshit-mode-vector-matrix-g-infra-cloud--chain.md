# G. INFRA / CLOUD — chain composition

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-g-infra-cloud.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Public buckets: S3/GCS/Azure listing+read+write, backup dirs, credential files
- Metadata endpoints via SSRF: 169.254.169.254 (AWS/GCP/Azure IMDS, IMDSv1 vs v2)
- K8s: API server anonymous, kubelet 10250 auth, etcd 2379 exposure, dashboard public
- Container registries: anonymous pull, :latest overwrite
- CI/CD: public workflow logs with secrets, self-hosted runner exposure, artifact signing gaps
- Mail: SPF/DKIM/DMARC gaps → spoofing; subdomain takeover via orphaned MX/CNAME
- Cloudflare/CDN: Workers KV/D1 exposure via misrouted routes, origin-shield bypass

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
