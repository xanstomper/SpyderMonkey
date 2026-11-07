# 4. Model-page hydration data leak (Next.js) — cloud / machine

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- base technique: `holyshit-mode-case-experientiallabs-xplabs-internal-fleet-4-.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- context: **cloud** · auth **machine** · chain role **pivot**

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (cloud × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
