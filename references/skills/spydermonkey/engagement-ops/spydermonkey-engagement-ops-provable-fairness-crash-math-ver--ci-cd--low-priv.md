# Provable-fairness crash math: verify the derivation before claiming prediction — ci-cd / low-priv

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-provable-fairness-crash-math-ver.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- context: **ci-cd** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-http-backup`, `nmap-robots`, `nmap-sitemap`, `snallygaster`, `wget-mirror`, `httrack`, `gau`, `git-dumper`, `trufflehog`, `gitleaks`
- chains: `exposure-sweep`, `content`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

When a crash/multiplier game exposes round hashes, the scary claim is "outcome
predictable from public data". Test it as a decisive sweep, not a single match:

1. **Pull N≥50 real rounds from the unauthenticated history API** — the app-bundle route
   usually needs POST + JSON body (`/api/game/bet/multi/history` ← `{gameUrl: "crash",
   page: 1, pageSize: 100}`); GET on the same path answers 405 with a custom error code
   (4001-class) because the method is wrong, not the route. Rows carry
   `gameDetail` = `{hash, salt, rate, times}`.
2. **Verify chain continuity first**: in this stack `hash(N-1) = SHA256(hash(N))`
   (99/99 consecutive pairs observed) — the past chain is fully public and walkable, and
   the client bundle's `getPrevHash`/`pe` walker is this exact function. Chain integrity
   is verification-only; it does NOT make the next hash derivable (SHA256 preimage).
3. **Sweep candidate derivations against ALL non-trivial rounds** (rate ≥ ~1.05, where the
   floor can't mask a miss): HMAC-SHA256 vs SHA256 × hex-parsed vs UTF-8 message ×
   round-hash vs chain-neighbor hash × house-edge/rtp 0.90–1.00. Requiring every round to
   match is the standard; one match is coincidence. Also back-solve the implied house edge
   from (rate, first-13-hex denominator) — if no constant e fits across rounds, the
   multiplier consumes a server-side secret.
4. **0/N matches = the derivation holds a server secret — register the DECISIVE NEGATIVE
   as a finding** (PF math sound, prediction impossible from public data). A refused
   prediction claim is an audit win for the report, not a dead end; pair it with the
   corollary finding that the official verifier site may be dead (404), so players cannot
   practically verify even though the math lane is sound.

Pitfalls that cost this sweep time:

- **The operator's OWN verifier repo may carry the OLD salt — a drift finding, not a bug**: `bc-game-project/verify` and `bcgame-crash` docs pre-fill a 64-hex salt that can differ from the LIVE bundle's config salt (both start `0000000000000000000` but diverge after). Harvest salts from THREE sources and treat disagreement as its own disclosure item: (1) per-round `gameDetail.salt` from the history API (chain-head constant), (2) the live bundle config chunk, (3) committed verifier HTML/git history. Verify against CURRENT live rounds (rate + hash pairs from the same history page), not against memory of an earlier session's salt.
- **Neither salt reproducing live rates = a hop you haven't unwound, not "math is broken"**: when HMAC/sha variants with all known salts fail to turn a round hash into its rate, the live derivation may consume an extra input the verifier page doesn't show — e.g. a gameId-parameterized step (`ve(be(hash, gameId), rtp)` family). Do NOT register "verifier is stale/lying" from salt mismatch alone; the testable claim is chain integrity (below) and the decisive negative stands. A chain that verifies + derivations that don't = server-secret-backed multiplier, which is the soundness result you report.
- **Two salts, don't confuse them**: the history API's per-round `gameDetail.salt` is the
  CHAIN-HEAD constant (`mt`-style, identical every row), NOT the derivation salt. The
  derivation salt lives per-game in the config chunk (e.g. `cfg.C.salt` / the game-list
  entry's `salt`), a different 64-hex constant. Sweep both explicitly.
- **Compute with the page's own crypto, not a reimplementation**: dynamically
  `await import()` the provider chunk in-page and use its exports (e.g. ProviderMain
  exports C=HmacSHA256, D=Hex, B=SHA; config chunk carries salts/namespaces). CryptoJS-
  vs-node byte/UTF-8 parsing mismatches make identical-looking formulas disagree; the
  page's own primitives are the ground truth for what the bundle would compute.
- **A token sharing bytes with client input may share a CLOCK, not echo input**: an
  unauthenticated ticket oracle (`/test/?p=<fingerprint>`) returning a ~27-hex token
  whose middle 8 hex advance with wall-clock (epoch µs >> 12 — verify the delta ratio
  ≈4096 vs `Date.now()`) will show an LCS match with the page-generated fingerprint `p`
  because BOTH embed the same clock. Mint with a FIXED `p` across time: if the matched
  bytes advance with the clock, it's shared time, not an input echo — and the ticket
  oracle is instead a server-clocked identity-mint (attacker-chosen `p` accepted).

## Probe adjustment (ci-cd × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
