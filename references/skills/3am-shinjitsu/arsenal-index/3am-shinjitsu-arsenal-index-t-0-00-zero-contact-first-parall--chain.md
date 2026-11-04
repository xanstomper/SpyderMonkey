# T+0:00 — zero-contact first (parallel, no target traffic) — chain composition

- source canon: `3am-shinjitsu/arsenal-index.md`
- base technique: `3am-shinjitsu-arsenal-index-t-0-00-zero-contact-first-parall.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| # | Probe | Test | Score' | Confirmed-when |
|---|---|---|---|---|
| 1 | CT-log pull | `curl -s 'https://crt.sh/?q=%25.<domain>&output=json' \| jq -r '.[].name_value' \| sort -u` | 85 | hidden/staging/sister hosts never in DNS |
| 2 | SPF/TXT origin leak | `dig +short <domain> TXT @1.1.1.1` → `v=spf1 ip4:<ip>` | 90 | an IP outside 104.21.x/172.67.x-class = origin candidate |
| 3 | Passive DNS | `curl -s https://api.hackertarget.com/hostsearch/?q=<domain>` | 80 | dead-DNS-live-cert hosts, staging family |
| 4 | Wayback CDX ghost diff | `curl -s 'https://web.archive.org/cdx/search/cdx?url=<domain>/*&fl=original&collapse=urlkey'` | 75 | removed routes, id-format oracle, old auth methods |
| 5 | Breach-context brief | `web_search <domain> breach leak ransomware` + ransomware.live | 80 | leak-site statement > victim PR; no-post-mortem = live root cause |
| 6 | Mirror/entrance brands | `tr.` / `giris.` / `<lang>.` subdomains from CT+DNS | 70 | separate-hosting mirrors = un-CDN'd surface |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
