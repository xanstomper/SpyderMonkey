# First-party OIDC (separate from GoTrue external OAuth) — windows / service

- source canon: `holyshit-mode/oauth-redirect-uri-impact-gate.md`
- base technique: `holyshit-mode-oauth-redirect-uri-impact-gate-first-party-oid.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **windows** · auth **service** · chain role **pivot**

## Route

- probes: `sslscan`, `sslyze`, `testssl`, `tlsx`, `ssh-audit`, `openssl`, `nmap-ssl-ciphers`, `nmap-script-ssl`, `ssh-keyscan`
- chains: `tls`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: token/session confusion classes; read-only enumeration, NO-GAIN
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

Platforms that offer "Login with X" via their own OIDC provider (`/oauth/authorize` + `/api/oauth/token`) are a SEPARATE auth surface from the Supabase GoTrue external OAuth (Discord/Google). On example-target.xyz the first-party flow used:

- PKCE S256 with `crypto.getRandomValues(48)` verifier — proper, not bruteable
- `code_challenge_method: S256`, nonce, sessionStorage state binding
- Server rejects garbage codes with uniform `invalid_grant`

Treat first-party OIDC as hardened unless the verifier is `Math.random()`-based or the challenge method is `plain`. Mine the SPA bundle for the PKCE generation function to confirm — `grep -oE 'crypto\.getRandomValues|Math\.random' firstPartyOidc*.js`.

## Probe adjustment (windows × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
