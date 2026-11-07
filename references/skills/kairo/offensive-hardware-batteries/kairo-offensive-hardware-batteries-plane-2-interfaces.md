# Plane 2 — Interfaces

- source canon: `kairo/offensive-hardware-batteries.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- generated: 2026-11-04

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| UART discovery | 4-pin header detection (GND sweep) → `minicom` @ 115200/57600 | bootloader/root shell banner |
| UART login | `root`/empty/`admin`/vendor defaults at the serial prompt | shell or `$` prompt |
| JTAG/SWD | `openocd -f interface/ftdi.cfg` on owned board; `jtagscan`-class pin find | debug access or IDCODE read |
| Bus sniffing | logic analyzer on SPI/I²C to crypto IC / flash on owned board | key material or plaintext on the bus |
| USB | `lsusb` descriptors, `usbhid-dump` on owned device, DFU mode check | hidden DFU/update mode exposed |
| Crypto/Secure element | MITM the element's bus (owned board); read-back attempt | key read or bus-level bypass |

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
