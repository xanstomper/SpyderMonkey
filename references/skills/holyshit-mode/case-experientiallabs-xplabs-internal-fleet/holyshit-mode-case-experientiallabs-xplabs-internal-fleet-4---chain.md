# 4. Model-page hydration data leak (Next.js) — chain composition

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- base technique: `holyshit-mode-case-experientiallabs-xplabs-internal-fleet-4-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
