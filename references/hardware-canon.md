# SPYDERMONKEY — Hardware Canon (v5.17: audio + smart-home planes)

The family's real-hardware execution canon: RF/BLE/RFID/SDR/ESP/smart-home
chains plus the AUDIO & SPEAKER research plane. Every probe is a decisive,
non-destructive test on OPERATOR-OWNED hardware in the operator's own lab.
Radio rule: document frequency/power before any transmit. NO third-party
hardware. NO-GAIN: proofs only, nothing taken.

Execution lives in `arsenal_hw.py` (merged into the arsenal at import time):
– chains: hw-wifi · hw-ble · hw-rfid · hw-sdr · hw-esp · hw-iot · hw-audio
– every chain is scope-gated; tools are discovery-based (activate where the
  binary exists — fleet/engagement machines, never installed on the operator
  box).

## Plane 5 — Audio & speaker research (OWN files, OWN devices, lab)

| Probe | Test | Confirmed-when |
|---|---|---|
| Covert data-over-audio | `minimodem --tx 1200 -f data.wav` (own payload) → `minimodem --rx 1200 -f data.wav` | round-trip bit-exact on own channel |
| Audio data channel audit | `sox in.wav -n stat`/spectral view (own capture) — find out-of-band carriers | unexpected carrier/energy off the voice band |
| Ultrasonic feasibility | `sox`/`ffmpeg` upshift own test tone to 18–22kHz; `arecord` on own device pair | inaudible carrier decodes on own receiver — feasibility ONLY |
| DTMF/telephony tones | `multimon-ng -t dtmf -a AUDIO` (own IVR capture) | digits decoded from own recording |
| Speaker/device fingerprint | `ffmpeg` chirp playback on own speaker → own mic capture — impulse response | stable per-device signature (fingerprint research) |
| Voice-assistant mic wake | own assistant device: play own trigger phrase from owned audio — note LED/mic state | wake triggers on owned device only |
| Audio exfil proof of concept | own lab: encode file → play out of own speaker → record on own mic → decode | bit-exact round trip (lab channel, own gear) |

Walls: everything above runs on the operator's own audio gear or own
recordings; ultrasonic transmission is feasibility on own devices only and
stopped at proof. No surveillance of third parties, no hidden audio capture
of anyone but the operator.

## Plane 6 — Smart-home & LED strips (OWN controller, OWN broker, OWN network)

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

## Plane 7 — RF & chip execution routes (which chain fires which probe)

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

## The hardware kit (what a real engagement node carries)

USB-UART (CP2102/CH340-class), logic analyzer (OpenBench/Saleae-class), SOIC-8
flash clip, Bus Pirate/FT2232H, HackRF/RTL-SDR dongles, ubertooth One,
Proxmark3 Easy, NFC reader, ESP32 dev boards + the operator's own devices
(strips, plugs, badge). RF enclosure for tx work. All of it lab inventory;
nothing ships to a third-party engagement target without scope authority
explicitly naming the device/network.