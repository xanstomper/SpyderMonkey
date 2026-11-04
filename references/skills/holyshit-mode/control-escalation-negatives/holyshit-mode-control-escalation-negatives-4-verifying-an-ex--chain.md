# 4. Verifying an exposed archive before declaring a DB leak — chain composition

- source canon: `holyshit-mode/control-escalation-negatives.md`
- base technique: `holyshit-mode-control-escalation-negatives-4-verifying-an-ex.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Download a candidate backup with a Range header first (`Range: bytes=0-200`), check the magic
(`PK` = zip), then pull full bytes and list `zipfile.namelist()` + `getinfo().file_size`. A `.zip`
whose members are all `.jpg`/media is a photo archive, not a credentials dump. Don't report "DB
backup exposed" from the filename alone.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
