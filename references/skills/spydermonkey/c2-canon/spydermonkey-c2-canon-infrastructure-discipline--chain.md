# Infrastructure discipline — chain composition

- source canon: `spydermonkey/c2-canon.md`
- base technique: `spydermonkey-c2-canon-infrastructure-discipline.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
