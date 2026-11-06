# MASTG WebView JS Bridge (MASTG-PLATFORM-05) — android / high-priv

- source canon: `spydermonkey/mobile-canon.md`
- base technique: `spydermonkey-mobile-canon-mastg-webview-js-bridge-mastg-plat.md`
- bindings: **MASTG-PLATFORM** · **CWE-749** · **ATT&CK T1557**
- context: **android** · auth **high-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- class: addJavascriptInterface exposing native to web content
- probe: static inventory + the lab webview loads the marker page
- wall: lab only

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
