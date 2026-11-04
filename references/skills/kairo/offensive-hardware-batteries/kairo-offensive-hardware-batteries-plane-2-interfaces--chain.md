# Plane 2 — Interfaces — chain composition

- source canon: `kairo/offensive-hardware-batteries.md`
- base technique: `kairo-offensive-hardware-batteries-plane-2-interfaces.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Probe | Test | Confirmed-when |
|---|---|---|
| UART discovery | 4-pin header detection (GND sweep) → `minicom` @ 115200/57600 | bootloader/root shell banner |
| UART login | `root`/empty/`admin`/vendor defaults at the serial prompt | shell or `$` prompt |
| JTAG/SWD | `openocd -f interface/ftdi.cfg` on owned board; `jtagscan`-class pin find | debug access or IDCODE read |
| Bus sniffing | logic analyzer on SPI/I²C to crypto IC / flash on owned board | key material or plaintext on the bus |
| USB | `lsusb` descriptors, `usbhid-dump` on owned device, DFU mode check | hidden DFU/update mode exposed |
| Crypto/Secure element | MITM the element's bus (owned board); read-back attempt | key read or bus-level bypass |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
