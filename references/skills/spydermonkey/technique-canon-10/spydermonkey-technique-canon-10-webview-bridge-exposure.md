# WebView bridge exposure

- source canon: `spydermonkey/technique-canon-10.md`
- bindings: **MASTG-PLATFORM** · **CWE-749** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

addJavascriptInterface exposing native methods to remote content. Decisive test: bridge method inventory from the build + the remote-content reach path = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
