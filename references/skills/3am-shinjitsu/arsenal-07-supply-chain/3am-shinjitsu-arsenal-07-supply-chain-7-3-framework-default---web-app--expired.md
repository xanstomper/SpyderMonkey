# 7.3 Framework-default admin planes (score 75) — web-app / expired

- source canon: `3am-shinjitsu/arsenal-07-supply-chain.md`
- base technique: `3am-shinjitsu-arsenal-07-supply-chain-7-3-framework-default-.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **web-app** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

- SET: Spring `/actuator/*` (env, heapdump, jolokia), Django admin `/admin/` (title oracle),
  Laravel `/telescope`, `/horizon`, Strapi admin, `/debug/vars` (expvar), `/_debug/bar`,
  phpLiteAdmin/Adminer, phpMyAdmin paths, `/console` (WERKZEUG debugger PIN page).
- DISCRIMINATOR: status + content-type pair (§2.2) + a title/body fingerprint, once each.

## Probe adjustment (web-app × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
