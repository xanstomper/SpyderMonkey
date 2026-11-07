# C. WEB APP — AUTHZ

- source canon: `holyshit-mode/vector-matrix.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-07

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
