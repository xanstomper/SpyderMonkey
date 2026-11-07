# C. WEB APP — AUTHZ — worker / guest

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-c-web-app-authz.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **worker** · auth **guest** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- IDOR/BOLA: every GET/PUT/DELETE with enumerateable IDs, cross-account only
- BFLA: privileged API actions replayed as low-priv test user
- Mass assignment: is_admin/role/verified/credits/price/owner_id injected on writes
- Hidden endpoints: ghost routes (playbook §3), debug endpoints (/debug, /actuator, /swagger, /api-docs, /.env)
- Client-only gates: frontend-hidden routes still callable (verify server-side 405/401)
- JWT: alg=none, kid injection, weak HMAC secret (hashcat), no audience check, key-confusion RS256→HS256
- Session: fixation via URL params, no rotation on privilege change, non-HttpOnly, missing SameSite
- OAuth: missing/predictable state, redirect_uri bypass (open-redirect chains), token-in-fragment, PKCE downgrade
- Password reset: host-header poisoning, token-in-URL leakage (referrer), predictability, no single-use
- 2FA: response-status trust, brute-forceable codes, bypass via backup-code enumeration, remember-token reuse

## Probe adjustment (worker × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
