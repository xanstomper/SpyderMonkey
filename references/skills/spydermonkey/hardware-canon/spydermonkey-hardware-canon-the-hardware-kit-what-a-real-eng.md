# The hardware kit (what a real engagement node carries)

- source canon: `spydermonkey/hardware-canon.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

USB-UART (CP2102/CH340-class), logic analyzer (OpenBench/Saleae-class), SOIC-8
flash clip, Bus Pirate/FT2232H, HackRF/RTL-SDR dongles, ubertooth One,
Proxmark3 Easy, NFC reader, ESP32 dev boards + the operator's own devices
(strips, plugs, badge). RF enclosure for tx work. All of it lab inventory;
nothing ships to a third-party engagement target without scope authority
explicitly naming the device/network.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
