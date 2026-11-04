# Gate analysis (the critical lesson) — api / low-priv

- source canon: `holyshit-mode/supabase-gotrue-playbook.md`
- base technique: `holyshit-mode-supabase-gotrue-playbook-gate-analysis-the-cri.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **api** · auth **low-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

A "verification required" (e.g. `email_not_verified`, `turnstile_required`) error on one endpoint is NOT a global gate. Fuzz sibling endpoints with the same session before concluding:
- `/api/account/*` may demand email verification while `/api/media/*` on the chat subdomain accepts the same unverified session.
- Text chat gated by server-side Turnstile ≠ media endpoints gated. Media (speech/images/transcriptions) often runs wide open.

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
