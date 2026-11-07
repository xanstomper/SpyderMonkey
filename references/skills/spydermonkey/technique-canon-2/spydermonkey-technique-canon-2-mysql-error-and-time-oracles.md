# MySQL error and time oracles

- source canon: `spydermonkey/technique-canon-2.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- generated: 2026-11-06

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

ExtractValue/`updatexml` error-channel reflection and `SLEEP(n)`/`BENCHMARK` timing channel — error-first, one timing sample per request against a 3-sample baseline. Decisive test: error string with controlled content echoed, or a stable timing delta ≥ 10× baseline.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
