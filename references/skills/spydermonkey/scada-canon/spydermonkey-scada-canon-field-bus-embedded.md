# Field-bus & embedded

- source canon: `spydermonkey/scada-canon.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
