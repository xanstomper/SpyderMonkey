# NTLM relay classes (documented mechanisms) — chain composition

- source canon: `spydermonkey/technique-canon-6.md`
- base technique: `spydermonkey-technique-canon-6-ntlm-relay-classes-documented.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

SMB signing absent / channel-binding gaps — the CONFIG posture (signing required?) is the read-only finding; the relay is never executed. Decisive test: SMB negotiation flags — the flag absence is the class.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
