# 5. Hardened-surface contrast (what was NOT vulnerable, honestly)

- source canon: `holyshit-mode/case-experientiallabs-xplabs-internal-fleet.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
