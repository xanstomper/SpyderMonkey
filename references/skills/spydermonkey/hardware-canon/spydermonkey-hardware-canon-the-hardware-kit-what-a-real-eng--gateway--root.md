# The hardware kit (what a real engagement node carries) — gateway / root

- source canon: `spydermonkey/hardware-canon.md`
- base technique: `spydermonkey-hardware-canon-the-hardware-kit-what-a-real-eng.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **gateway** · auth **root** · chain role **pivot**

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

USB-UART (CP2102/CH340-class), logic analyzer (OpenBench/Saleae-class), SOIC-8
flash clip, Bus Pirate/FT2232H, HackRF/RTL-SDR dongles, ubertooth One,
Proxmark3 Easy, NFC reader, ESP32 dev boards + the operator's own devices
(strips, plugs, badge). RF enclosure for tx work. All of it lab inventory;
nothing ships to a third-party engagement target without scope authority
explicitly naming the device/network.

## Probe adjustment (gateway × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
