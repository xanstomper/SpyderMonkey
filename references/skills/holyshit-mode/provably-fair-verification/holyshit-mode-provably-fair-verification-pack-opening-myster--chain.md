# Pack-opening / mystery-box class: the fixed-seed documentation tell — chain composition

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-pack-opening-myster.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

For case-opener / pack sites, the operator's OWN fairness page is the spec AND the
first exploit lead. Mine it for the VERBATIM algorithm (they publish it: ticket =
`(int(sha512(f"{clientSeed}:{serverSeed}:{nonce}"), 16) % 1_000_000) + 1`) and for
mechanic wording that reveals the seed-rotation policy:

- A nonce described as "auto-incrementing… to provide a unique random result when
  server seeds and client seeds remain unchanged, as is the case when opening multiple
  packs in a single purchase" = seeds do NOT rotate — the nonce exists because the
  seed is stable. Combined with an account-level commitment ("our server seed hash
  before purchase, found in your account profile. After your purchase, we expose the
  unhashed server seed"), the architecture is fixed-seed-per-account: after ONE reveal,
  every future ticket is computable before paying (player controls clientSeed and the
  nonce increments) → open only tickets whose public range EV > price = guaranteed-win
  grind against the house. That wording is the finding's first half — it upgrades the
  hypothesis before any account exists.
- **Minimum decisive test (2 opens, cheapest packs, operator account):** record the
  profile server-seed hash BEFORE purchase 1 (H0), then revealed seed S1 + client seed
  + nonce after open 1; hash check `sha512(S1) == H0` (commitment discipline); record
  profile hash H1 before purchase 2 and revealed S2. `S2 == S1` = CONFIRMED
  predictable-outcome grind (build the verifier from their published function and the
  public per-item ticket ranges — grid the +EV nonces). `S2 != S1` = rotating, clean.
  Ship this as a ready-to-run verify script (`ticket` / `commit-check` / `grind` CLIs).
- The DEMO button on such sites is usually inert for guests (multiple click
  sequences, zero state change, zero network) — do not burn rounds on it; the account
  test is the gate. If it does call a server action, running it unauth is the free
  version of the same test.
- **House edge is computable unauth** from the public odds table: EV = Σ(pct × price)
  vs pack price (a 13% edge was confirmed on one target; "odds tightened after update"
  complaints corroborate the direction). Quantify it — it is both a finding and the
  EV baseline that the grind exploit flips.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
