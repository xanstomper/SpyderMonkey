# Protocol-logic classes (read-only) — chain composition

- source canon: `spydermonkey/scada-canon.md`
- base technique: `spydermonkey-scada-canon-protocol-logic-classes-read-only.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
