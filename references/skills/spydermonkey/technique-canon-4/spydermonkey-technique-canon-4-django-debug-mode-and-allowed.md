# Django debug mode and ALLOWED_HOSTS gaps

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- generated: 2026-11-06

## The technique

DEBUG=true tracebacks (settings/secrets in the error page) and the 404 debug page. Decisive test: trigger a controlled 404/500 — the traceback panel is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
