# 2.1 405-matrix first (score 80, T≈2min)

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- DECISIVE: for each discovered path: `curl -s -o /dev/null -w '%{http_code} %{content_type}'
  -X <M> <path>` for M ∈ {GET, POST, PUT, PATCH, DELETE, OPTIONS}
- CONFIRMED WHEN: 405 on GET + 200/400/422 on POST = POST-only surface the GET sweep missed.
- Pair with §3.10 POST-`{}` sweep: an endpoint can accept POST only.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
