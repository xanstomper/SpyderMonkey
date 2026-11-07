# 4. Subscription / free-tier entitlement mining from the model page (hydration leak) — mesh / machine

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- base technique: `holyshit-mode-vllm-gateway-internal-fleet-ssrf-4-subscriptio.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- context: **mesh** · auth **machine** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Model page root (`/models/<slug>` on the Next.js app) leaks full promo/subscription config in the
RSC `self.__next_f` flight payload:
`free_input_tokens_per_day|hour`, `free_output_tokens_per_day|hour`, `requires_payment`,
`requires_payment_method`, `verifyChargeUsd`, `badge_style:"allowance"`, `marketedPromo`. Tells you
the exact free-tier gate (e.g. "saved card + $1 settled charge") and the daily/hourly token budget —
primes the card-gate-bypass / credits-overflow escalation, which needs an authenticated context to
test (HYPOTHESIS until proven).

## Probe adjustment (mesh × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
