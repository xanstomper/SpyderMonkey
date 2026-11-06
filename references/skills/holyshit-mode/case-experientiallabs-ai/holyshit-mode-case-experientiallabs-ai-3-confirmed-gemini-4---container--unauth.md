# 3. CONFIRMED — `gemini-4-argon` promotional free-tier + trust-flag mismatch (score 55) — container / unauth

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-3-confirmed-gemini-4-.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- context: **container** · auth **unauth** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- **EVIDENCE (model page `platform.experientiallabs.ai/models/gemini-4-argon` hydration):**
  - `promo-free-chip` badge: "Free allowance available to eligible accounts."
  - Free hourly tokens: `free_input_tokens_per_hour: 832500`, `free_output_tokens_per_hour: 166500`.
  - `requires_payment_method: true` — free tier needs a saved card + settled charge to unlock
    (docs-confirmed bar).
  - **Trust-flag mismatch:** the public catalog shows `requires_payment:false` /
    `requires_purchase:false` for `gemini-4-argon`, but the runtime entitlement context shows
    `requires_payment:true`. Inconsistent trust flags across the two reads.
- **IMPACT:** Promotional free-tier model (intro pricing through 2026-11-30). Whether the
  card/$1 gate is bypassable (credits-overflow switch, `available_to_org:null` trust gap) is
  the open escalation on this model — needs an authenticated context to test honestly.
- **CONFIDENCE:** High on the page leak; the free-tier bypass itself is UNTESTED (HYPOTHESIS).

## Probe adjustment (container × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
