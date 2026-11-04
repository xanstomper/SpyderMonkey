# 1. Find the origin IP (bypass the CF WAF entirely) — chain composition

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-1-find-the-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

The single highest-leverage move on any Cloudflare-fronted target. Once you have the true
origin IP, the entire WAF/challenge stack is moot — you talk straight to the backend.

**Origin-leak sources (key-free):**
- **SPF record first.** `dig +short <target> TXT @1.1.1.1`. A `v=spf1 ip4:<ip>` entry leaks the
  real sending/origin host. On .163.60 ~all` → origin at that IP,
  **not** behind CF (CF anycast IPs are 104.21.x / 172.67.x). This was the instant win.
- MX records can leak the mail host (which may share origin infra).
- crt.sh (`https://crt.sh/?q=%25.domain&output=json`) for subdomain discovery — flaky (502),
  retry with backoff.
- Memory/env intel (known hosting netblocks, e.g. `bacloud.info 88.119.163.0/24`).

**Verify the origin serves the target:** connect with SNI set to the Host AND send the
`Host:` header, using a TLS context that skips hostname verification (origin cert may not cover
every vhost):

```python
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
conn = http.client.HTTPSConnection("88.119.163.60", 443, context=ctx, timeout=15)
conn.request("GET", "/", headers={"Host":""Mozilla/5.0 Chrome/124.0"})
```

If this returns WP/app content while `curl https://domain` yields a CF "One moment, please…"
challenge, **the WAF is bypassed**.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
