# Discovery & identity

- source canon: `spydermonkey/scada-canon.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- generated: 2026-11-07

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
