# MASTG Runtime Detection Evasion (MASTG-RESILIENCE) — iot / low-priv

- source canon: `spydermonkey/mobile-canon.md`
- base technique: `spydermonkey-mobile-canon-mastg-runtime-detection-evasion-ma.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **iot** · auth **low-priv** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- class: root/jailbreak/frida detection in the app
- probe: LAB — document which detectors fire; the bypass is proof of weakness, not a foothold
- wall: lab only; no distribution of bypass tooling

## Probe adjustment (iot × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
