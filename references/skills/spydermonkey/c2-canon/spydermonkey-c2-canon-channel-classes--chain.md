# Channel classes — chain composition

- source canon: `spydermonkey/c2-canon.md`
- base technique: `spydermonkey-c2-canon-channel-classes.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
