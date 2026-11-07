# Plane 6 — Smart-home & LED strips (OWN controller, OWN broker, OWN network) — mesh / expired

- source canon: `spydermonkey/hardware-canon.md`
- base technique: `spydermonkey-hardware-canon-plane-6-smart-home-led-strips-ow.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **mesh** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| ESP chip identity | `esptool --port /dev/ttyUSB0 chip_id` on OWN strip controller / smart plug | chip + flash size identified |
| Flash dump (own device) | `esptool read_flash 0x0 0x400000 flash.bin` → `strings` sweep (keys, ssid, tokens) | credentials/config in own device image |
| Firmware compare | dump twice (fresh vs after OTA) → `binwalk`/`diffoscope` | OTA delta readable (own device) |
| MQTT topic audit (own broker) | `mosquitto_sub -h <own> -t '#' -v` on own broker/net | device topics flood on own network |
| MQTT auth check | `mosquitto_pub` to own broker lab topic without creds | anonymous publish accepted (own broker) |
| Tuya local API | `tuya-cli get <device-id>` on OWN tuya device (local key from own app config) | state read without cloud (own device) |
| Zigbee key exchange | `zigbee2mqtt`/Conbee on own coordinator — observe own network join | own network key observed on own coordinator |
| Update channel | capture own device OTA (mitmproxy on own update endpoint) → inspect | unsigned/plaintext update (own device, then STOP) |

Yields: hardcoded Wi-Fi creds in own strips, local API keys, broker topic
inventory — the operator's own estate only. Confirmed → ledger → STOP.

## Probe adjustment (mesh × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
