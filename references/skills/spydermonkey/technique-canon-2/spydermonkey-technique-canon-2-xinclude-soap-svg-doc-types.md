# XInclude / SOAP / SVG-doc types

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **WSTG-BUSL-09** · **CWE-434** · **ATT&CK T1190**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Fragment-level XML parsers (XInclude on a node, SOAP body, SVG/image upload parsing) carry the same entity class without full-document control. Decisive test: OOB marker through each fragment type.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
