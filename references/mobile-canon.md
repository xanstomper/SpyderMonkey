# The Mobile Canon — MASTG/MASVS classes, family-native

> Real mobile technique classes with the family's probe shape and wall.
> Header = technique; body = class, probe, wall. Deterministic.

## MASTG Sensitive Data in Logs (MASTG-STORAGE-01)

- class: app logging credentials, tokens, PII to logcat
- probe: read the app's own logs on a LAB device; grep for the test account's markers
- wall: lab devices only; no third-party apps touched

## MASTG Sensitive Data in Local Storage (MASTG-STORAGE-02)

- class: shared prefs / sqlite / files holding credentials unencrypted
- probe: read the app sandbox on the lab device; diff the storage before/after a login
- wall: lab device, lab app; the finding is the storage class, not the data

## MASTG Data in Clipboard and Keyboard Cache (MASTG-STORAGE-04)

- class: clipboard sync + keyboard autocorrect retaining secrets
- probe: paste a marker, inspect the keyboard cache db
- wall: lab only

## MASTG Screenshots and Backgrounding (MASTG-STORAGE-05)

- class: task-switcher snapshot exposing session screens
- probe: background the app, pull the snapshot from the lab device
- wall: lab only

## MASTG Hardcoded Secrets in Code (MASTG-CRYPTO-RESILIENCE)

- class: api keys, jks keystores, endpoints in the binary
- probe: static strings dump of the lab build; compare against the known-good key list
- wall: read-only static analysis of the artifact the scope declares

## MASTG Weak Cryptography (MASTG-CRYPTO-02)

- class: ECB mode, MD5/SHA1, hardcoded IVs, predictable random
- probe: decompile the lab build, inventory the crypto primitives per MASVS-CRYPTO
- wall: static inventory; no crypto oracle execution

## MASTG Insecure Random (MASTG-CRYPTO-03)

- class: java.util.Random / non-CSPRNG for tokens
- probe: static scan + session-token structure check (the SESSION class on mobile)
- wall: read-only

## MASTG Certificate Pinning Bypass (MASTG-NETWORK-02)

- class: pinning that can be bypassed at runtime (frida/objection)
- probe: LAB DEVICE — attempt the documented runtime bypass, prove traffic visibility
- wall: lab device + lab cert only; never against a device the scope doesn't own

## MASTG Cleartext Traffic (MASTG-NETWORK-01)

- class: http / mixed-content on the mobile client
- probe: mitm on the lab proxy; inventory every cleartext request
- wall: lab proxy; the app under scope only

## MASTG Exported Components (MASTG-PLATFORM-03)

- class: exported activities/providers/receivers callable cross-app
- probe: static manifest inventory + lab-device intent probes
- wall: lab device; no third-party interaction

## MASTG WebView JS Bridge (MASTG-PLATFORM-05)

- class: addJavascriptInterface exposing native to web content
- probe: static inventory + the lab webview loads the marker page
- wall: lab only

## MASTG Deep Links and Intent Redirection (MASTG-PLATFORM-06)

- class: hijackable deep links, intent passthrough
- probe: static link inventory; am-probe the lab app with crafted intents
- wall: lab device

## MASTG Backup Extraction (MASTG-STORAGE-06)

- class: adb backup / iOS backup exposing app data
- probe: lab backup of the lab app; inventory the extracted class
- wall: lab only

## MASTG Runtime Detection Evasion (MASTG-RESILIENCE)

- class: root/jailbreak/frida detection in the app
- probe: LAB — document which detectors fire; the bypass is proof of weakness, not a foothold
- wall: lab only; no distribution of bypass tooling

## MASTG Anti-Tampering (MASTG-RESILIENCE-02)

- class: integrity checks on the binary
- probe: lab build resign/probe; document the response
- wall: lab only

## MASTG Mobile IPC Surface (MASTG-PLATFORM-04)

- class: binder/intent IPC exposing privileged actions
- probe: static inventory + lab probes
- wall: lab only

## MASTG Biometric Flow (MASTG-AUTH-02)

- class: biometric auth where fallback breaks the model
- probe: lab — exercise the documented fallback paths; the differential is the proof
- wall: lab only

## MASTG Session Handling on Mobile (MASTG-AUTH-01)

- class: token storage/renewal/invalidation on the client
- probe: lab — token lifecycle diff; the SESSION class applies
- wall: lab only
