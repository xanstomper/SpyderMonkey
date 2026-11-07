# 4. Subscription / free-tier entitlement mining from the model page (hydration leak)

- source canon: `holyshit-mode/vllm-gateway-internal-fleet-ssrf.md`
- bindings: **WSTG-BUSL-05** · **CWE-285** · **ATT&CK T1068**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Model page root (`/models/<slug>` on the Next.js app) leaks full promo/subscription config in the
RSC `self.__next_f` flight payload:
`free_input_tokens_per_day|hour`, `free_output_tokens_per_day|hour`, `requires_payment`,
`requires_payment_method`, `verifyChargeUsd`, `badge_style:"allowance"`, `marketedPromo`. Tells you
the exact free-tier gate (e.g. "saved card + $1 settled charge") and the daily/hourly token budget —
primes the card-gate-bypass / credits-overflow escalation, which needs an authenticated context to
test (HYPOTHESIS until proven).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
