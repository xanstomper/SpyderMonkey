# 7. Frame-capture integrity (evidence hygiene)

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-04

## The technique

- ALWAYS reassemble continuation frames: large events arrive as op=1 + op=0 fragments (~4KB each); naive per-frame saves split JSON mid-object and corrupt evidence files. Read each header, honor the `fin` bit, merge fin=0 payloads; skip pongs (op=10) instead of writing them as text junk.
- Sanitize control bytes (`[\x00-\x08\x0b\x0c\x0e-\x1f]`) before json-parsing saved captures, and parse arrays with `json.JSONDecoder().raw_decode` rather than regexing field ORDER (field order varies between event types).
- Re-run a second capture and confirm stable IDs/values before calling a leaked field real — a finding that does not reproduce across captures is a parse artifact.
- The masking may exist on SOME feed paths and not others (leaderboard masked, game-detail/crash rows unmasked-with-flag) — audit every path independently.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
