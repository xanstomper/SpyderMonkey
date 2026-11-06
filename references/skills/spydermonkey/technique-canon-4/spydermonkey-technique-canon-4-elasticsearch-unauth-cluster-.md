# Elasticsearch unauth cluster (9200)

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-06

## The technique

Cluster health + indices readable unauth. Decisive test: GET / and /_cat/indices — index inventory (names/shapes) = the finding; document reads stay sample-only (your own test doc).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
