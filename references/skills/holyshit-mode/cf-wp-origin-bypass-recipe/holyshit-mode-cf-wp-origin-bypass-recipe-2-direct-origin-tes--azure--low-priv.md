# 2. Direct-origin testing = WAF fully bypassed — azure / low-priv

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-2-direct-origin-tes.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **azure** · auth **low-priv** · chain role **pivot**

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

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

## Probe adjustment (azure × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
