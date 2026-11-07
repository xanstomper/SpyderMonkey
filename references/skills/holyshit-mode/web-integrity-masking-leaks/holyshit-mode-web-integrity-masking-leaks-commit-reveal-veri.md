# Commit-reveal verification (reverse-consumed hash chains)

- source canon: `holyshit-mode/web-integrity-masking-leaks.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-04

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
