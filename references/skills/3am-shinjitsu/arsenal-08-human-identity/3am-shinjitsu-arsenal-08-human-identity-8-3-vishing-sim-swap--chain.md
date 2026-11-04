# 8.3 Vishing/sim-swap/MFA-fatigue EXPOSURE ratings (score 55, never executed) — chain composition

- source canon: `3am-shinjitsu/arsenal-08-human-identity.md`
- base technique: `3am-shinjitsu-arsenal-08-human-identity-8-3-vishing-sim-swap.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Rated from artifacts only: which MFA method, whether office refs are public, SIM-portal
  exposure of the org (carrier domain in email headers is documentation, not targeting).
- MITRE anchors for the report: T1598/T1566/T1621/T1656 noted as EXPOSURE, not attempts.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
