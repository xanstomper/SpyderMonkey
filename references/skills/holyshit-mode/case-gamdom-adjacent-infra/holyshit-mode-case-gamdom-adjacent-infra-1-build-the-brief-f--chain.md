# 1. Build the brief from breach-OSINT — chain composition

- source canon: `holyshit-mode/case-gamdom-adjacent-infra.md`
- base technique: `holyshit-mode-case-gamdom-adjacent-infra-1-build-the-brief-f.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Search: `<target> breach leak <year>` — hit Breachsense, ransomware.live, and 2-3 news writeups.
- Record from the attacker's leak-site statement: claimed initial access, claimed data
  holdings, escalation promises. This is the engagement brief — the attacker documents
  their own kill-chain.
- Corroborate against the victim's public statements. The mechanism is confirmed when the
  victim's own PR admits it ("unauthorized withdrawal requests were added to the database"
  = proven DB-level WRITE). Disputed scale ≠ disputed method.
- The two datasets (attacker holdings vs victim confirmations) define what remains open.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
