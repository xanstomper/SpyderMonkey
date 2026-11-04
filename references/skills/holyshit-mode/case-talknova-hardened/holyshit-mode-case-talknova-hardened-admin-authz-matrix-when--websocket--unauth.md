# Admin authz matrix (when admin endpoints are discovered) — websocket / unauth

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-admin-authz-matrix-when.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **websocket** · auth **unauth** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- GET unauth → expect 401
- POST unauth → expect 401
- PATCH/DELETE unauth → expect 401
- IDOR by numeric ID (`/users/1`, `/grants/1`, `/custom-keys/1`) → expect 401
- Mass assignment probe (`{"plan":"max","is_admin":true}`) → expect 401 or validation error
- Rate-limit probe on login → note decay time (talknova: 30 min)

## Probe adjustment (websocket × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
