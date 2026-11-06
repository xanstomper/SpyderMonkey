# PLAYBOOK A — FINTECH / PAYMENTS — cloud / unauth

- source canon: `holyshit-mode/operational-playbooks.md`
- base technique: `holyshit-mode-operational-playbooks-playbook-a-fintech-payme.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **cloud** · auth **unauth** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

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

## Probe adjustment (cloud × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
