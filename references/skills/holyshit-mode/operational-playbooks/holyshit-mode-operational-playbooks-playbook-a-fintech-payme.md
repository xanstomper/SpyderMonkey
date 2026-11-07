# PLAYBOOK A — FINTECH / PAYMENTS

- source canon: `holyshit-mode/operational-playbooks.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-07

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

**Objective**: validate PCI-DSS boundary integrity, transaction logic, and fraud controls.

**Phase 1 — Recon**
- CT logs + Wayback on `%.target.tld` — separate payment gateway domains from marketing.
- ASN map: payment processors, fraud vendors, banking partners (third-party = out of scope).
- GitHub/org sweep for processor API keys, webhook secrets, test-card configs.

**Phase 2 — Payment Flow Analysis**
- **Transaction state machine**: map every state transition (auth → capture → refund → void).
  Test race conditions on duplicate capture (single-packet attack).
- **Amount manipulation**: negative/zero/decimal overflow, currency confusion (USD vs JPY
  decimal places), coupon stacking, post-hoc price edits in cart APIs.
- **Webhook integrity**: signature validation, timestamp/nonce enforcement, replay window.
  Send signed-but-stale events to test replay acceptance.
- **3DS / SCA validation**: bypass via fallback APIs, merchant-initiated transaction abuse,
  exemption thresholds (low-value exemption farming).

**Phase 3 — Auth & Session**
- Session fixation via `?token=` params (referrer leakage to third-party analytics = HOLY SHIT).
- JWT validation: alg=none, kid injection, weak HMAC secret (hashcat), no audience check.
- OAuth state/redirect validation on payment-provider handoffs.

**Phase 4 — API Surface**
- IDOR on transaction IDs (cross-account access with second test account only).
- Mass assignment: `is_refunded`, `is_authorized`, `amount_final` injection on PUT.
- GraphQL introspection on payment APIs; field-level auth on `card_token`, `bank_account`.

**Phase 5 — Infrastructure**
- PCI boundary: is card data touching your servers or processor-hosted fields? Look for
  PAN in logs, PAN in URLs, PAN in analytics events.
- Public buckets: S3/GCS with transaction exports, settlement files, chargeback evidence.

**Deliverable**: transaction-flow map, race-condition findings, webhook-replay validation,
PCI-boundary assessment, IDOR/authorization gaps.

---

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
