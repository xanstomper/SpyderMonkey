# SupaBomb / JWT forge attempt (2026-10-03, all dead)

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- alg:none → `signing method none is invalid`; tampered-payload-same-sig → rejected; **HS256 forge with anon-key-as-secret** (the textbook Supabase confusion — the anon key is itself an HS256 JWT with `role:anon`, signed with the same secret class that signs access tokens) → rejected on GoTrue AND PostgREST (`PGRST301 No suitable key or wrong key type` — PostgREST verifies with a different key, layered trust roots); jwk-header injection (CVE-2016-10555 style) → rejected; offline weak-secret crack of the known anon-key sig vs ~20 common secrets incl. default self-hosted `super-secret-jwt-token-with-at-least-32-characters-long` → no hit. GoTrue checks claims BEFORE signature (`missing sub claim` errors first). Offline crack against a known sig is free (zero requests) — always do it before any online probe.
- Supabase service-path sweep on the auth host: `/pg` 401 / `/pg/meta` 403 Kong-gated ("You cannot consume this service"); `/functions/v1/` 503 name-resolution; `/realtime/v1/websocket` 403 pre-handshake; `/storage/v1/bucket` → `[]` for anon, `POST /bucket/list` route 404; `/storage/v1/status` 200.
- **Stack-topography lesson**: PostgREST + storage + pg-meta + functions + realtime all lived on the AUTH host, NOT the api host. Probe every Supabase service path (`/rest/v1/`, `/storage/v1/`, `/pg`, `/pg/meta`, `/functions/v1/`, `/realtime/v1/`) on EVERY Kong-fronted auth host — topography varies per deployment.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
