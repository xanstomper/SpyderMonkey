# D6 — RANDOMNESS & ENTROPY (universal) — chain composition

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-d6-randomness-entropy-univers.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
