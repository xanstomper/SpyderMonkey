# Rails mass-assignment and render-params classes

- source canon: `spydermonkey/technique-canon-4.md`
- bindings: **WSTG-INPV** · **CWE-1321** · **ATT&CK T1190**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

`render params[]` legacy and to_json exposure of sensitive columns. Decisive test: crafted params[:object] nested keys accepted on YOUR test record — the persisted field is the finding.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
