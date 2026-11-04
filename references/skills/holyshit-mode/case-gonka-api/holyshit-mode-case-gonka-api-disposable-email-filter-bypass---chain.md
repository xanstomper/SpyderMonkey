# Disposable-email filter bypass (discovery recipe) — chain composition

- source canon: `holyshit-mode/case-gonka-api.md`
- base technique: `holyshit-mode-case-gonka-api-disposable-email-filter-bypass-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Signup enforces a 23514 CHECK constraint on email domain.
- Blocked: tempmail, guerrillamail, yopmail, 10minutemail, maildrop, getnada,
  dispostable, fakeinbox, trashmail, sharklasers, grr.la.
- MISSED (200): harakirimail.com, pokemail.net, spam4.me, bccto.me, chammy.info.
- Discovery: batch-signup one probe account per candidate domain, read
  200 vs 23514. A filter-list gap = automate account creation at scale.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
