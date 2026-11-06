# CSS injection and clickjacking depth

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-06

## The technique

Attribute-exfil CSS and framable state-changers (padding/preview techniques). Decisive test: local harness render — the exfil channel shown in the lab, never against a third party.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
