# PLAYBOOK B — HEALTHCARE-ADJACENT (NOT PROVIDER SYSTEMS)

- source canon: `holyshit-mode/operational-playbooks.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

**Scope note**: Hospital EHRs, clinical devices, and patient-care systems are RESTRICTED
TARGETS. This playbook covers adjacent business systems: patient portals, billing platforms,
telehealth scheduling, wellness apps, medical-device companion apps.

**Phase 1 — Recon**
- Subdomain enumeration: separate clinical systems from business systems.
- Wayback for old patient-portal versions; ghost-route diffing.

**Phase 2 — PHI Boundary Validation**
- Test whether PHI appears in URLs, logs, analytics, or third-party trackers.
- Validate de-identification: can you re-identify "anonymized" records via
  quasi-identifiers (ZIP + DOB + gender)?
- API responses: does `GET /appointment/123` leak `diagnosis_code`, `notes`, `ssn`?

**Phase 3 — Auth & Access**
- Role-based access: patient vs provider vs admin — BFLA on every privileged endpoint.
- Break-glass access: is emergency-access logged and auditable? Test with scoped break-glass
  account.
- Family/caregiver proxy access: can Patient A view Patient B's records via shared links?

**Phase 4 — Business Logic**
- Appointment race conditions: double-booking, overbooking provider slots.
- Prescription-refill logic: early-refill detection bypass, quantity manipulation.
- Telehealth session tokens: predictable? Replayable? TTL enforcement?

**Phase 5 — Mobile Companion Apps**
- Hardcoded API keys, debug flags, exported components (Android), keychain analysis (iOS).
- Deeplink handling: unvalidated parameter → WebView JS injection → session theft.

**Deliverable**: PHI-boundary map, role-authorization matrix, proxy-access findings,
mobile-trust findings, de-identification validation.

---

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
