# Context — chain composition

- source canon: `holyshit-mode/case-logfare-ai-retest2.md`
- base technique: `holyshit-mode-case-logfare-ai-retest2-context.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Second engagement of logfare.ai (baseline 2026-10-03: CORS arbitrary-origin + credentials
CVSS ~9.1, broken rate limiting, FastAPI openapi.json exposure). Target rebuilt since
baseline: SPA → server-rendered FastAPI (inline `<script>` blocks, no hashed JS bundle),
plus a NEW OAuth-provider surface (`/oauth/authorize`, `/v1/me/apps`, device flow).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
