# MASTG Certificate Pinning Bypass (MASTG-NETWORK-02) — iot / unauth

- source canon: `spydermonkey/mobile-canon.md`
- base technique: `spydermonkey-mobile-canon-mastg-certificate-pinning-bypass-m.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **iot** · auth **unauth** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- class: pinning that can be bypassed at runtime (frida/objection)
- probe: LAB DEVICE — attempt the documented runtime bypass, prove traffic visibility
- wall: lab device + lab cert only; never against a device the scope doesn't own

## Probe adjustment (iot × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
