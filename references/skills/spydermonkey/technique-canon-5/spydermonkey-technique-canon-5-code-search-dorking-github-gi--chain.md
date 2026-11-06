# Code-search dorking (github/gitlab/gist) — chain composition

- source canon: `spydermonkey/technique-canon-5.md`
- base technique: `spydermonkey-technique-canon-5-code-search-dorking-github-gi.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Org-attribution via user-id chains (the SPY-067 class family), deleted-file recovery, committed secrets in value="" attributes, committed CSVs as QA telemetry. Decisive test: the recovered artifact itself (file/blob path) — the artifact is the evidence.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
