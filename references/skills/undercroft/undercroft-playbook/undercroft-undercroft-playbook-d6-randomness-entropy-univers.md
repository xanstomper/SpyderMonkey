# D6 — RANDOMNESS & ENTROPY (universal)

- source canon: `undercroft/undercroft-playbook.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

Wherever the target generates outcomes or secrets. Observation-based on declared
estate flows; sampling on the operator's own accounts; threshold = documented
tolerance, never noise.

| Seam | Analysis (observation) | Confirmed-when |
|---|---|---|
| commit-reveal RNG | seed/nonce structure: what is revealed, when, by whom (games/lotteries/provably-fair) | nonce reuse or predictable seed window |
| distribution bias | skew on N ≥ 1000 observed outcomes vs documented expectation | divergence beyond documented tolerance |
| seed-timing | correlation between seed selection and server event stream | seed-timing dependency |
| modulo/precision | RNG loop boundaries: drift, modulo bias, precision edges | measurable bias on crafted input |
| verification binding | any player-verifiable check actually binds the server-side value | server value unconstrained by the check |
| token/OTP entropy | generation structure of OTPs/tokens (alphabet, TTL, rate, retry) | reduced entropy / predictable window / replay |

### Worked domain example — auditing shipped odds math from client bundles (casino RTP audit)

1. Extract game-config regions from the verifier/game chunks: search for
   `fairValueProduces|roundMultiplier|weights|slug:"` and pull ±12KB context.
2. Reconstruct the fair multiplier per outcome: `fair = 1/P(outcome)` where P comes
   from the shipped `weights` table (weights summing to 100 are percentages).
3. Verify every ladder rung against `rung(f) = edge × fair^floor` — a consistent
   constant across ALL difficulties/floors means the math is sound; a rung
   off-formula, or an inverted derivation for one mode, is the finding.
4. Check rounding direction on every printed value: flooring in the USER's favor
   at scale is a margin finding even when the formula is right.
5. If outcome derivation never ships client-side (server-only math), say so — the
   audit ends EXHAUSTED, not INCONCLUSIVE; the remaining test needs an account +
   browser vantage and is a parked decisive test, not a hole in the sweep.

The same method transfers to ANY shipped-math audit: pricing ladders, fee tables,
scoring formulas, rank/elo curves — reconstruct, verify against formula, check
rounding direction, park what needs a live vantage.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
