# 2.2 Ghost-route discrimination (score 75 — kills false positives)

- source canon: `3am-shinjitsu/arsenal-02-web-app.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-07

## Route

- probes: `s3scanner`, `cloudbrute`, `cloudlist`, `kube-hunter`, `shodan`
- chains: `cloud-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- RULE: status alone proves NOTHING on SPA/CDN deployments. Every path returns 200 text/html.
- REAL = `application/json` (or `text/event-stream`, `application/msgpack`).
- Cloudflare Access wall: `Sign in · Cloudflare Access` title on EVERY path incl. JSON APIs
  = WALL, not response. Record WALL for the phase; verdicts from a gated host are junk.
- Sensitive-file soft-404: identical `DOCTYPE html / charset=utf8 / viewport` 200 = absent.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
