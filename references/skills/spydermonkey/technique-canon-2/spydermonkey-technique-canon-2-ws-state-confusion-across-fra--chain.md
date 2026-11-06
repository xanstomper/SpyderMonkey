# WS state confusion across frames — chain composition

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-ws-state-confusion-across-fra.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Session/identity state set in frame N trusted in frame N+1 (the SPY-048/069 family). Decisive test: mirror the app's packet types exactly (connect-ack vs data-gate — the engagement-ops recipe) and show frame-level state carry — mis-framing is YOUR bug, not a finding.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
