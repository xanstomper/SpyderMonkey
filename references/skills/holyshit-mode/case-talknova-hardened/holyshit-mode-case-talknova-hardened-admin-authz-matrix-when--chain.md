# Admin authz matrix (when admin endpoints are discovered) — chain composition

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-admin-authz-matrix-when.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- GET unauth → expect 401
- POST unauth → expect 401
- PATCH/DELETE unauth → expect 401
- IDOR by numeric ID (`/users/1`, `/grants/1`, `/custom-keys/1`) → expect 401
- Mass assignment probe (`{"plan":"max","is_admin":true}`) → expect 401 or validation error
- Rate-limit probe on login → note decay time (talknova: 30 min)

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
