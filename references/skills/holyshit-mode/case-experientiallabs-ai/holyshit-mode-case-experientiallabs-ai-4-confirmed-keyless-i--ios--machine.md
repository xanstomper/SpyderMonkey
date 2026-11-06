# 4. CONFIRMED — Keyless internal usage/billing ledger leak on `gateway.xplabs.ai` (score 70) — ios / machine

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-4-confirmed-keyless-i.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **ios** · auth **machine** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- **EVIDENCE:** `GET https://gateway.xplabs.ai/usage.json` (no auth) returns full internal
  ledger: `organization_id:"local"`, totals + per-`identity` breakdown.
- **Identities leaked keyless:** `kion-unlimited`, `opflow`, `platform`, `vincent`
  (internal serving tenant/account names) with per-identity requests, token counts, and
  **known_estimated_cost_micro_usd** (total ~`1,753,588` µUSD ≈ $1.75).
- `GET /usage` also serves a human HTML page of the same ledger.
- **IMPACT:** Internal account-name enumeration + wallet/usage/spend exposure on operator-
  owned infra. Feeds further targeted abuse (tenant enumeration).
- **CONFIDENCE:** High — raw JSON keys verified.

## Probe adjustment (ios × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
