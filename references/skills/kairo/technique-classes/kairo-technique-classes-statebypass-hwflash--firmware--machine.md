# STATEBYPASS — HWFLASH — firmware / machine

- source canon: `kairo/technique-classes.md`
- base technique: `kairo-technique-classes-statebypass-hwflash.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **firmware** · auth **machine** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- STATEBYPASS
- HWFLASH
- out-of-order OTA/bootloader stages — N+2 before N+1

## Probe adjustment (firmware × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
