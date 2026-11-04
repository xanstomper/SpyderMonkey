# Plane 1 — Firmware & storage — chain composition

- source canon: `kairo/offensive-hardware-batteries.md`
- base technique: `kairo-offensive-hardware-batteries-plane-1-firmware-storage.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Probe | Test | Confirmed-when |
|---|---|---|
| Extraction (SPI) | `flashrom -p ch341a_spi -r fw.bin` on pinned flash (owned board) | full image read |
| Extraction (eMMC/NAND) | footprint/`nanddump` on owned inline-eMMC dev boards | userspace files visible |
| Filesystem carve | `binwalk -Me fw.bin` → squashfs/cpio/ubifs | filesystem mounts |
| String sweep | `strings -n 6 fw.bin` + targeted grep (`passwd`, `key`, `token`, `192.168`, `/dev/tty`) | credentials/keys/hosts in image |
| Update package | capture OTA (`mitmproxy` on own update endpoint) → sign/format inspect | unencrypted or unsigned payload |
| Signature check | extract pubkey (`openssl x509`/`uefi-firmware-parser`), test rollback of OLD signed version (owned device) | old image accepted = rollback open |
| Secure boot chain | `cbmem`/UEFI vars/`sbctl status`-class read on owned device | chain config identifies trust root |

Typical yields: plaintext credentials, hardcoded API/cloud keys, hidden debug UART
configs, unsigned OTA → arbitrary firmware (confirmation via one shell command on the
owned device, then STOP).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
