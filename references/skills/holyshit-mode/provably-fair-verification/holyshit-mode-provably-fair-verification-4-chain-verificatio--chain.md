# 4. Chain verification (the decisive test) — chain composition

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-4-chain-verificatio.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
