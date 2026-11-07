# Plane 1 — Firmware & storage — gateway / expired

- source canon: `kairo/offensive-hardware-batteries.md`
- base technique: `kairo-offensive-hardware-batteries-plane-1-firmware-storage.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **gateway** · auth **expired** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

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

## Probe adjustment (gateway × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
