# 4. Model-page hydration data leak (Next.js)

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

The web model page (`/models/<slug>`) embeds the FULL entitlement config in `self.__next_f`
hydration JSON, readable pre-auth:
- `promo-free-chip` badge text + `free_input_tokens_per_day`, `free_output_tokens_per_day`,
  `free_input_tokens_per_hour`, etc. — exact promotional free-tier allowance.
- `requires_payment`, `requires_payment_method`, `verifyChargeUsd` (the $1 card gate),
  `showCardGate`, `model_terms`, `token_rates`.
- **Trust-flag mismatch detector:** cross-check catalog `requires_payment`/`requires_purchase`
  vs the page-hydration `requires_payment` — they disagreed for `gemini-4-argon`
  (catalog false, runtime true). Flag inconsistencies as an escalation lead.
- A model served on a real cloud provider (`gemini`,`anthropic`,`openai`) is NOT on the weakened
  internal `experiential_cloud` lane → NOT reachable via keyless `/invocations`. Check the
  provider before assuming free-AI reachability.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
