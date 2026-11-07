# 1. Find the origin IP (bypass the CF WAF entirely) — wasm / root

- source canon: `holyshit-mode/wordpress-cloudflare-origin-bypass.md`
- base technique: `holyshit-mode-wordpress-cloudflare-origin-bypass-1-find-the-.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **wasm** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

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

## Probe adjustment (wasm × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
