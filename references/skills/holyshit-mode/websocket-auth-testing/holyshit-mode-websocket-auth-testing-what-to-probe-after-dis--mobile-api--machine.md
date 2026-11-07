# What to Probe After Discovering the Auth Pattern — mobile-api / machine

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-what-to-probe-after-dis.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **mobile-api** · auth **machine** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the mobile client IS another api principal — same routes, different trust assumptions
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

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

## Probe adjustment (mobile-api × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
