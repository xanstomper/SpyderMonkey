# Entropy/PRNG weakness classes

- source canon: `spydermonkey/technique-canon-6.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Predictable tokens (Math.random, time-seeded PRNG, sequential ids) — the SPY-048/058 fingerprint-mint family is the live example. Decisive test: N sampled tokens from YOUR OWN sessions → entropy arithmetic (pairwise deltas, structure) — a sub-64-bit space or visible structure = the finding; an evenly-distributed space is the banked negative (the ggpoker alias test).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
