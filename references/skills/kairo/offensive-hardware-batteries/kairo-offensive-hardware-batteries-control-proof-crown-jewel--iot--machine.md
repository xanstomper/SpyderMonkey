# Control proof & crown jewels — iot / machine

- source canon: `kairo/offensive-hardware-batteries.md`
- base technique: `kairo-offensive-hardware-batteries-control-proof-crown-jewel.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **iot** · auth **machine** · chain role **final**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Confirmed plane finding → one read-only proof (shell `id`, bus byte read, key
extraction hash) → STOP. Then chain: what does the device reach? (cloud API, adjacent
network, OTA server, other devices). Record the chain per 3AM/T1–T7 style:
`uart-shell→firmware-keys→cloud-api:TAKEOVER` where the final hop is proven read-only.

## Probe adjustment (iot × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
