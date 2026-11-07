# Honest drain-ceiling measurement (do NOT overstate free-AI burn) — container / high-priv

- source canon: `holyshit-mode/ssrf-via-image-url-and-drain-ceiling-measurement.md`
- base technique: `holyshit-mode-ssrf-via-image-url-and-drain-ceiling-measureme.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **container** · auth **high-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

The kill-claim instinct is "keyless premium inference => spend all the money." **Measure
before asserting a ceiling.** Two mechanisms crushed the worst case on the target:

1. **Throughput is latency-bound, not rate-bound.** A single `/invocations` completion took
   ~37s (cold / scale-to-zero worker). At 3-4 concurrent the sustained rate was **~0.2-1 req/s**,
   NOT thousands. With modest `max_tokens` that is **pennies-to-low-dollars/hour**, not a
   wallet-emptier.
2. **The scale-to-max lever was non-functional.** A `scale_elastic_ep`-style control-write that
   **executes at size=1 but returns `500 Scale failed` for every size>1** means you CANNOT force
   GPU allocation — the endpoint is a live vuln (unauth write) but non-destructive in practice.
   Verify by: (a) actually try the trigger, (b) read the is-scaling flag = false, (c) read the
   usage ledger before/after — unchanged cost means no GPU was allocated.

**Bound-burn discipline in action:** because "max drain in 1 second" is a burn-until-gone ask,
run a **bounded, instrumented, auto-stopped measurement** (fixed window, capped concurrency +
max_tokens, every call/token logged, scale-back after) and extrapolate the $/hr. The vulnerability
proof is the amount an attacker *could* burn, not the amount actually burned. Report the honest
measured ceiling even when it kills the operator's "we can drain everything" assumption — that is
a more valuable truth than an inflated claim. If the operator confirms the target is THEIR own
upstream, the operator-owning test is in-scope but still bounded; an unbounded drain on a third-party
upstream is the attack itself, not a test.

## Probe adjustment (container × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
