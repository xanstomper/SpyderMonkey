# Channel classes — graphql / service

- source canon: `spydermonkey/c2-canon.md`
- base technique: `spydermonkey-c2-canon-channel-classes.md`
- bindings: **WSTG-CLNT-05** · **CWE-345** · **ATT&CK T1557**
- context: **graphql** · auth **service** · chain role **pivot**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

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

## Probe adjustment (graphql × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
