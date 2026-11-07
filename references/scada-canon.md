# SPYDERMONKEY — SCADA/ICS Canon (v6.0)

Industrial-protocol classes as read-only decisive tests against the
OPERATOR'S OWN controllers/lab rigs (or in-scope ICS assets in scope.json).
The control-write wall is absolute: register READS and banner/identity probes
only. Bindings: ATT&CK T0853/T0869 · CWE-787 surface.

## Discovery & identity

| Probe | Test | Confirmed-when |
|---|---|---|
| Modbus banner | `modbus-cli` / `mbtget` read holding regs 0x0 (own PLC) | device answers / unit id |
| DNP3 discovery | `nmap -sU -p 20000` + `dnp3-version` NSE (own) | dnp3 stack banner |
| S7 identity | `s7brute` info mode / `s7-info` on own S7 plc | rack/slot + model string |
| BACnet discovery | `bacnet-version` NSE on own controller | BACnet stack present |
| EtherNet/IP | `enip-info` NSE on own scanner/PLC | vendor/device identity |
| IEC-104 | `iec-identify` NSE on own RTU/gateway | ASDU class response |
| HMI web | `httpx` on own HMI panel (in scope) | web UI + version banner |
| Historian | db service banner on own historian host | SQL/OPC endpoint |

## Protocol-logic classes (read-only)

| Probe | Test | Confirmed-when |
|---|---|---|
| Modbus function sweep | `modpoll` read coils 0x0-0x20 (own device) | unexpected read functions open |
| Unit-id enumeration | `mbtget -a 1..10` on own gateway (own) | multiple unit ids respond |
| DNP3 APDU class | capture own traffic (`tcpdump`), `tshark -d dnp` | classes/functions observed |
| S7 auth gap | `s7brute` with empty/blank (own plc) | blank auth accepted (lab) |
| BACnet object browse | `bacnet-version` + object poll (own controller) | object list exposed |
| OPC UA discovery | `ua-discovery`-class on own server (own) | endpoints without auth |
| ENIP list identity | `enip-info` + `enip-list-identity` NSE (own) | CIP identity broadcast |
| Historian SQL | `psql`/`mssql-cli` banner on own historian | default sa/blank (own db) |
| Firmware version | panel web/`snmp` on own device | outdated build (own device) |

## Field-bus & embedded

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