# Control proof & crown jewels

- source canon: `kairo/offensive-hardware-batteries.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- generated: 2026-11-04

## The technique

Confirmed plane finding → one read-only proof (shell `id`, bus byte read, key
extraction hash) → STOP. Then chain: what does the device reach? (cloud API, adjacent
network, OTA server, other devices). Record the chain per 3AM/T1–T7 style:
`uart-shell→firmware-keys→cloud-api:TAKEOVER` where the final hop is proven read-only.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
