# Other carriers — chain composition

- source canon: `spydermonkey/stego-canon.md`
- base technique: `spydermonkey-stego-canon-other-carriers.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

| Probe | Test | Confirmed-when |
|---|---|---|
| Polyglot | `file` + `binwalk` (own artifact) | two formats valid |
| Video frames | `ffmpeg` frame extraction → zsteg per frame (own) | frame-embedded data |
| PDF layers | `qpdf --show-objects` (own pdf) | hidden layers/attachments |
| Office content | `olevba`/`oleid` + `unzip -l` (own doc) | embedded objects |
| Trailing bytes | `xxd` tail + `strings` tail (own file) | appended payload |
| Cover vs stego | same-image diff (own pair) | byte drift located |

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
