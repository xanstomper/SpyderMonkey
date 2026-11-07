"""
ARSENAL_HW — the hardware / physical execution layer for SPYDERMONKEY v5.17.

The family's arsenal gains its REAL hardware domain: RF, BLE, RFID/NFC, SDR,
ESP32-class chips, smart-home (MQTT/Tuya), and audio/speaker research.

Design rules (identical to the rest of the arsenal):
- discovery-based: wrappers are defined-and-routable; they activate wherever
  the binary exists (fleet/engagement machines). No installs on the operator
  box, ever (operator-box rule).
- scope-gated: every execution passes the shared scope authority via
  arsenal.py's cmd_run — no authority → rc=1.
- lab wall: radio-frequency and physical-device probes are validation-only
  against OPERATOR-OWNED hardware in the operator's own lab; document
  frequency/power before any transmit. No third-party hardware. No DoS.
- NO-GAIN: nothing read is taken; proofs are decisive tests only.

Merged into the live registry by arsenal.py at import time via merge_hw().
"""
from __future__ import annotations

# ── hardware tool wrappers: name → (capability, classes, plan, builder) ──────
# builder(t, extra) returns argv AFTER the binary name; t is the target token
# (per-tool semantics documented in the plan line), extra is --wordlist etc.

ARSENAL_HW = {
    # ── wifi (OWN AP / lab only; radio tx documented first) ─────────────────
    "airmon-ng":  ("wifi monitor-mode mgmt", ("wifi", "hardware"),
                   "start monitor mode on own NIC (pass iface, e.g. wlan0)",
                   lambda t, extra=None: ["start", t]),
    "wash":       ("wps scan", ("wifi", "hardware"),
                   "WPS scan of OWN AP (pass monitor iface)",
                   lambda t, extra=None: ["-i", t]),
    "reaver":     ("wps pin trial", ("wifi", "hardware"),
                   "WPS pin trial against OWN AP (pass BSSID, lab only)",
                   lambda t, extra=None: ["-b", t, "-vv"]),
    "aircrack-ng": ("wpa handshake crack", ("wifi", "hardware"),
                    "crack own capture (pass BSSID; --wordlist for dict)",
                    lambda t, extra=None: ["-b", t, "-w",
                                           str(extra or "/usr/share/wordlists/rockyou.txt"),
                                           "capture.cap"]),
    "wifite":     ("wifi audit sweep", ("wifi", "hardware"),
                   "automated wifi audit of OWN network (pass iface)",
                   lambda t, extra=None: ["-i", t]),
    "kismet":     ("rf discovery", ("wifi", "hardware"),
                   "passive wifi/bt/sdr discovery server (pass log dir)",
                   lambda t, extra=None: ["-t", t]),
    "mdk4":       ("wifi flood verify", ("wifi", "hardware"),
                   "flood own lab AP only — documented, reversible",
                   lambda t, extra=None: ["wifi", "d", "-b", t]),
    "bettercap":  ("multi-mode mitm/rf", ("wifi", "hardware", "network"),
                   "caplets, ble + wifi sniffer on OWN devices (pass iface)",
                   lambda t, extra=None: ["-iface", t, "--no-colors"]),
    # ── BLE (own peripheral / own dongle only) ──────────────────────────────
    "hcitool":    ("ble device mgmt", ("ble", "hardware"),
                   "lescan on own adapter (pass hciN)",
                   lambda t, extra=None: ["-i", t, "lescan", "--discovery"]),
    "bluetoothctl": ("ble controller", ("ble", "hardware"),
                     "scan/connect on own adapter (pass hciN)",
                     lambda t, extra=None: ["--adapter", t, "scan", "on"]),
    "gatttool":   ("ble gatt read/write", ("ble", "hardware"),
                   "GATT read/write against OWN peripheral (pass MAC)",
                   lambda t, extra=None: ["-b", t, "--interactive"]),
    "ubertooth-btle": ("ble broad sniff", ("ble", "hardware"),
                       "broadcast sniff on own ubertooth dongle",
                       lambda t, extra=None: ["-f", "-t", "10"]),
    "btlejack":   ("ble link jack", ("ble", "hardware"),
                   "sniff/crack OWN ble links (pass device, lab)",
                   lambda t, extra=None: ["-d", t, "-f"]),
    "btscanner":  ("classic bt scan", ("ble", "hardware"),
                   "inquiry scan on own adapter (pass iface)",
                   lambda t, extra=None: ["-i", t]),
    # ── RFID/NFC (OWN badge / OWN tag only) ─────────────────────────────────
    "nfc-list":   ("nfc reader check", ("rfid", "hardware"),
                   "list attached nfc readers",
                   lambda t, extra=None: []),
    "nfc-poll":   ("nfc tag poll", ("rfid", "hardware"),
                   "poll for tags on own reader",
                   lambda t, extra=None: []),
    "nfc-mfclassic": ("mfclassic read", ("rfid", "hardware"),
                      "read OWN classic tag with known keys (pass dump)",
                      lambda t, extra=None: ["r", "a", t]),
    "mfoc":       ("mfclassic crack", ("rfid", "hardware"),
                   "hardnested read of OWN tag (pass output dump)",
                   lambda t, extra=None: ["-O", t]),
    "proxmark3":  ("rfid swiss army", ("rfid", "hardware"),
                   "proxmark ops against OWN tags (pass cmd string)",
                   lambda t, extra=None: ["-c", t]),
    "mfterm":     ("mf offline attack", ("rfid", "hardware"),
                   "offline mfclassic key attack (pass dump file)",
                   lambda t, extra=None: ["-f", t]),
    # ── SDR (own dongle; tx only after documenting freq/power) ──────────────
    "hackrf_info": ("sdr device check", ("sdr", "hardware"),
                    "identify own hackrf dongle",
                    lambda t, extra=None: []),
    "hackrf_transfer": ("sdr rx/tx", ("sdr", "hardware"),
                        "capture 433MHz band (pass output file)",
                        lambda t, extra=None: ["-r", t, "-f", "433920000",
                                               "-s", "2000000"]),
    "hackrf_sweep": ("sdr spectrum", ("sdr", "hardware"),
                     "spectrum sweep 430–870MHz (pass log file)",
                     lambda t, extra=None: ["-r", t, "-f", "430000000",
                                            "-l", "870000000"]),
    "rtl_sdr":    ("sdr capture", ("sdr", "hardware"),
                   "capture own dongle (pass freq; out=rtl.iq)",
                   lambda t, extra=None: ["-f", t, "-g", "40", "-s", "2000000",
                                          "capture.iq"]),
    "rtl_fm":     ("fm demod", ("sdr", "hardware"),
                   "demod FM at given freq",
                   lambda t, extra=None: ["-f", t, "-M", "fm", "-s", "22050", "-"]),
    "rtl_433":    ("433/868 decode", ("sdr", "iot", "hardware"),
                   "decode OWN sensors (pass freq; also 868MHz)",
                   lambda t, extra=None: ["-f", t, "-f", "868000000", "-A"]),
    "multimon-ng": ("digital mode decode", ("sdr", "audio", "hardware"),
                    "decode DTMF/FSK/pocsag from capture files",
                    lambda t, extra=None: ["-t", "dtmf,pocsag,fsk", t]),
    # ── ESP32-class chips + smart-home (OWN controller/OWN broker only) ─────
    "esptool":    ("esp flash mgmt", ("esp", "iot", "hardware"),
                   "identify/read OWN esp chip (pass port; dumps flash.bin)",
                   lambda t, extra=None: ["--port", t, "read_flash", "0x0",
                                          "0x400000", "flash.bin"]),
    "mosquitto_sub": ("mqtt subscribe", ("iot", "hardware"),
                      "subscribe OWN broker (pass host; topic #, -v)",
                      lambda t, extra=None: ["-h", t, "-t", "#", "-v"]),
    "mosquitto_pub": ("mqtt publish", ("iot", "hardware"),
                      "publish to OWN broker lab topic",
                      lambda t, extra=None: ["-h", t, "-t", "lab/test", "-m", "ping"]),
    "tuya-cli":   ("tuya local api", ("iot", "hardware"),
                   "tuya local control of OWN devices (pass device id)",
                   lambda t, extra=None: ["get", t]),
    "zigbee2mqtt": ("zigbee bridge", ("iot", "hardware"),
                    "zigbee coordinator ops on own network (pass host)",
                    lambda t, extra=None: ["info", t]),
    # ── audio / speaker research (OWN files, OWN devices, lab only) ─────────
    "sox":        ("audio toolkit", ("audio", "hardware"),
                   "encode/transform research audio (pass input)",
                   lambda t, extra=None: [t, "out.wav", "rate", "8000"]),
    "ffmpeg":     ("media convert", ("audio", "hardware"),
                   "audio encode/concat for data-over-audio labs (pass input)",
                   lambda t, extra=None: ["-i", t, "-ar", "8000", "out.wav"]),
    "minimodem":  ("audio modem", ("audio", "hardware"),
                   "data-over-audio modem rx/tx on OWN setups (pass capture)",
                   lambda t, extra=None: ["--rx", "1200", "-f", t]),
}

