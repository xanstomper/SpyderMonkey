# Session-ID attacker-chosen acceptance (score 50, confirmed) — chain composition

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-session-id-attacker-cho.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Server accepts ANY client-supplied `lfc_session` uuid **verbatim** — no entropy check, no re-mint: send `Cookie: lfc_session=11111111-2222-4333-8444-555566667777` and the server persists it via Set-Cookie, then creates conversations + settings on the chosen id. Cookie-fixation class; brute is closed (uuid v4, 122-bit) but issuance has zero integrity. Weaponization needs an injection vector or parent-domain cookie-toss (sibling subdomain setting cookies for `.logfare.ai`) — subdomain sweep is the open follow-up.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
