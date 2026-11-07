# Commit-reveal verification (reverse-consumed hash chains) — wasm / service

- source canon: `holyshit-mode/web-integrity-masking-leaks.md`
- base technique: `holyshit-mode-web-integrity-masking-leaks-commit-reveal-veri.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **wasm** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

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

## Probe adjustment (wasm × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
