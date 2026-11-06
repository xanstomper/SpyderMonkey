# 2.6 Compiled env-object dump (score 80)

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-04

## The technique

- DECISIVE: grep every chunk for `VITE_[A-Z_0-9]+:` (backtick-aware: Vite compiles strings as
  template literals — plain quote-greps return EMPTY and you conclude "no surface" falsely).
- CONFIRMED WHEN: prod payment test-mode flags ON, New Relic license keys, internal bot names,
  `VITE_SUPABASE_*`, unshipped feature flags.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
