# 3. CONFIRMED — `gemini-4-argon` promotional free-tier + trust-flag mismatch (score 55) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-ai.md`
- base technique: `holyshit-mode-case-experientiallabs-ai-3-confirmed-gemini-4-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
