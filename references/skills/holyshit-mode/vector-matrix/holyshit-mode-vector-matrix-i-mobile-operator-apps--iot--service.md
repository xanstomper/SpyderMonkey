# I. MOBILE (operator apps) — iot / service

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-i-mobile-operator-apps.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **iot** · auth **service** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- APK/IPA static: hardcoded keys, debuggable flags, exported components, backup=true
- Deeplink handling: unvalidated parameter → WebView JS injection
- Cert pinning gaps; runtime hooking (frida) on own builds
- IPC exposure: broadcast receivers, content providers, exported services (Android)
- Keychain/keystore analysis: key accessibility classes, jailbreak-detection bypass
- WebView bridge: JS-native bridge functions callable from loaded content
- App extension abuse: share extensions, keyboard extensions leaking input
- OTA update mechanism: signing validation, rollback protection

## Probe adjustment (iot × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
