# T+0:00 — zero-contact first (parallel, no target traffic)

- source canon: `3am-shinjitsu/arsenal-index.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

| # | Probe | Test | Score' | Confirmed-when |
|---|---|---|---|---|
| 1 | CT-log pull | `curl -s 'https://crt.sh/?q=%25.<domain>&output=json' \| jq -r '.[].name_value' \| sort -u` | 85 | hidden/staging/sister hosts never in DNS |
| 2 | SPF/TXT origin leak | `dig +short <domain> TXT @1.1.1.1` → `v=spf1 ip4:<ip>` | 90 | an IP outside 104.21.x/172.67.x-class = origin candidate |
| 3 | Passive DNS | `curl -s https://api.hackertarget.com/hostsearch/?q=<domain>` | 80 | dead-DNS-live-cert hosts, staging family |
| 4 | Wayback CDX ghost diff | `curl -s 'https://web.archive.org/cdx/search/cdx?url=<domain>/*&fl=original&collapse=urlkey'` | 75 | removed routes, id-format oracle, old auth methods |
| 5 | Breach-context brief | `web_search <domain> breach leak ransomware` + ransomware.live | 80 | leak-site statement > victim PR; no-post-mortem = live root cause |
| 6 | Mirror/entrance brands | `tr.` / `giris.` / `<lang>.` subdomains from CT+DNS | 70 | separate-hosting mirrors = un-CDN'd surface |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
