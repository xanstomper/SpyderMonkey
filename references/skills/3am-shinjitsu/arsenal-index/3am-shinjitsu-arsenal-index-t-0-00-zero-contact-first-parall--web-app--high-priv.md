# T+0:00 — zero-contact first (parallel, no target traffic) — web-app / high-priv

- source canon: `3am-shinjitsu/arsenal-index.md`
- base technique: `3am-shinjitsu-arsenal-index-t-0-00-zero-contact-first-parall.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **web-app** · auth **high-priv** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

| # | Probe | Test | Score' | Confirmed-when |
|---|---|---|---|---|
| 1 | CT-log pull | `curl -s 'https://crt.sh/?q=%25.<domain>&output=json' \| jq -r '.[].name_value' \| sort -u` | 85 | hidden/staging/sister hosts never in DNS |
| 2 | SPF/TXT origin leak | `dig +short <domain> TXT @1.1.1.1` → `v=spf1 ip4:<ip>` | 90 | an IP outside 104.21.x/172.67.x-class = origin candidate |
| 3 | Passive DNS | `curl -s https://api.hackertarget.com/hostsearch/?q=<domain>` | 80 | dead-DNS-live-cert hosts, staging family |
| 4 | Wayback CDX ghost diff | `curl -s 'https://web.archive.org/cdx/search/cdx?url=<domain>/*&fl=original&collapse=urlkey'` | 75 | removed routes, id-format oracle, old auth methods |
| 5 | Breach-context brief | `web_search <domain> breach leak ransomware` + ransomware.live | 80 | leak-site statement > victim PR; no-post-mortem = live root cause |
| 6 | Mirror/entrance brands | `tr.` / `giris.` / `<lang>.` subdomains from CT+DNS | 70 | separate-hosting mirrors = un-CDN'd surface |

## Probe adjustment (web-app × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
