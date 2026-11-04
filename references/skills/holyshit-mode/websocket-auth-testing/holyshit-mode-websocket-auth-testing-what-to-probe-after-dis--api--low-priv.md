# What to Probe After Discovering the Auth Pattern — api / low-priv

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-what-to-probe-after-dis.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **api** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

| Vector | Test |
|--------|------|
| Token reuse across users | Get token as user A, use on user B's resources |
| Token replay | Use the same token twice |
| Token expiry | Wait 5/30/60 min, retry |
| Token forgery | Guess the structure (UUID? JWT? random?) |
| Session-cookie substitute | Send session cookie in upgrade headers, skip token frame |
| Mass assignment on token source | POST `/api/.../session` with `{"unlimited":true,"isAdmin":true}` |
| Origin bypass | Strip Origin header from upgrade request |
| First-frame type confusion | Send `{"type":"ready"}` instead of `{"type":"authenticate",...}` |

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
