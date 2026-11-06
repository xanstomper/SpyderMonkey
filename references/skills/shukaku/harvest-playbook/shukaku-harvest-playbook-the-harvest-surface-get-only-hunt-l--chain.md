# The harvest surface (GET-only, `hunt --live`) — chain composition

- source canon: `shukaku/harvest-playbook.md`
- base technique: `shukaku-harvest-playbook-the-harvest-surface-get-only-hunt-l.md`
- chain role: **entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow**

## Chain roles

- entry — this OPENS a chain: everything after pairs with it; chain detect looks for same-origin findings that follow

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

backup archives (`backup.zip|tar.gz|sql`, `dump.sql`, `db.sqlite`…), env/config
leaks (`.env`, `.git/config`, `config.*.bak`), admin/admin-export paths,
`api/export(s)`, `debug/vars`, `server-status`. Data plane only — route probing is
UNDERCROFT's. 200s register CONFIRMED with body sizes; **nothing is downloaded**.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
