# Re-verified — chain composition

- source canon: `holyshit-mode/case-logfare-reengagement2.md`
- base technique: `holyshit-mode-case-logfare-reengagement2-re-verified.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- **CORS arbitrary-origin + credentials reflection** (score 72) on every endpoint including
  state-changers (`/v1/auth/regenerate-key`, `/v1/me/delete`). BUT: auth is now cookie-based and
  observed cookies ship `SameSite=Lax; HttpOnly; Secure` + path scoping → cross-site POSTs don't
  carry the session. **Exploitability downgraded 9.1 → ~7.1.** Lesson: the SAME finding changes
  severity when the auth model changes — re-rate exploitability, not just presence, on re-engage.
- `/openapi.json` full exposure (60+ routes, no security schemes).

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
