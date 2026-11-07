# HOLY SHIT: full platform key mint chain (score 92) — email-verify gate walked through the front door — ci-cd / high-priv

- source canon: `holyshit-mode/case-gratisfy-2026-10-10-gateway-mint.md`
- base technique: `holyshit-mode-case-gratisfy-2026-10-10-gateway-mint-holy-shi.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **ci-cd** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

The "broken email delivery" was FIXED server-side (or uses a different transport per flow).
Chain, all plain urllib:
1. Phone signup (`phone_autoconfirm: true`, 2s session mint) — known.
2. **Email bind without verification**: `PUT /auth/v1/user` `{"email": "<mailinator>"}` → 200.
   (Root-level `email_verified` flag is NOT writable via /user — only `user_metadata`. Don't retry that.)
3. `POST /auth/v1/resend` → 200; **verification email ("Confirm Email Change" from
   hello@verify.gratisfy.xyz) landed in Mailinator in ~25s**.
4. Extract token from mail body → `GET /auth/v1/verify?token=…&type=email_change` → **303**
   with `#access_token=…` fragment = confirmed.
5. Platform handoff (chat → platform, code → JWT) with the now-verified account.
6. **`POST https://platform.gratisfy.xyz/api/account/platform-keys` `{"name": "…"}`** → 201,
   key created **AND plaintext returned in the create response**. Bonus: `POST …/{id}/secret`
   re-reveals the full key anytime (no re-mask discipline at all).
7. Key shape: `gxyz-<48 digits>`, scope `inference`, all models, all routes, free tier.

Lesson: "email delivery is broken" findings rot. Always re-test the verify-mail path before
concluding an email-gated chain is dead — one Mailinator inbox check flipped a hard wall into
full API-key issuance.

## Probe adjustment (ci-cd × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
