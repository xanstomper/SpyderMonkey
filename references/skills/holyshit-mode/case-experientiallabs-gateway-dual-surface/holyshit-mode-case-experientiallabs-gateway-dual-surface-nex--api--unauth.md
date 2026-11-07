# Next.js model-page flight data (RSC $S) leaks promo/free-tier + trust-flag mismatch — api / unauth

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-nex.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- context: **api** · auth **unauth** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

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

## Probe adjustment (api × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
