# Rails mass-assignment and render-params classes

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-INPV** · **CWE-1321** · **ATT&CK T1190**
- generated: 2026-11-06

## The technique

`render params[]` legacy and to_json exposure of sensitive columns. Decisive test: crafted params[:object] nested keys accepted on YOUR test record — the persisted field is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
