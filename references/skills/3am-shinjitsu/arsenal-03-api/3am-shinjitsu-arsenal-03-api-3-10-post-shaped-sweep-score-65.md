# 3.10 POST-shaped sweep (score 65)

- source canon: `3am-shinjitsu/arsenal-03-api.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- One pass: replay every discovered path with `-X POST -d '{}'`. 404 = method-bound ghost;
  200/201/400/500 = real POST surface. Log 500s as regressions.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
