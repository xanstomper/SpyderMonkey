# MASTG Data in Clipboard and Keyboard Cache (MASTG-STORAGE-04) — chain composition

- source canon: `spydermonkey/mobile-canon.md`
- base technique: `spydermonkey-mobile-canon-mastg-data-in-clipboard-and-keyboa.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- class: clipboard sync + keyboard autocorrect retaining secrets
- probe: paste a marker, inspect the keyboard cache db
- wall: lab only

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
