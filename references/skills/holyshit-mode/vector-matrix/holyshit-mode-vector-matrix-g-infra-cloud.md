# G. INFRA / CLOUD

- source canon: `holyshit-mode/vector-matrix.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- Public buckets: S3/GCS/Azure listing+read+write, backup dirs, credential files
- Metadata endpoints via SSRF: 169.254.169.254 (AWS/GCP/Azure IMDS, IMDSv1 vs v2)
- K8s: API server anonymous, kubelet 10250 auth, etcd 2379 exposure, dashboard public
- Container registries: anonymous pull, :latest overwrite
- CI/CD: public workflow logs with secrets, self-hosted runner exposure, artifact signing gaps
- Mail: SPF/DKIM/DMARC gaps → spoofing; subdomain takeover via orphaned MX/CNAME
- Cloudflare/CDN: Workers KV/D1 exposure via misrouted routes, origin-shield bypass

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
