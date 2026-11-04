# 6.9 Observability plane (score 70)

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## The technique

- Grafana/Prometheus anon (`/api/status`), Jaeger/Zipkin exposure, `/metrics` on API hosts.
- Status pages: incident post-mortems leak infra names/timelines — free recon.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
