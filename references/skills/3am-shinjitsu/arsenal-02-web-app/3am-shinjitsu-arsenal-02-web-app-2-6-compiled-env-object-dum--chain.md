# 2.6 Compiled env-object dump (score 80) — chain composition

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- base technique: `3am-shinjitsu-arsenal-02-web-app-2-6-compiled-env-object-dum.md`
- chain role: **final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it**

## Chain roles

- final — this CLOSES a chain: shukaku prices what it reaches; chain detect looks for the entries that feed it

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- DECISIVE: grep every chunk for `VITE_[A-Z_0-9]+:` (backtick-aware: Vite compiles strings as
  template literals — plain quote-greps return EMPTY and you conclude "no surface" falsely).
- CONFIRMED WHEN: prod payment test-mode flags ON, New Relic license keys, internal bot names,
  `VITE_SUPABASE_*`, unshipped feature flags.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
