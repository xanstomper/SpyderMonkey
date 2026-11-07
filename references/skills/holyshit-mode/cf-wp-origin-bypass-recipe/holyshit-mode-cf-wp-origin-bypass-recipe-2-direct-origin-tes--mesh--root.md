# 2. Direct-origin testing = WAF fully bypassed — mesh / root

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-2-direct-origin-tes.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **mesh** · auth **root** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

Once you have the origin IP, you do NOT need to solve the CF JS challenge. Hit the IP
directly over raw TLS with the target's `Host:` header. `http.client.HTTPSConnection`
(paired with `_create_unverified_context`) handles TLS + chunked decoding for you:

```python
import ssl, http.client
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
c = http.client.HTTPSConnection("88.119.163.60", 443, context=ctx, timeout=12)
c.request("GET", "/", headers={"Host":""Mozilla/5.0 Chrome/124.0"})
r = c.getresponse(); body = r.read()
```

Every request then lands on the untouched origin with zero Cloudflare WAF/challenge in the
path — exploit payloads pass, admin/API fully reachable. This is the single highest-value
move on any CF-fronted WP target.

## Probe adjustment (mesh × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
