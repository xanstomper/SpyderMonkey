# PLAYBOOK B — HEALTHCARE-ADJACENT (NOT PROVIDER SYSTEMS) — chain composition

- source canon: `holyshit-mode/operational-playbooks.md`
- base technique: `holyshit-mode-operational-playbooks-playbook-b-healthcare-ad.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
