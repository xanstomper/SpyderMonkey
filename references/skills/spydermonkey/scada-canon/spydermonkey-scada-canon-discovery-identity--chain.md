# Discovery & identity — chain composition

- source canon: `spydermonkey/scada-canon.md`
- base technique: `spydermonkey-scada-canon-discovery-identity.md`
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
| Modbus banner | `modbus-cli` / `mbtget` read holding regs 0x0 (own PLC) | device answers / unit id |
| DNP3 discovery | `nmap -sU -p 20000` + `dnp3-version` NSE (own) | dnp3 stack banner |
| S7 identity | `s7brute` info mode / `s7-info` on own S7 plc | rack/slot + model string |
| BACnet discovery | `bacnet-version` NSE on own controller | BACnet stack present |
| EtherNet/IP | `enip-info` NSE on own scanner/PLC | vendor/device identity |
| IEC-104 | `iec-identify` NSE on own RTU/gateway | ASDU class response |
| HMI web | `httpx` on own HMI panel (in scope) | web UI + version banner |
| Historian | db service banner on own historian host | SQL/OPC endpoint |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
