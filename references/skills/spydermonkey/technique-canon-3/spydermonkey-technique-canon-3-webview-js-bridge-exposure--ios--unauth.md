# WebView JS-bridge exposure — ios / unauth

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-webview-js-bridge-exposure.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **ios** · auth **unauth** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

addJavascriptInterface/WebViewAssetLoader exposing native methods to remote content. Decisive test: bridge methods listed from the decompiled build — the reachable-native-surface map is the finding.

## Probe adjustment (ios × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
