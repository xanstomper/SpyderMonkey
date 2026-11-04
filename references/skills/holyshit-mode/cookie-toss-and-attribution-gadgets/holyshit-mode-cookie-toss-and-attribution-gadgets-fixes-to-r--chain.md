# Fixes to recommend — chain composition

- source canon: `holyshit-mode/cookie-toss-and-attribution-gadgets.md`
- base technique: `holyshit-mode-cookie-toss-and-attribution-gadgets-fixes-to-r.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Allowlist (not blocklist) writable params; refuse writes matching session-family prefixes;
signed/short-lived attribution tokens validated server-side at signup; treat identity cookies
as untrusted client input and re-verify server-side before risk decisions.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
