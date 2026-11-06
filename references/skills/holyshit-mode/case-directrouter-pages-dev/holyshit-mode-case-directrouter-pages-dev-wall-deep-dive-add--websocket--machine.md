# Wall — deep dive (added 2026-10-04 evening) — websocket / machine

- source canon: `holyshit-mode/case-directrouter-pages-dev.md`
- base technique: `holyshit-mode-case-directrouter-pages-dev-wall-deep-dive-add.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **machine** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

Discord OAuth session required for `/v1/chat/completions`, `/api/keys`, `/api/redeem`,
`/api/usage/stats`, `/api/auth/me`, `/api/admin/*`. Admin Bearer required for `/api/admin/*`.

## Probe adjustment (websocket × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
