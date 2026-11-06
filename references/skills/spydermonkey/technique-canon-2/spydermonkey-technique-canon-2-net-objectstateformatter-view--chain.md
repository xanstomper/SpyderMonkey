# .NET ObjectStateFormatter / ViewState — chain composition

- source canon: `spydermonkey/technique-canon-2.md`
- base technique: `spydermonkey-technique-canon-2-net-objectstateformatter-view.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

MAC-enabled vs legacy ViewState — the `__VIEWSTATE` parameter with tamper acceptance is the class. Decisive test: modified viewstate → distinct MAC error vs acceptance (acceptance = crown; never execute the gadget).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
