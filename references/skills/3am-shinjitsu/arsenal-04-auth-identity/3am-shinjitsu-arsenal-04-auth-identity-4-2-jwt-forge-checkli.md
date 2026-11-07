# 4.2 JWT forge checklist — OFFLINE FIRST (zero traffic before this)

- source canon: `3am-shinjitsu/arsenal-04-auth-identity.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-07

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- (a) OFFLINE crack of known sig with default/self-hosted secrets (SupaBomb list) — hashcat.
- (b) HS256 forge with anon-key-as-secret against `/auth/v1/user` AND `/rest/v1/` separately
  (`PGRST301` = separate trust root).
- (c) alg:none, `jwk` header injection, tamper-keep-sig, kid-injection, RS256→HS256 confusion.
- GoTrue checks claims BEFORE signature: `missing sub claim` = sig never ran — reorder probes.
- Uniform `invalid_api_key` for EVERY bearer/JWT/alg-none variant = no JWT path exists —
  log the negative, STOP (keys are opaque strings; forging is chasing nothing).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
