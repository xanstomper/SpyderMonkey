# Takeover classes

- source canon: `spydermonkey/domtake-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| AWS S3 bucket | `s3scanner` check bucket name == cname (own) | bucket missing/claimable |
| Azure blob | `az storage container` existence probe (own) | container absent |
| GitHub pages | `curl` expected 404 signature (own) | pages site dormant |
| Heroku/Glitch | status code + body fingerprint (own) | app name free |
| Elastic IP | `whois`/`ipinfo` on cname (own) | eip released |
| Shopify/Wordpress | fingerprint strings (own) | storename claimable |
| Zendesk/Cargo | body markers (own) | subdomain free |
| Dead CDN | edge cert + 526/530 codes (own) | origin missing |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
