# 2. CALIBRATE the "drain/scale to max" ceiling by MEASUREMENT, don't assert max-shock — ci-cd / root

- source canon: `holyshit-mode/llm-gateway-ssrf-oracle-and-drain-calibration.md`
- base technique: `holyshit-mode-llm-gateway-ssrf-oracle-and-drain-calibration-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **ci-cd** · auth **root** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

A keyless free-AI + unauth-scale surface looks like a wallet-emptier, but measure before claiming:
- **Throughput is latency-bound, not high.** A cold/scale-to-zero worker returns each completion in
  ~37s; at 2-3 concurrent that's ~0.2-0.3 req/s sustained, NOT hundreds. Re-measure warm before stating
  a drain rate. Convert real tok/sec × price → cents/hour, not "unlimited."
- **"Scale to max" may be non-functional.** `scale_elastic_ep {"new_data_parallel_size": N}` can return
  200 for `1` but **500 `Scale failed` for ANY size > 1** — the elastic backend is broken, so the pool
  is pinned at 1 engine and "scale up then loop requests" is DEAD despite the unauth write existing.
  Confirm max viable size with one bounded step + a `/usage` before/after delta.
- **Honest verdict is often "pennies/hour," not "spend all the money."** VULNERABILITY (endpoint exists,
  fix it) and IMPACT (what you measured) are separate axes — record them separately. This is the most
  trust-preserving habit when an operator pushes "how much can we drain / scale to max and loop."
- Both drain levers can be real-but-circumscribed; running an uncontrolled "scale to max + infinite
  loop" is a live metered burn unless the operator owns the upstream — bound it, log it, auto-stop,
  extrapolate. No unbounded drain.

## Probe adjustment (ci-cd × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
