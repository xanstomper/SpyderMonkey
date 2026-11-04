# Provably-fair scheme (from their fairness page — the key attack surface) — ios / low-priv

- source canon: `holyshit-mode/case-packdraw-com.md`
- base technique: `holyshit-mode-case-packdraw-com-provably-fair-scheme-from-th.md`
- bindings: **MASTG-RES** · **CWE-494** · **ATT&CK T1601**
- context: **ios** · auth **low-priv** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Packs/deals: `ticket = normalize(hash(clientSeed + serverSeed + nonce))` in 1..1M;
  item by ticket range (ranges visible in pack details). Server seed committed as hash
  pre-open, revealed unhashed AFTER the game.
- Battles: entropy = `sha256(future EOS block hash)` (mined after entries close);
  jackpot = `sha256(eosBlockHash)` modular raffle over ticket ranges; card-flip:
  `nonce = roundIndex*lineCount + lineIndex`, win if ticket <= survivalProb*1M.
- **THE OPEN QUESTION (WhiteArmor-grade if wrong): server-seed rotation policy.**
  Per-open rotation = standard safe. Per-account FIXED seed revealed after every open =
  after ONE open the user knows the seed and can compute future tickets BEFORE paying
  (controls clientSeed + nonce) → open only when the ticket lands on value > pack price
  → guaranteed-profit drain. Demo mode exists without account but the modal flow did not
  complete in testing (needs the mode-confirm step click-timing). Decisive test: 2 opens
  (one account, ~$11) or a working demo run — compare revealed seeds + pre-open hashes.

## Probe adjustment (ios × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
