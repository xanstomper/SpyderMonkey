# Provably-fair scheme (from their fairness page — the key attack surface) — chain composition

- source canon: `holyshit-mode/case-packdraw-com.md`
- base technique: `holyshit-mode-case-packdraw-com-provably-fair-scheme-from-th.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
