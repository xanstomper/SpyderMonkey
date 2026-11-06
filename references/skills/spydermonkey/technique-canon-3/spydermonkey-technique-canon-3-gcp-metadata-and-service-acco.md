# GCP metadata and service-account surface

- source canon: `spydermonkey/technique-canon-3.md`
- bindings: **WSTG-PARA** · **CWE-113** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

metadata.google.internal classes + service-account key exposure in artifacts. Decisive test: metadata header requirement (Metadata-Flavor) honored/refused — the delta is the posture.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
