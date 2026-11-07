# C. WEB APP — AUTHZ — edge-node / low-priv

- source canon: `holyshit-mode/vector-matrix.md`
- base technique: `holyshit-mode-vector-matrix-c-web-app-authz.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **edge-node** · auth **low-priv** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

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

## Probe adjustment (edge-node × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
