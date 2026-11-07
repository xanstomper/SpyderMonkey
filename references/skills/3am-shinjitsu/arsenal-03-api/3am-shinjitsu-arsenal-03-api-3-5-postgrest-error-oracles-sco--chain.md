# 3.5 PostgREST error oracles (score 70, RLS-safe recon) — chain composition

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- base technique: `3am-shinjitsu-arsenal-03-api-3-5-postgrest-error-oracles-sco.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- `PGRST205` table absent · `[]` table exists+RLS-gated · `42703` on `?select=<col>` = free
  column-name brute · `22P02` = column TYPE oracle · `PGRST301` = PostgREST uses a DIFFERENT
  JWT trust root than GoTrue (forge against both separately).
- Schema map from errors = coverage finding even when RLS holds.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
