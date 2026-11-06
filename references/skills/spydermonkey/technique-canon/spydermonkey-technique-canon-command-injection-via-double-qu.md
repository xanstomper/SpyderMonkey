# Command injection via double-quote/pipe variants

- source canon: `spydermonkey/technique-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

The documented class vocabulary (backtick, $( ), newline, %0a) applied ONE variant per request. Decisive test: an out-of-band marker (DNS to your registered domain) beats response-diff for blind injection — the marker arrival is the proof.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
