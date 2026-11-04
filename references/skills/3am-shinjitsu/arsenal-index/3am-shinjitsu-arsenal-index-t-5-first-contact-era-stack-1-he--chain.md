# T+5 — first-contact era-stack (1 HEAD request) — chain composition

- source canon: `3am-shinjitsu/arsenal-index.md`
- base technique: `3am-shinjitsu-arsenal-index-t-5-first-contact-era-stack-1-he.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| # | Probe | Test | Confirmed-when |
|---|---|---|---|
| 7 | Header stack | `curl -sI https://<domain>` | Server/X-Powered-By/via/x-kong-*/x-served-by fingerprints → EOL table (`arsenal-01` §1.12) |
| 8 | Kong-fronted Supabase | `www-authenticate: Basic realm="service"` + `x-kong-response-latency` + ACAH contains `apikey` | GoTrue chain unlocks (`arsenal-04` §3.1) |
| 9 | Origin-verify | `python3 http.client` → origin IP, `Host:`/SNI=<domain>, unverified TLS, expect real app HTML vs CF interstitial | full WAF bypass (`arsenal-01` §1.2) |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
