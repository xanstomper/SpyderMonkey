# Login throttling response differential

- source canon: `spydermonkey/technique-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## The technique

Locked vs unlocked account responses differ (message/timing/length) = enumeration oracle. Decisive test: your test account (existing) vs random string (nonexisting) — differentiable = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
