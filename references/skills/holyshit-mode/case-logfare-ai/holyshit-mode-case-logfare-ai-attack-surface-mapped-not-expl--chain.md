# Attack Surface Mapped (Not Exploited) — chain composition

- source canon: `holyshit-mode/case-logfare-ai.md`
- base technique: `holyshit-mode-case-logfare-ai-attack-surface-mapped-not-expl.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **IDOR on DSAR:** `/v1/me/data`, `/v1/me/delete` — need valid session
- **SSO confusion:** Race condition on `/v1/sso/approve` + `/v1/sso/token` — need valid session
- **Post-auth injection:** Stored XSS, CSRF — need valid session
- **Rate limit bypass:** `X-Forwarded-For` spoofing — not tested
- **Premium model access:** Tier 1 models require auth — no bypass found

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
