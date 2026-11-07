# I. MOBILE (operator apps) — android / high-priv

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-i-mobile-operator-apps.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **android** · auth **high-priv** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- APK/IPA static: hardcoded keys, debuggable flags, exported components, backup=true
- Deeplink handling: unvalidated parameter → WebView JS injection
- Cert pinning gaps; runtime hooking (frida) on own builds
- IPC exposure: broadcast receivers, content providers, exported services (Android)
- Keychain/keystore analysis: key accessibility classes, jailbreak-detection bypass
- WebView bridge: JS-native bridge functions callable from loaded content
- App extension abuse: share extensions, keyboard extensions leaking input
- OTA update mechanism: signing validation, rollback protection

## Probe adjustment (android × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
