# .git /.env /backup discovery discipline

- source canon: `spydermonkey/technique-canon.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-06

## The technique

Distinguish SPA-fallback 200 shells from REAL exposure: require content distinct from the canonical nonexistent-path control (size/content-type delta). Decisive test: control path vs candidate path — identical shell = exhausted, different = the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
