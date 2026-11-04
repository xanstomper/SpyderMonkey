# 1.1 Era-stack header grab (score 80, T≈1min)

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- generated: 2026-11-04

## The technique

- DECISIVE: `curl -sI https://<target>/` and on the API host separately
- READ: `Server`, `X-Powered-By`, `via`, `x-served-by`, `x-turbo-by`, `x-kong-*`,
  `www-authenticate`, `content-generator`, `x-generator`
- CONFIRMED WHEN: any component EOL per §1.12 table
- FP: CDN-injected headers (`via` from CF/Fastly is not the origin stack)

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
