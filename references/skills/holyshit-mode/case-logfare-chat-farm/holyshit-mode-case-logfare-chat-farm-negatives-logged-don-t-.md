# Negatives (logged, don't re-probe)

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

- Tier-2 consent gate holds: glm-5/grok-4.6 → 403 `consent_required` (real server gate; mass-assigned tier/role/can_use_premium/consent fields accepted `{"ok":true}` but stripped — verify by GET-back + retry, not the 200).
- Cross-session conversation IDOR → 404; client-supplied `conversation_id` ignored; no shared global buffer (PTOK constant 7-36/fresh session, cross-user probe → NONE).
- Model-field path traversal → clean 502 upstream-404 passthrough (no SSRF via model routing).
- SvelteKit escapes stored conversation titles; settings theme not reflected into HTML.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
