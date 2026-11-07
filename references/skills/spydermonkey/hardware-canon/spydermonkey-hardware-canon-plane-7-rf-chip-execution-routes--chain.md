# Plane 7 — RF & chip execution routes (which chain fires which probe) — chain composition

- source canon: `spydermonkey/hardware-canon.md`
- base technique: `spydermonkey-hardware-canon-plane-7-rf-chip-execution-routes.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
