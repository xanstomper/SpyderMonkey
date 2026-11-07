# Plane 1 — Firmware & storage

- source canon: `kairo/offensive-hardware-batteries.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- generated: 2026-11-04

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
