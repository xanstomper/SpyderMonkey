# 2. CALIBRATE the "drain/scale to max" ceiling by MEASUREMENT, don't assert max-shock

- source canon: `holyshit-mode/llm-gateway-ssrf-oracle-and-drain-calibration.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
