# Backup extraction and root-detection gaps — chain composition

- source canon: `spydermonkey/technique-canon-3.md`
- base technique: `spydermonkey-technique-canon-3-backup-extraction-and-root-de.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

allowBackup=true and client-only root/jail checks. Decisive test: adb backup pull of your build; the bypass shim on your device — the class is the check's client-side placement.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
