# SvelteKit chunk walk (client-API call-site discovery) — api / low-priv

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-sveltekit-chunk-walk-cl.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- context: **api** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

`index.html` → `entry/start.<hash>.js` → `chunks/<hash>.js` → `nodes/<n>.<hash>.js`. The 358KB **node** chunk (not the tiny entry/app chunks) held ALL fetch call sites — including the correct `/api/conversations/${id}/messages` subresource that guessed paths missed (all wrong guesses 404'd). Don't guess subresource paths; read the framework's lazy-loaded page chunks.

## Probe adjustment (api × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
