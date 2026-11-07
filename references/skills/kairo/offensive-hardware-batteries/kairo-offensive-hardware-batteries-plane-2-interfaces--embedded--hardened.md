# Plane 2 — Interfaces — embedded / hardened

- source canon: `kairo/offensive-hardware-batteries.md`
- base technique: `kairo-offensive-hardware-batteries-plane-2-interfaces.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **embedded** · auth **hardened** · chain role **pivot**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: banner/identity reads only on in-scope industrial tiers — control writes are the absolute wall
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

| Probe | Test | Confirmed-when |
|---|---|---|
| UART discovery | 4-pin header detection (GND sweep) → `minicom` @ 115200/57600 | bootloader/root shell banner |
| UART login | `root`/empty/`admin`/vendor defaults at the serial prompt | shell or `$` prompt |
| JTAG/SWD | `openocd -f interface/ftdi.cfg` on owned board; `jtagscan`-class pin find | debug access or IDCODE read |
| Bus sniffing | logic analyzer on SPI/I²C to crypto IC / flash on owned board | key material or plaintext on the bus |
| USB | `lsusb` descriptors, `usbhid-dump` on owned device, DFU mode check | hidden DFU/update mode exposed |
| Crypto/Secure element | MITM the element's bus (owned board); read-back attempt | key read or bus-level bypass |

## Probe adjustment (embedded × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
