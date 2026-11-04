# 10. Email delivery FIXED server-side + `/auth/v1/user` email bind (score 92, TOP FINDING) — iot / high-priv

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-reengagement.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-reengagement-10-email.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **iot** · auth **high-priv** · chain role **pivot**

## Context

- platform: radio/serial surface — BLE/NFC/UART classes, lab hardware only
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

The session-3 "email delivery fully broken" negative is DEAD — "Confirm Email Change" from hello@verify.gratisfy.xyz lands in Mailinator in ~25s (second time this target invalidated a stored negative; re-test email paths before citing them as walls).
Full chain, ~90s total, zero payment:
1. `POST /auth/v1/signup {phone, password}` → full session (autoconfirm).
2. `PUT /auth/v1/user {"email": <mailinator>}` with Bearer AT → binds email. Root-level `email_verified` via PUT is REJECTED (Supabase /user only writes user_metadata) — the verify-email flow is the only way to flip the flag.
3. `POST /auth/v1/resend {"type":"signup","email":...}` → 200; email arrives at Mailinator.
4. Extract token from link: `GET /auth/v1/verify?token=...&type=email_change` → 303 with access_token fragment = confirmed.
5. Handoff to platform (code→JWT as before), then:
   - `POST /api/account/platform-keys {"name":"x"}` → 201, **plaintext key in the response body** (`key.plaintext`, format `gxyz-<long digits>`).
   - `POST /api/account/platform-keys/{id}/secret` → re-reveals full key anytime (`apiKey` field).
   - Param is `name` NOT `label` (400 `missing_key_name`).
6. Key authenticates `https://api.gratisfy.xyz/v1/*` — the real OpenAI-compat gateway (nginx 404 elsewhere on that host).

## Probe adjustment (iot × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
