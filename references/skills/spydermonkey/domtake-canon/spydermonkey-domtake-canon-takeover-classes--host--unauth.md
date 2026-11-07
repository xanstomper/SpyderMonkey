# Takeover classes — host / unauth

- source canon: `spydermonkey/domtake-canon.md`
- base technique: `spydermonkey-domtake-canon-takeover-classes.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **host** · auth **unauth** · chain role **final**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

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

## Probe adjustment (host × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
