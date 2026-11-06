# Leak claims: row-level correlation or it isn't a finding — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-leak-claims-row-level-correlatio.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Counting `"display_username"` fields does NOT prove a masking failure — a feed full of
visible users also contains that field. The decisive test: find rows where the masked
field (`username == "Hidden user"`) appears, then check the SAME row's `display_username`
for a real value. Report `masked occurrences → correlated rows → unique userIds`. Only the
correlated count is the leak; the rest is noise. Same discipline as the 3-gate: a diff
needs the baseline and the attack joined on the same object.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
