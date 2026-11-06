# SQS/SNS policy gaps

- source canon: `spydermonkey/technique-canon-8.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

Queue/topic policies with wildcard principals or open HTTP notification endpoints. Decisive test: policy doc where readable + one subscribe-probe to YOUR endpoint = the class.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
