# The 4-step chain (verified end-to-end, ~60s) — browser / high-priv

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-the-4-step-chain-verif.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **browser** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

1. **Confirmed session with zero verification.** If `phone_autoconfirm: true`,
   `POST /auth/v1/signup` with a phone number returns a full session (access_token +
   refresh_token, `phone_confirmed_at` set) — no SMS delivered or checked. Also test
   arbitrary `data:` fields (mass assignment) but VERIFY against the full response: GoTrue
   strips `user_metadata`/`app_metadata` from the body in recent versions — retract the
   finding if fields are not echoed back.
2. **RLS write escalation on trust flags.** With the session JWT as
   `Authorization: Bearer` + anon key as `apikey`, try
   `PATCH /rest/v1/profiles?user_id=eq.<self>` with `{"email_verified": true}`. Row-owner
   RLS often permits writing user-controlled boolean trust flags the backend then gates on.
   Check constraint errors (pg 23514) reveal allowed column value sets.
3. **Key/feature minting behind the trust gate.** Retest the previously-401 backend
   endpoints (`/api/account/platform-keys` POST → real `gxyz-...` plaintext key;
   `/api/account/settings` PATCH accepts rate-limit increases, clamped server-side).
4. **Free inference.** `POST /v1/chat/completions` on the API host with the minted key.
   Proxy error bodies leak upstream provider state (e.g. Z.ai 403 USER_BLOCKED with
   upstream user_id) — inventory which paid models actually return 200.

## Probe adjustment (browser × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
