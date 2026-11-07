# 6. Phone autoconfirm = instant full sessions (score 80, CORRECTION of old negative) — kubernetes / high-priv

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-reengagement-6-phone-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **kubernetes** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

POST /auth/v1/signup {phone:+1XXXXXXXXXX, password} → returns FULL session (access_token+refresh_token, phone_confirmed_at set) with NO SMS. Earlier case log said "SMS OTP dead" — that was OTP *verify*; phone *signup autoconfirm* is a different, working path. Old case negatives must be re-read narrowly.
- user_metadata admin injection (role:admin, is_admin, credits:999999, tier:enterprise) PERSISTS into JWT user_metadata — but backend authorizes on its own DB, NOT user_metadata → **admin bypass is a dead end** (backend gate = `profiles.email_verified` middleware on all /api/account/*).
- Email delivery fully broken server-side: signup confirm, email-change, recover all silently dropped (verified via working Mailinator API — test inbox had mail, Gratisfy inboxes empty). Email-verify gate = unsatisfiable by the user themselves.

## Probe adjustment (kubernetes × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
