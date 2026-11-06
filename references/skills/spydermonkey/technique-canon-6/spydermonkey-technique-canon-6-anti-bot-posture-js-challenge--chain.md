# Anti-bot posture (JS challenges, managed challenge) — chain composition

- source canon: `spydermonkey/technique-canon-6.md`
- base technique: `spydermonkey-technique-canon-6-anti-bot-posture-js-challenge.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Which lanes get challenged (curl/requests vs headless vs real browser) — the differential map is the recon crown (drives all lane strategy). Decisive test: same endpoint three clients — the treatment matrix.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
