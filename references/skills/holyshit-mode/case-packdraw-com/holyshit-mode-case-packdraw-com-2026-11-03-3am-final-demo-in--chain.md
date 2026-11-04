# 2026-11-03 3AM final: demo inert, PF hypothesis upgraded, T2 stands — chain composition

- source canon: `holyshit-mode/case-packdraw-com.md`
- base technique: `holyshit-mode-case-packdraw-com-2026-11-03-3am-final-demo-in.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Demo mode: verified INERT for guests (4 click sequences incl post-Continue, DOM dumps,
  zero network) — no unauth seed-observation path exists.
- PF algorithm verbatim (from their fairness page): `ticket = (BigInt('0x'+sha512(
  clientSeed+':'+serverSeed+':'+nonce)) % 1_000_000) + 1`; jackpot = `sha256(eosBlockHash)
  % totalTickets + 1` with contiguous ticket ranges. Their text: nonce is needed "when
  server seeds and client seeds remain unchanged, as is the case when opening multiple
  packs in a single purchase"; the hashed server seed is shown in the account PROFILE
  before purchase and the unhashed seed exposed after. Account-level seed commitment +
  nonce-machinery = fixed-seed architecture hypothesis (58-70 if 2-open test confirms
  non-rotation across purchases). Full verify recipe documented in the ledger class.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
