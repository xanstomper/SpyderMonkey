# Zero server-side CSRF enforcement (score 45, hypothesis for browser-exploit) — mobile-api / machine

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-zero-server-side-csrf-e.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **mobile-api** · auth **machine** · chain role **final**

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

`PUT /api/settings` returns 200 with `Origin: evil.com` AND no Origin. Only SameSite=Lax blocks browser exploitation — one flag from drive-by config hijack. Server does no verification.

## Probe adjustment (mobile-api × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
