# Plane 7 — RF & chip execution routes (which chain fires which probe) — wireless / federated

- source canon: `spydermonkey/hardware-canon.md`
- base technique: `spydermonkey-hardware-canon-plane-7-rf-chip-execution-routes.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **wireless** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: LAB-ONLY — your own radios and stations; third-party airwaves are the absolute wall
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

| Chain | Fires | Confirmed-when (per stage) |
|---|---|---|
| hw-wifi | airmon-ng → wash → reaver → kismet → bettercap → wifite → aircrack-ng | mon mode up; WPS open; handshake captured; crack (own AP) |
| hw-ble | hcitool → bluetoothctl → gatttool → ubertooth-btle → btlejack → btscanner | adapter up; device seen; GATT list; sniff (own dongle) |
| hw-rfid | nfc-list → nfc-poll → nfc-mfclassic → mfoc → mfterm → proxmark3 | reader up; tag seen; keys read (own tag) |
| hw-sdr | hackrf_info → hackrf_transfer → hackrf_sweep → rtl_sdr → rtl_fm → rtl_433 → multimon-ng | dongle up; 433 capture; sensor decode (own gear) |
| hw-esp | esptool → mosquitto_sub → mosquitto_pub | chip id; topic flood (own broker); flash dump |
| hw-iot | bettercap → hcitool → mosquitto_sub → mosquitto_pub → tuya-cli → esptool → rtl_433 | full smart-home estate sweep (own network) |
| hw-audio | sox → ffmpeg → minimodem → multimon-ng | round-trip decode; DTMF on own capture (own files) |

Every chain ends in the ledger with its decisive test or a hypothesis — no
speculation. Family walls apply at every stage.

## Probe adjustment (wireless × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
