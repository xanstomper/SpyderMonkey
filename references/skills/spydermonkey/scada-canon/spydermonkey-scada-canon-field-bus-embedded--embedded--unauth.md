# Field-bus & embedded — embedded / unauth

- source canon: `spydermonkey/scada-canon.md`
- base technique: `spydermonkey-scada-canon-field-bus-embedded.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **embedded** · auth **unauth** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: banner/identity reads only on in-scope industrial tiers — control writes are the absolute wall
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

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

## Probe adjustment (embedded × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
