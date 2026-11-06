# Phase 6: Brute-Force Execution — chain composition

- source canon: `holyshit-mode/recon-technique-multi-host-brute.md`
- base technique: `holyshit-mode-recon-technique-multi-host-brute-phase-6-brute.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Chain roles

- final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `x-export-password` brute-forced with trivial wordlist — password `madsys` matched on 7th attempt
- Same password worked on `x-refresh-password` — credential reuse confirmed
- Password is the Harvard MaDSys Lab team name — trivially guessable by anyone reading the status page or docs footer
- 20 rapid wrong-password probes returned zero 429s across both endpoints

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
