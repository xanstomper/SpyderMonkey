# Control-path chain (what "gaining control" requires here) — web-app / high-priv

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-control-path-chain-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **web-app** · auth **high-priv** · chain role **pivot**

## Context

- platform: strike through the browser/proxy path; the 3-gate differential runs on the reflected/accepted value
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

`origin_ip_exposed -> cf_waf_bypassed -> direct_origin_wp_admin -> admin_credential_access ->
wp-admin -> plugin/theme RCE -> full control`. The blocker on this target: native auth enforced
on all data endpoints (orders/customers/payment-gateway secrets need a session), maintenance is
vhost-level, so the remaining levers are (a) a known-CVE plugin exploit landing WAF-less against
the exact inventory, or (b) finding the admin password via sibling-domain/backup/source-mining.

## Probe adjustment (web-app × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
