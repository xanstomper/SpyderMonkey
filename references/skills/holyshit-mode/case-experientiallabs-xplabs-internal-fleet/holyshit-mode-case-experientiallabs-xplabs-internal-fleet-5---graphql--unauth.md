# 5. Hardened-surface contrast (what was NOT vulnerable, honestly) — graphql / unauth

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- base technique: `holyshit-mode-case-experientiallabs-xplabs-internal-fleet-5-.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **graphql** · auth **unauth** · chain role **pivot**

## Context

- platform: aliases and batched queries bypass field-level checks; type confusion lives in the schema
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Web root: `/auth/create-account`, `/auth/otp`, `/auth/password/signin`, `/auth/resend-verification`
  all Turnstile-captcha-gated (`captcha_failed` 403 fires BEFORE body parsing → mass-assignment
  not testable pre-captcha). `/auth/spend-unlock` session-gated (`no_session`). All `/api/*`
  (keys, mfa, credits-overflow, rewards, onboarding, admin/access) → 401 keyless.
- Public gateway: all `/v1/*` inference 401; `/api/models` + `/api/v1/endpoints/zdr` intentionally
  public (recon, not vuln).
- **Key discriminator:** `gateway.xplabs.ai`'s GLM/Qwen lanes WERE correctly keyed
  (`/glm/v1/models` → 401 `Invalid API Key`) while `wm.xplabs.ai` was left OPEN — the compromise
  is a **deployment misconfiguration / single-host exposure**, not a platform-wide design flaw.
  State that contrast; one auth-gate fix on the open host kills most findings.

## Probe adjustment (graphql × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