# ── hardware feeding chains (stages feed each other, scope-gated) ───────────

HW_CHAINS = {
    "hw-wifi":  ["airmon-ng", "wash", "reaver", "kismet", "bettercap", "wifite",
                 "aircrack-ng"],
    "hw-ble":   ["hcitool", "bluetoothctl", "gatttool", "ubertooth-btle",
                 "btlejack", "btscanner"],
    "hw-rfid":  ["nfc-list", "nfc-poll", "nfc-mfclassic", "mfoc", "mfterm",
                 "proxmark3"],
    "hw-sdr":   ["hackrf_info", "hackrf_transfer", "hackrf_sweep", "rtl_sdr",
                 "rtl_fm", "rtl_433", "multimon-ng"],
    "hw-esp":   ["esptool", "mosquitto_sub", "mosquitto_pub"],
    "hw-iot":   ["bettercap", "hcitool", "mosquitto_sub", "mosquitto_pub",
                 "tuya-cli", "esptool", "rtl_433"],
    "hw-audio": ["sox", "ffmpeg", "minimodem", "multimon-ng"],
}

HW_CHAIN_NAMES = set(HW_CHAINS)

# ── hardware technique classes (consume the ledgers' CANON_KW vocabulary) ───
HW_CLASSES = ("wifi", "ble", "rfid", "sdr", "esp", "iot", "audio", "hardware")


def merge_hw(arsenal: dict, chains: dict, chain_names: set) -> None:
    """Fold the hardware domain into the live arsenal registries (import-time)."""
    arsenal.update(ARSENAL_HW)
    chains.update(HW_CHAINS)
    chain_names.update(HW_CHAIN_NAMES)