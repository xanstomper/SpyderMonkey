# 5.3 Client-only gates + ID backdoors (score 80) — chain composition

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- base technique: `3am-shinjitsu-arsenal-05-client-side-5-3-client-only-gates-i.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- GREP every chunk: `user.id === <numeric literal>`, `is_admin`, `switchTab`, `can_*`,
  `window.hide*Gate` — dev backdoors bypassing UI role checks.
- Cross-file consistency law: map EVERY module's check independently — the backdoor may grant
  provider admin in one chunk while giveaway creation stays blocked in another. The
  inconsistency IS the true attack surface.
- EXPLOITABILITY GATE: does the backing API ALSO trust the client flag, or does the endpoint
  independently validate? Client-only bypass without API validation = needs-API-confirmation.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
