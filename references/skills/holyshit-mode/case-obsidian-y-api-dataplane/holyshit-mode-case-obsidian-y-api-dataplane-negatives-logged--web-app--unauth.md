# Negatives (logged as coverage) — web-app / unauth

- source canon: `holyshit-mode/case-obsidian-y-api-dataplane.md`
- base technique: `holyshit-mode-case-obsidian-y-api-dataplane-negatives-logged.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **web-app** · auth **unauth** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

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

## Probe adjustment (web-app × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
