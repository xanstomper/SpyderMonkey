# Next.js model-page flight data (RSC $S) leaks promo/free-tier + trust-flag mismatch — graphql / machine

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-nex.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- context: **graphql** · auth **machine** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (graphql × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
