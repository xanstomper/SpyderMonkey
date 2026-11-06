# CI/CD pipeline injection and artifact poisoning (documented classes)

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

PR-triggered workflows executing fork-controlled code (pull_request_target misuse) and artifact substitution. Decisive test: workflow YAML analysis — the misconfiguration IS the finding (the exploit is reported as the mechanism writeup).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
