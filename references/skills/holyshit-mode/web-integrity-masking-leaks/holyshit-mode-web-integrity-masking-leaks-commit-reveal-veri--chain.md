# Commit-reveal verification (reverse-consumed hash chains) — chain composition

- source canon: `holyshit-mode/web-integrity-masking-leaks.md`
- base technique: `holyshit-mode-web-integrity-masking-leaks-commit-reveal-veri.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

For a documented scheme like "a chain of N SHA-256 hashes from one secret seed,
consumed in reverse, each game uses the previous hash":

1. Capture CONSECUTIVE rounds from the public wire (game_starting/game_crash
   events, two sessions for independence).
2. Check `sha256(later_round_hash_as_hex_ASCII) == earlier_round_hash`.
3. Exact match across independent captures = the chain is REAL and pre-generated
   (a post-hoc fabricated hash cannot chain two rounds).

The two hashes + one sha256 call ARE the public rebuttal to any "provably fair
is fake" claim — publish them. If the only hash ships in the SAME event as the
result AND consecutive rounds don't chain, the per-round commitment is
unverifiable (remediable: publish hash pre-round, reveal seed post-round).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
