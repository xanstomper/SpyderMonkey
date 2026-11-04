# 2. user_metadata injection (limited value) — websocket / low-priv

- source canon: `holyshit-mode/web-llm-proxy-auth-bypasses.md`
- base technique: `holyshit-mode-web-llm-proxy-auth-bypasses-2-user-metadata-in.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **websocket** · auth **low-priv** · chain role **pivot**

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- Arbitrary `user_metadata` (role, is_admin, credits) PERSISTS into the JWT via signup/update.
- Backends authorize on their own DB (`profiles` / `app_metadata`), NOT client metadata →
  admin bypass fails. Expect `email_not_verified` middleware on all privileged routes.
- Don't burn turns re-testing metadata escalation against a well-built backend.

## Probe adjustment (websocket × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
