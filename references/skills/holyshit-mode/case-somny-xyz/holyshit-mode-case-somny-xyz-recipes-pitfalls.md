# Recipes / pitfalls

- source canon: `holyshit-mode/case-somny-xyz.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

- **Key-masking pattern:** key-create endpoints return masked keys; a `reveal`/`secret` sub-endpoint is the real primitive (same as gratisfy's `platform-keys/{id}/secret`). IDOR on reveal with foreign UUID → 400 body-validation (auth before existence).
- **mail.tm flow:** GET `/domains` (find active domain) → POST `/accounts` → POST `/token` → poll `/messages` (5s) → GET `/messages/{id}` for full body → regex `token=([a-zA-Z0-9._-]+)&callbackURL`. Consume ONCE via GET with no-redirect opener; capture 302 Location.
- **Verification token may be JWT-style (167 chars), not hex** — regex must allow dots: `[a-zA-Z0-9._-]+`.
- **Terminal `&` guard:** shell loops with `&` backgrounding rejected by terminal tool — serialize.
- **delete-user 404:** better-auth endpoint present in client bundle but plugin not enabled server-side — bundle lists endpoints the server doesn't have; always live-probe.
- Hygiene: revoked probe key via `DELETE /api/keys/{id}` (worked).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
