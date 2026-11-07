# SupaBomb / JWT forge attempt (2026-10-03, all dead) — chain composition

- source canon: `holyshit-mode/case-gratisfy-xyz.md`
- base technique: `holyshit-mode-case-gratisfy-xyz-supabomb-jwt-forge-attempt-2.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- alg:none → `signing method none is invalid`; tampered-payload-same-sig → rejected; **HS256 forge with anon-key-as-secret** (the textbook Supabase confusion — the anon key is itself an HS256 JWT with `role:anon`, signed with the same secret class that signs access tokens) → rejected on GoTrue AND PostgREST (`PGRST301 No suitable key or wrong key type` — PostgREST verifies with a different key, layered trust roots); jwk-header injection (CVE-2016-10555 style) → rejected; offline weak-secret crack of the known anon-key sig vs ~20 common secrets incl. default self-hosted `super-secret-jwt-token-with-at-least-32-characters-long` → no hit. GoTrue checks claims BEFORE signature (`missing sub claim` errors first). Offline crack against a known sig is free (zero requests) — always do it before any online probe.
- Supabase service-path sweep on the auth host: `/pg` 401 / `/pg/meta` 403 Kong-gated ("You cannot consume this service"); `/functions/v1/` 503 name-resolution; `/realtime/v1/websocket` 403 pre-handshake; `/storage/v1/bucket` → `[]` for anon, `POST /bucket/list` route 404; `/storage/v1/status` 200.
- **Stack-topography lesson**: PostgREST + storage + pg-meta + functions + realtime all lived on the AUTH host, NOT the api host. Probe every Supabase service path (`/rest/v1/`, `/storage/v1/`, `/pg`, `/pg/meta`, `/functions/v1/`, `/realtime/v1/`) on EVERY Kong-fronted auth host — topography varies per deployment.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
