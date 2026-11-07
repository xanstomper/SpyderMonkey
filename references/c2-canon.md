# SPYDERMONKEY — C2 & Tunnels Canon (v6.0)

C2/tunneling classes as lab-only decisive tests. Every command-channel test
runs between machines the operator owns (two lab VMs, a lab VPS and a lab
client). The operator-box rule: no C2 tooling is installed on the daily
driver. Bindings: ATT&CK T1071/T1090/T1572.

## Channel classes

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

## Pivot & tunnel classes

| Probe | Test | Confirmed-when |
|---|---|---|
| Socks reverse | `chisel`/`ligolo-ng` lab pair | local socks reaches remote lan |
| SSH dynamic | `ssh -D` (own hosts) | socks proxy up |
| Frp/nps | `frp` lab pair | nat traversal works |
| RDP pivot | `rpivot` lab pair (own rdp) | socks over rdp |
| HTTP CONNECT | `proxytunnel` lab pair | meet-in-middle tunnel |
| Malleable profile | c2 profile test (own listener) | jitter/URI pattern applied |
| OPSEC hygiene | `macchanger` + fresh identity before lab c2 | listener not tied to op identity |

## Infrastructure discipline

| Probe | Test | Confirmed-when |
|---|---|---|
| Listener red-flag scan | verify own listener banners match decoy (own) | banner/tls profile clean |
| Redirector | `socat`/`haproxy` stager in lab | redirector forwards |
| Log checks | `relay exec` ls on own node | no third-party touch |
| Takedown drill | stop + verify listener dead (own) | clean kill switch |
| Backup channel | second listener pair (own lab) | resilience confirmed |

Walls: C2/Tunnels run against operator-OWNED endpoints exclusively —
anything else is a network-level violation (scope gate refuses, rc=1). A
confirmed channel is proof in the ledger, never an operation: no data
exfiltration, no persistence on owned hosts.