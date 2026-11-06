# IDOR beyond the object id — filter/sort leakage

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-06

## The technique

Enumeration via filter operators (`?sort=-balance`) and range queries reading relative order without direct object access. Decisive test: sort/filter on a field across two of YOUR objects revealing a third's rank — the oracle is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
