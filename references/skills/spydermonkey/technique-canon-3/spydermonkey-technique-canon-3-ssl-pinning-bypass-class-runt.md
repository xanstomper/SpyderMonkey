# SSL pinning bypass class (runtime, own app)

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

Frida/objection pinning defeats on YOUR OWN app builds — the class writeup maps the app's trust chain. Decisive test: pinning observable and the defeat reproducible on your build.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
