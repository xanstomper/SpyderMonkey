# 7. Frame-capture integrity (evidence hygiene) — chain composition

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-7-frame-capture-inte.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- ALWAYS reassemble continuation frames: large events arrive as op=1 + op=0 fragments (~4KB each); naive per-frame saves split JSON mid-object and corrupt evidence files. Read each header, honor the `fin` bit, merge fin=0 payloads; skip pongs (op=10) instead of writing them as text junk.
- Sanitize control bytes (`[\x00-\x08\x0b\x0c\x0e-\x1f]`) before json-parsing saved captures, and parse arrays with `json.JSONDecoder().raw_decode` rather than regexing field ORDER (field order varies between event types).
- Re-run a second capture and confirm stable IDs/values before calling a leaked field real — a finding that does not reproduce across captures is a parse artifact.
- The masking may exist on SOME feed paths and not others (leaderboard masked, game-detail/crash rows unmasked-with-flag) — audit every path independently.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
