# 7.3 Framework-default admin planes (score 75)

- source canon: `3am-shinjitsu/arsenal-07-supply-chain.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-04

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

- SET: Spring `/actuator/*` (env, heapdump, jolokia), Django admin `/admin/` (title oracle),
  Laravel `/telescope`, `/horizon`, Strapi admin, `/debug/vars` (expvar), `/_debug/bar`,
  phpLiteAdmin/Adminer, phpMyAdmin paths, `/console` (WERKZEUG debugger PIN page).
- DISCRIMINATOR: status + content-type pair (§2.2) + a title/body fingerprint, once each.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
