# Re-verification of prior confirmeds (doctrine: patch-check FIRST) — grpc / low-priv

- source canon: `holyshit-mode/case-logfare-ai-retest2.md`
- base technique: `holyshit-mode-case-logfare-ai-retest2-re-verification-of-pri.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **grpc** · auth **low-priv** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: reflection/list methods first; protobuf definitions are the schema oracle
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

- **CORS reflection SURVIVED** on every endpoint incl. state-changers:
  `/v1/models`, `/login`, `/register`, `/dashboard`, `/v1/chat/completions` (405 but
  headers present), `POST /v1/auth/regenerate-key`, `/v1/me/delete`, `/v1/me/opt-out` —
  all reflect `access-control-allow-origin: https://evil.com` +
  `access-control-allow-credentials: true` (vary: Origin).
- **BUT auth model changed** to cookie sessions. Observed cookie flags
  (`/v1/auth/discord/start`):
  `logfare_discord_oauth_state=...; HttpOnly; Max-Age=600; Path=/v1/auth/discord; SameSite=lax; Secure`
  SameSite=Lax blocks cross-site POST cookies → prior CVSS ~9.1 downgraded to ~7.1
  (cross-site GET/top-level-nav exposure + misconfig lint, not session hijack).
  Authenticated matrix (real login cookie SameSite, IDOR, regenerate CSRF) needs a session.
- **openapi.json still 200** (24.5KB, 60+ routes, no security schemes declared), /docs public.

## Probe adjustment (grpc × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
