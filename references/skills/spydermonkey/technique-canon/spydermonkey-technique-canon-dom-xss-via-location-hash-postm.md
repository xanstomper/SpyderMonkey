# DOM XSS via location.hash / postMessage

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

hash-borne sinks and postMessage handlers without origin checks. Decisive test: postMessage from YOUR page to the in-scope window — handler executes with your payload; the alert/echo in YOUR browser session is the proof (self-XSS framing stays hypothesis unless it crosses principals).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
