# Protocol-logic classes (read-only) — wireless / high-priv

- source canon: `spydermonkey/scada-canon.md`
- base technique: `spydermonkey-scada-canon-protocol-logic-classes-read-only.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **wireless** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: LAB-ONLY — your own radios and stations; third-party airwaves are the absolute wall
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (wireless × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
