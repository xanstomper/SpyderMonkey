# I. MOBILE (operator apps) — worker / machine

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-i-mobile-operator-apps.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **worker** · auth **machine** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- APK/IPA static: hardcoded keys, debuggable flags, exported components, backup=true
- Deeplink handling: unvalidated parameter → WebView JS injection
- Cert pinning gaps; runtime hooking (frida) on own builds
- IPC exposure: broadcast receivers, content providers, exported services (Android)
- Keychain/keystore analysis: key accessibility classes, jailbreak-detection bypass
- WebView bridge: JS-native bridge functions callable from loaded content
- App extension abuse: share extensions, keyboard extensions leaking input
- OTA update mechanism: signing validation, rollback protection

## Probe adjustment (worker × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
