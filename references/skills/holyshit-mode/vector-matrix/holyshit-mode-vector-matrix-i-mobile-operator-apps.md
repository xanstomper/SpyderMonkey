# I. MOBILE (operator apps)

- source canon: `holyshit-mode/vector-matrix.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- generated: 2026-11-04

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- APK/IPA static: hardcoded keys, debuggable flags, exported components, backup=true
- Deeplink handling: unvalidated parameter → WebView JS injection
- Cert pinning gaps; runtime hooking (frida) on own builds
- IPC exposure: broadcast receivers, content providers, exported services (Android)
- Keychain/keystore analysis: key accessibility classes, jailbreak-detection bypass
- WebView bridge: JS-native bridge functions callable from loaded content
- App extension abuse: share extensions, keyboard extensions leaking input
- OTA update mechanism: signing validation, rollback protection

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
