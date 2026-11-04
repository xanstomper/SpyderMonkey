# Negatives (logged as coverage)

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

- 47-path secret/source-map/env/backup/admin-panel sweep: all 404/403. Playground + docs HTML
  contain ONLY `YOUR_API_KEY` placeholder; no hardcoded secrets, no admin panel exists
  (`/admin, /panel, /dashboard, /console, /internal` all 404).
- `/v1/chat/completions` uniform `invalid_api_key` 401 for ALL JWT/Bearer/alg-none/Basic/key-prefix
  variants — no JWT auth path, no key-format oracle, no SQL/NoSQL/SSTI/XXE/command-injection/
  path-traversal/SSRF on key or model fields.
- Private Anthropic fleet (`claude-opus-4-8` etc.) stays 403 `no_access`; 21+ gate-bypass variants
  blocked. `kallme/`, `muse/` prefix aliases not routable (404) — gate keys on exact `anthropic/`.
- No shared/cross-user data read in this pass (proxy requests stateless; `user`/`session_id`
  fields accepted but ignored).
- Upstream provider endpoints (`gonka-api.org` = Lovable 403; `router.kiosapi.com` = unreachable)
  not directly attackable without the operator's upstream credentials.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
