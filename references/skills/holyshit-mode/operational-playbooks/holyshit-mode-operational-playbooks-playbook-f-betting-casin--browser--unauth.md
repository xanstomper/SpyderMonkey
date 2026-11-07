# PLAYBOOK F — BETTING / CASINO / GAMBLING — browser / unauth

- source canon: `holyshit-mode/operational-playbooks.md`
- base technique: `holyshit-mode-operational-playbooks-playbook-f-betting-casin.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **browser** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

**Objective**: game-integrity (provably fair), money-RPC authorization, and the
forgotten regional/mirror infrastructure these operators always accumulate.

**Phase 1 — Surface & Mirror Recon**
- CT logs on `%.<brand>.tld` AND partner/white-label brands (shared backends leak
  into each other's bundles — `providers/<partner>-originals` in the JS is the tell).
- Regional entrance/mirror domains (e.g. Turkish `giris`/`tr.` hosts) sit on separate
  legacy hosting — fingerprint SEPARATELY; they never inherit main-site hardening.
- PTR-reverse every infrastructure IP, then whois every name in the funnel (links,
  PTRs, robots): unregistered-but-linked = registration takeover, executable same-day.
- Parked-domain landers (`ap:"parking"` script) on mirror domains = dead funnel links.

**Phase 2 — Provably-Fair Structural Test (the integrity crown)**
- Capture a FULL game round from the UNAUTH socket: `game_starting` → `game_started`
  → `player_bet`/`game_tick` → `game_crash`.
- Verify commitment PLACEMENT: a fairness commitment must precede the outcome on a
  publicly-checkable channel. Hash delivered in the SAME event as the result = no
  verifiable pre-commitment = the marketing claim is unfalsifiable (integrity finding
  that supports extortion narratives — capture it before the attackers publish theirs).
- Check for staff-control flags in public event schemas (`forced`, manual-settle) —
  outcome-control capability confirmed in the wire schema is a regulator-grade question.
- Mixed-game asymmetry matters: client-seed PF on dice-class games vs no visible
  commitment on crash-class games is the common real pattern.

**Phase 3 — Money-RPC Authorization**
- Extract the client's shared schema library (io-ts/zod chunk) for every money RPC's
  exact shape — then fire valid-shaped unauth probes and read the GATE ORDER
  (validation → auth → balance is the secure order; explicit "Not logged in" beats
  silent session-fail for reporting).
- **Wallet-claim trust model**: if the RPC carries a client-supplied wallet object,
  reason from its structure — no cross-user identifier (walletId/ownerId) in the shape
  = cross-wallet theft structurally impossible, worst case is self-inflation. Then
  weigh: `*_requested` field naming (server treats client figure as advisory),
  optional fee fields (server computes), attached anti-fraud session tokens, and
  economic self-detection (minting bugs scream in ledger reconciliation). Deliver a
  reasoned confidence % + the residual edges (unit conversion, wallet_type override,
  float-vs-integer refinement asymmetries) when a live session isn't available.

**Phase 4 — The Forgotten Edges (where these breaches actually come from)**
- Aged machine/service accounts, never-rotated credentials, staging hosts, dead-name
  identities — the attacker group narrative + the founder's incident statement usually
  corroborate the access method even while disputing scale. Cross-check them.
- Vendor paths in mail (SPF includes, PTR-named mail servers), support-tool data
  channels (identity-verification HMAC fields on user objects), custody integrations.
- Default-credential decisive test on ANY internet-exposed database the engagement
  owns (3-4 read-only attempts, stop at denial — the posture finding stands either way).

**Deliverable**: integrity-commitment map, money-RPC gate-order matrix, mirror/edge
infrastructure assessment, dead-name takeover list, prioritized firewall/patch list.

---

## Probe adjustment (browser × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
