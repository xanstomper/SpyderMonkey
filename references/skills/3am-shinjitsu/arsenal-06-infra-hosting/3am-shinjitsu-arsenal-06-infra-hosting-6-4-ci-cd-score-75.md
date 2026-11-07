# 6.4 CI/CD (score 75)

- source canon: `3am-shinjitsu/arsenal-06-infra-hosting.md`
- bindings: **WSTG-CONF-04** · **CWE-798** · **ATT&CK T1552**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- Public workflow logs with secrets; self-hosted runner exposure; artifact signing gaps;
  branch-protection bypass; deploy-key scope. Read-only: log pages + API reads of public repos.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
