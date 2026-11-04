# 5.6 Dependency rot / dead references (score 75) — chain composition

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- base technique: `3am-shinjitsu-arsenal-05-client-side-5-6-dependency-rot-dead.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- Third-party scripts, invites, widgets, CDN links in the bundle → 404/NXDOMAIN = hijackable
  reference (registration-takeover the domain → code execution in context).
- DECISIVE: extract every external URL from all chunks → resolve each → dead ones scored by
  what the page does with the loaded content.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
