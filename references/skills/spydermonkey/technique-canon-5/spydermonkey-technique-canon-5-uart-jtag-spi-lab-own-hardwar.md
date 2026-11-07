# UART/JTAG/SPI (lab, own hardware)

- source canon: `spydermonkey/technique-canon-5.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- generated: 2026-11-06

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Console discovery (baud-rate sweep on your own board), JTAG chain enumeration, SPI flash dump — firmware-extraction classes with the no-gain read-only framing (MASTG-RES canon). Decisive test: the extracted image hash + strings inventory of YOUR device.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
