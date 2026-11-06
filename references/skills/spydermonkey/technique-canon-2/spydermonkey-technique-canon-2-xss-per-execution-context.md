# XSS per-execution-context

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-06

## The technique

HTML-body, attribute, JS-string, URL-attribute (`href`/`src` javascript:), and CSS contexts each need THEIR encoding-vocabulary variant. Decisive test: the reflected marker in the correct context form — context-specific execution in YOUR session is the proof; stored/cross-principal framing stays hypothesis without a second principal.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
