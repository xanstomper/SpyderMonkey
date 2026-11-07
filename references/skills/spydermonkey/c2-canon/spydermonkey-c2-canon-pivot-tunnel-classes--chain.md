# Pivot & tunnel classes — chain composition

- source canon: `spydermonkey/c2-canon.md`
- base technique: `spydermonkey-c2-canon-pivot-tunnel-classes.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Probe | Test | Confirmed-when |
|---|---|---|
| Socks reverse | `chisel`/`ligolo-ng` lab pair | local socks reaches remote lan |
| SSH dynamic | `ssh -D` (own hosts) | socks proxy up |
| Frp/nps | `frp` lab pair | nat traversal works |
| RDP pivot | `rpivot` lab pair (own rdp) | socks over rdp |
| HTTP CONNECT | `proxytunnel` lab pair | meet-in-middle tunnel |
| Malleable profile | c2 profile test (own listener) | jitter/URI pattern applied |
| OPSEC hygiene | `macchanger` + fresh identity before lab c2 | listener not tied to op identity |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
