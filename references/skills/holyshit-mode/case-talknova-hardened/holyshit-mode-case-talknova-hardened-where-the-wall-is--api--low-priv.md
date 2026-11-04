# Where the wall is — api / low-priv

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-where-the-wall-is.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **api** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Everything interesting sits behind:
1. **Google session** — /api/chat plan-tier tampering, /api/usage IDOR, /api/apikey authz (can user A read user B's key?)
2. **Admin session** — admin API depth, session fixation, CSRF on state-changing admin POSTs, privilege escalation via mass assignment on /api/admin/users/:id

Pre-auth surface exhausted. The next decisive test REQUIRES credentials.

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
