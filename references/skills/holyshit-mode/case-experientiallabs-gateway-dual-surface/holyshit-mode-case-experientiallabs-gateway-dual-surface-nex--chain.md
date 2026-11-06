# Next.js model-page flight data (RSC $S) leaks promo/free-tier + trust-flag mismatch — chain composition

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-nex.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- The model page `<script>(self.__next_f=self.__next_f||[]).push([1,"...])` stream embeds the
  **full model entitlement object** to the unauthenticated viewer:
  `free_input_tokens_per_day/hout`, `requires_payment`, `requires_payment_method`,
  `showCardGate`, `verifyChargeUsd`, promo/free chips.
- **Trust-flag mismatch find:** public catalog said `requires_payment:false` /
  `requires_purchase:false`, but the runtime flight-data entitlement said
  `requires_payment:true` + `requires_payment_method:true`. Inconsistent trust flags across
  two sources on the SAME model = a flag worth recording (card-gate is the real gate).
- Technique: `curl <page> -> regex '{[^{}]{0,600}?free_[a-z_]+...}'` + grep for
  `requires_payment|showCardGate|free_|verifyChargeUsd|marketedPromo`.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
