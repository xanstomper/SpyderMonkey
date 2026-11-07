# 6.3 K8s/container surfaces (score 80, banner/anon-read only)

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- 2379 etcd (anon read = the finding), 10250 kubelet, dashboard 30000-32767, API 6443
  anonymous, registry 5000 anon pull, `:latest` overwrite check (read-only manifest pull).

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
