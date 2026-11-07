# Prototype pollution (__proto__ / constructor.prototype)

- source canon: `spydermonkey/technique-canon.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Client-side merge sinks (or query-string ?__proto__[x]=y) that reach a gadget. Decisive test: pollution observable in-page (Object.keys diff) — gadget reach = the severity; no gadget = informational.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
