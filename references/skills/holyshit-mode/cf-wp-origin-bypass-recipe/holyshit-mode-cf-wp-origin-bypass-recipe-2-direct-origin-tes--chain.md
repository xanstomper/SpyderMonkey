# 2. Direct-origin testing = WAF fully bypassed — chain composition

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-2-direct-origin-tes.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
