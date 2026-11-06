# HOLY SHIT #2 — Shared global conversation context / cross-user disclosure (score 85) — chain composition

- source canon: `holyshit-mode/case-obsidian-y-api.md`
- base technique: `holyshit-mode-case-obsidian-y-api-holy-shit-2-shared-global-.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `prompt_tokens` DRIFTED on identical input across requests (21k → 30k → 50k) → context is server-side state, not static per-request injection. **PTOK drift on identical input = shared-context oracle.**
- No cookies/sessions at all, yet the model recalled ALL prior turns from earlier separate curls → global buffer keyed on nothing.
- Foreign users' roleplay content (character personas never sent by us) appeared in context. Anyone can read out other users' conversations via a summarization oracle and poison the shared context for everyone.
- The model itself CONFIRMED the history ("Turns 1–8...") when asked — the disclosure oracle is one prompt away for any user.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
