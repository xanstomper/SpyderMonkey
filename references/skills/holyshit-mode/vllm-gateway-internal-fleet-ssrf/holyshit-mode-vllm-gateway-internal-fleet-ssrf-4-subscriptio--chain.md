# 4. Subscription / free-tier entitlement mining from the model page (hydration leak) — chain composition

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-4-subscriptio.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Model page root (`/models/<slug>` on the Next.js app) leaks full promo/subscription config in the
RSC `self.__next_f` flight payload:
`free_input_tokens_per_day|hour`, `free_output_tokens_per_day|hour`, `requires_payment`,
`requires_payment_method`, `verifyChargeUsd`, `badge_style:"allowance"`, `marketedPromo`. Tells you
the exact free-tier gate (e.g. "saved card + $1 settled charge") and the daily/hourly token budget —
primes the card-gate-bypass / credits-overflow escalation, which needs an authenticated context to
test (HYPOTHESIS until proven).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
