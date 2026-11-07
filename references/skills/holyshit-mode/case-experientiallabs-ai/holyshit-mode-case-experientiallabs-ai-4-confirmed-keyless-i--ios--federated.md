# 4. CONFIRMED — Keyless internal usage/billing ledger leak on `gateway.xplabs.ai` (score 70) — ios / federated

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-4-confirmed-keyless-i.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **ios** · auth **federated** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

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

## Probe adjustment (ios × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
