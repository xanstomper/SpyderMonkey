# Technique: auth-mode header split discovery — chain composition

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-technique-auth-mode-header-s.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Multi-tenant SPA bundles carry an auth-mode selector header (`X-Chat-Auth-Mode: account|platform_key`). The error chain enumerates itself: endpoint bare → 400 naming the header → each value names the next required credential. Each branch validates DIFFERENT credentials against DIFFERENT backends — treat each branch as its own auth surface.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
