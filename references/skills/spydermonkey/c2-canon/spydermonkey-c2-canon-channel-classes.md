# Channel classes

- source canon: `spydermonkey/c2-canon.md`
- bindings: **WSTG-CLNT-05** · **CWE-345** · **ATT&CK T1557**
- generated: 2026-11-07

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| HTTP/S beacon | `sliver`/`havoc` lab pair, own listener | callback registered |
| DNS tunnel | `dnscat2` lab pair, own domain | channel established |
| ICMP tunnel | `icmpsh`/`hans` lab pair | shell over ping |
| DoH | `iodine` over own DoH resolver | tunnel up |
| Websocket | `wstunnel` lab pair | ws channel carries tcp |
| HTTP/2 | `suo5` lab pair | full-duplex over h2 |
| CDN fronting | own domain + CDN config in lab | request routed to listener |
| Jitter/beaconing | `pspy` + packet capture (own lab) | periodic C2 pattern |
| Steganographic C2 | `stegoc2`-style (own lab pair) | covert channel works (own) |
| Dead-drop | pastebin-style drop (own account) | retrieval loop verified |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
