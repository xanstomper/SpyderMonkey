# Protocol-logic classes (read-only)

- source canon: `spydermonkey/scada-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
