# 2.11 Injected-input classes (score per-cell, from vector-matrix B) — chain composition

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-11-injected-input-classes.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- One decisive probe per class, on ONE parameter, once: SQLi (error/boolean/time), NoSQLi
  (`{"$ne":null}` in JSON fields), SSTI (`{{7*7}}` in rendered/report fields), path traversal
  (`../%2e%2e` on filename/range/zip-entry), open redirect (`//evil`, `/\evil`, `@evil`),
  prototype pollution (`__proto__` in JSON merges), XXE (OOB DNS canary only).
- CONFIRMED WHEN: oracle in response (diff, error, canary callback). No spraying: one param,
  one class, one probe; a twice-failed approach is dead.
- CSV/formula injection in export features (`=cmd`); webhooks unsigned/replayable.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
