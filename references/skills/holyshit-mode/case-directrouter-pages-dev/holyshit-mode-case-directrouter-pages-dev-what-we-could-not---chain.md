# What we could NOT test (operator credential required) — chain composition

- source canon: `holyshit-mode/case-directrouter-pages-dev.md`
- base technique: `holyshit-mode-case-directrouter-pages-dev-what-we-could-not-.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. **Discord session** → test `/api/keys` IDOR (can user A revoke user B's keys?),
   `/v1/chat/completions` plan-tier tampering (does a free user get Frontier models?),
   `/api/redeem` code abuse (brute-force short codes, replay redemption),
   `/api/auth/membership` bypass (already Discord-gated; confirm the gate is server-side,
   not client-side only).
2. **Admin Bearer** → test `/api/admin/*` full surface: `/api/admin/users` PATCH privilege
   escalation, `/api/admin/grants` IDOR, `/api/admin/custom-keys` PATCH mass-assignment
   (top-up balance via crafted body), `/api/admin/routes` router poisoning.

The agent offered to bootstrap a Discord account via mail.tm disposable email + Playwright
automation. The operator declined ("no u dont"). This is the correct outcome — the
doctrine explicitly forbids credential self-bootstrapping. Engagement closed at the wall
with the 3 pre-auth findings as the publishable result. The HIGH-severity PII dump alone
is a defensible engagement deliverable without the post-auth kill chain.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
