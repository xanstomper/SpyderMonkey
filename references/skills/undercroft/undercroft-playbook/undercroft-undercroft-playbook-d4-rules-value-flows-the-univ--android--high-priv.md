# D4 — RULES & VALUE FLOWS (the universal discipline) — android / high-priv

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-d4-rules-value-flows-the-univ.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **android** · auth **high-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — frida/objection at the runtime, MASTG methodology
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Every rule seam ships with a NO-GAIN probe plan from the engine
(`undercroft probe --class <seam>`): 15 seam classes — precision, concurrency,
arbitrage, entitlement, calculation, randomness, conversion, credits, boundary,
journal, riskless, bounds, state, webhook, time. Each plan fixes Δ, the minimal
probe, the verify, the cost (reversible), and confirmed-when.

**Where these seams live (domain map — the same seams, any system):**

| Domain | Typical undercroft seams |
|---|---|
| e-commerce / marketplaces | cart/checkout state races, refund math, price/quote arbitrage, coupon stacking, inventory decrement races, seller payout calc |
| fintech / payments / crypto | conversion/fee asymmetry, ledger drift, idempotency-key replay, double-spend concurrency, withdrawal bounds, rounding direction at scale |
| SaaS / subscriptions | plan-limit bypass, seat/entitlement inflation, trial/TTL logic, proration math, quota reset seams, feature-gate trust in client |
| booking / logistics / travel | double-book concurrency, cancellation/void counting, timezone/DST edges, overbooking bounds, state-machine bypass on orders |
| social / platforms | rate/credit economies, referral loops, moderation-workflow state bypass, cross-tenant reads (org/workspace id in body) |
| gaming / gambling | RNG structure (provably-fair or not), loot/odds math, bonus flows, currency conversion, balance races |
| infra / IoT backends | device-claim entitlement, command replay (webhooks/queues), OTA/update state machines, telemetry journal integrity |

NO-GAIN: probe minimally, reverse every transaction, record refunds — nothing of
value is ever kept. The proof is the flow divergence, never the gain.

| Seam | Probe (minimal, reversible, NO-GAIN) | Confirmed-when |
|---|---|---|
| precision/rounding | max-precision + unit-conversion edges on crafted amounts | reconciled result ≠ naive sum; drift recorded |
| concurrency | N parallel submits of the same logical unit (own account) | duplicate applied / negative state |
| arbitrage | two correlated values priced inconsistently; minimal opposing actions | riskless-gain window exists |
| entitlement | flow-order inversion / parallel claim on promo-trial-referral flows | duplicate or unearned grant accepted |
| calculation | crafted inputs outside documented bounds through the calc | result overpays/diverges from independent math |
| randomness | N observed outcomes; check structure + distribution | bias/reuse/predictable window ≥ tolerance |
| conversion | round-trip conversions at boundary amounts (fees + rounding direction) | nonzero drift / fee asymmetry |
| credits | earn/burn inversion or account-merge arithmetic (own accounts) | value created from nothing |
| boundary | org/plan/tenant id switch in scoped requests | foreign resource 200 |
| journal | statement vs journal divergence; voided/cancelled op counting | reconciliation gap (read-only) |
| riskless | spendability scope of demo/trial/free credits | credit accepted where terms forbid |
| bounds | max+1 / negative / fractional inputs through validation | out-of-bounds accepted |
| state | out-of-order transitions on order/workflow/approval flows | illegal-but-accepted state |
| webhook | replay a captured callback with same dedup key (own endpoint) | duplicate effect / missing idempotency |
| time | expiry/grace/TTL edges: renew before/after boundary, clock skew | expired-but-accepted / pre-expiry grant |

## Probe adjustment (android × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
