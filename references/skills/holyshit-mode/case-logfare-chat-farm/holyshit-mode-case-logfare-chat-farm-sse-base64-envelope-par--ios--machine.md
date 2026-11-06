# SSE base64 envelope parsing — ios / machine

- source canon: `holyshit-mode/case-logfare-chat-farm.md`
- base technique: `holyshit-mode-case-logfare-chat-farm-sse-base64-envelope-par.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **ios** · auth **machine** · chain role **pivot**

## Context

- platform: the check often lives client-side — runtime inspection, MASTG/MASVS methodology
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Chat streams `data: <base64(json)>`. Decode with padding fix:
```python
b = line[6:].strip(); d = json.loads(base64.b64decode(b + '='*(-len(b)%4)))
```
- First chunk carries `usage` with prompt_tokens (empty completion_tokens); final `logfare_complete:true` chunk has totals.
- Parse ALL chunks, not just the last line — file tail can have corruption; use `errors='replace'`.
- `X-Conversation-Id` / `X-Message-Id` response headers; `/api/conversations` lists session history.

## Probe adjustment (ios × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
