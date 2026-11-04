# Lateral rules (the strictest)

- source canon: `kaisha/ladder-playbook.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

1. Own declared estates only — the scope authority (`~/.redteam/scope.json`) is
   checked; out-of-scope hosts refuse.
2. One shot per path per engagement window — never repeated without drift.
3. Nothing persists: no keys copied to disk, no schedules, no implants.
4. Every CONFIRMED lateral → shukaku ingest (the family loop closes).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
