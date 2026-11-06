# Bundle/chunk extraction discipline (the engagement-ops recipe)

- source canon: `spydermonkey/technique-canon-7.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

Loader-stub hosts hide the logic one layer deep: follow import graphs into chunks/ — the env→host map, default-env constants, query-string auth readers live there (SPY-095 recipe). Decisive test: the extracted map verbatim from the served binary.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
