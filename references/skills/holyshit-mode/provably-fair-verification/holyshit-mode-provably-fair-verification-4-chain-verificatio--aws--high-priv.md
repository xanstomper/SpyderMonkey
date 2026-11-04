# 4. Chain verification (the decisive test) — aws / high-priv

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-4-chain-verificatio.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **aws** · auth **high-priv** · chain role **pivot**

## Context

- platform: IAM/identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

For consecutive captured rounds, test the documented chain property:

```python
import hashlib
# reverse-consumption chain (hash N+1 hashes down to hash N):
hashlib.sha256(later_hash.encode()).hexdigest() == earlier_hash   # ascii-encoded
# also test bytes.fromhex encoding and the forward direction
```

- **Verified chain (across ≥3 links / 2 sessions)** = the commitment system is REAL:
  log as a negative (hardening), and hand the operator the rebuttal package — two
  consecutive public hashes + one sha256 call = live verification anyone can reproduce
  in 30 seconds. This blunts a PF-fraud extortion narrative.
- **Chain DIRECTION is the exploit gate, not link validity.** After links verify, test which
  way: `sha256(seed[N]) == seed[N+1]` = FORWARD chain = the BREAK (every reveal computes
  every future seed — the prediction Holy Shit); `sha256(seed[N+1]) == seed[N]` = REVERSE
  chain = SAFE (future seeds are preimages, underivable). State the direction in the
  ledger; a 99/99-reverse crash feed is verified-hardened, not "unverified".
- **Unverified or absent chain** = the finding; score as game-integrity (reputation +
  regulatory exposure), not a web vuln.
- **Commit-and-reveal variant (drand-seeded):** some operators publish the commitment in a
  dedicated PRE-round event (duel-family crash: `crash_hashed_pf`) and reveal `server_seed`
  + `drand_randomness` POST-crash in another (`pending_drand`). Verify
  `sha256(bytes.fromhex(server_seed)) == server_seed_hashed` — hash the HEX-DECODED bytes;
  sha256 over the utf-8 string false-mismatches and manufactures a fake "provably fair is
  fake" verdict. The drand cross-check against the public beacon (api.drand.sh,
  drand.cloudflare.com) is frequently network-blocked (403) from probe environments —
  verify the commitment layer and state EXACTLY which layers stayed unverified (derivation
  formula, beacon) rather than claiming full verification.

## Probe adjustment (aws × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
