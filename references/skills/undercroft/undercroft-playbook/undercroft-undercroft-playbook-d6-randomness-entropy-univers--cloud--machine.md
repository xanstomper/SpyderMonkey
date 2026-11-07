# D6 — RANDOMNESS & ENTROPY (universal) — cloud / machine

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-d6-randomness-entropy-univers.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **cloud** · auth **machine** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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
