# DNSSEC and CAA absence

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-CONF** · **CWE-693** · **ATT&CK T1014**
- generated: 2026-11-06

## The technique

Unsigned zones and missing CAA = issuance-posture classes. Decisive test: record lookups — the absence documented as the posture row.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
