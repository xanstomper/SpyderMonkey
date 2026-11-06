# WebView JS-bridge exposure

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

addJavascriptInterface/WebViewAssetLoader exposing native methods to remote content. Decisive test: bridge methods listed from the decompiled build — the reachable-native-surface map is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
