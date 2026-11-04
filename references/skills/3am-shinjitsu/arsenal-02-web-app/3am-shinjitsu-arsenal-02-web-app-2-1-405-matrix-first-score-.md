# 2.1 405-matrix first (score 80, T≈2min)

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- generated: 2026-11-04

## The technique

- DECISIVE: for each discovered path: `curl -s -o /dev/null -w '%{http_code} %{content_type}'
  -X <M> <path>` for M ∈ {GET, POST, PUT, PATCH, DELETE, OPTIONS}
- CONFIRMED WHEN: 405 on GET + 200/400/422 on POST = POST-only surface the GET sweep missed.
- Pair with §3.10 POST-`{}` sweep: an endpoint can accept POST only.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
