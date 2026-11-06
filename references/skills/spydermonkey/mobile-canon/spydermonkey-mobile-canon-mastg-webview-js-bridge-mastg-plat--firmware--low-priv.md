# MASTG WebView JS Bridge (MASTG-PLATFORM-05) — firmware / low-priv

- source canon: `spydermonkey/mobile-canon.md`
- base technique: `spydermonkey-mobile-canon-mastg-webview-js-bridge-mastg-plat.md`
- bindings: **MASTG-PLATFORM** · **CWE-749** · **ATT&CK T1557**
- context: **firmware** · auth **low-priv** · chain role **pivot**

## Context

- platform: the check lives in the image — uart/flash/ota paths, no-gain read-only dumps
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- class: addJavascriptInterface exposing native to web content
- probe: static inventory + the lab webview loads the marker page
- wall: lab only

## Probe adjustment (firmware × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
