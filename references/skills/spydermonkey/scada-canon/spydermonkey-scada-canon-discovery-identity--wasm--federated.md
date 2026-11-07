# Discovery & identity — wasm / federated

- source canon: `spydermonkey/scada-canon.md`
- base technique: `spydermonkey-scada-canon-discovery-identity.md`
- bindings: **WSTG-INPV-05** · **CWE-89** · **ATT&CK T1190**
- context: **wasm** · auth **federated** · chain role **pivot**

## Route

- probes: `httpx`, `whatweb`, `webanalyze`, `nmap-waf-fingerprint`, `katana`, `gospider`, `hakrawler`
- chains: `recon`, `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

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

## Probe adjustment (wasm × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
