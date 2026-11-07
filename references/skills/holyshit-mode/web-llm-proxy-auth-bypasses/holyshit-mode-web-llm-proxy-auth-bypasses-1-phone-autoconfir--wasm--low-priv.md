# 1. Phone autoconfirm = instant confirmed accounts — wasm / low-priv

- source canon: `holyshit-mode/web-llm-proxy-auth-bypasses.md`
- base technique: `holyshit-mode-web-llm-proxy-auth-bypasses-1-phone-autoconfir.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **wasm** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- `GET /auth/v1/settings` reveals `phone_autoconfirm: true`, `mailer_autoconfirm: false`.
- `POST /auth/v1/signup` with `{"phone":"+1...","password":"..."}` returns a FULL session
  (access_token + refresh_token) with NO SMS/OTP step. Accounts mint in ~2s.
- Rate limits on the AI proxy (~6 req/min) are defeated by minting fresh accounts and rotating.
- Pitfall: response shape differs by flow — email signup nests the session under `session`,
  phone signup may return access_token at top level. Parse both.

## Probe adjustment (wasm × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
