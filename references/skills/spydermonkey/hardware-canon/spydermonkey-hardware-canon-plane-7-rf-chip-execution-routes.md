# Plane 7 — RF & chip execution routes (which chain fires which probe)

- source canon: `spydermonkey/hardware-canon.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-07

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
