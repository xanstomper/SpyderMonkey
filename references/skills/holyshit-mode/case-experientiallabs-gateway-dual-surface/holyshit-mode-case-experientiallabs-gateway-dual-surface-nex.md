# Next.js model-page flight data (RSC $S) leaks promo/free-tier + trust-flag mismatch

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
