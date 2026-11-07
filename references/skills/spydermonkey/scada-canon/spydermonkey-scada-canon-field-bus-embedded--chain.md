# Field-bus & embedded — chain composition

- source canon: `spydermonkey/scada-canon.md`
- base technique: `spydermonkey-scada-canon-field-bus-embedded.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Probe | Test | Confirmed-when |
|---|---|---|
| CAN bus listen | `candump -L` on OWN lab bus | frames visible (own rig) |
| CAN id inventory | `cansniffer` (own bus) | id map built (own bus) |
| Replay feasibility | `canplayer` from own log (own bus) | exact replay decodes (lab) |
| UART console | `minicom` on own controller debug header | root shell banner (own board) |
| Flash read | `flashrom` on own board's SPI | image dumped (own board) |
| J1939 | `can-utils` j1939 tools on own bus | PGN stream decoded |

Walls: nowhere in this canon is a write to a live industrial process
permitted. Anything that could actuate (register writes, S7 commands, CAN
frame injection, OPC method calls) happens only in the operator's OWN lab rig
built for the purpose, documented before the test. Third-party ICS = absolute
no-go; findings there are out-of-scope refusals (rc=1).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
