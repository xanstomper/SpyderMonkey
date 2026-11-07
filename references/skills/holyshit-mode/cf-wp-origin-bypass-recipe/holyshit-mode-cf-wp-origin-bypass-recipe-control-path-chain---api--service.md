# Control-path chain (what "gaining control" requires here) — api / service

- source canon: `holyshit-mode/cf-wp-origin-bypass-recipe.md`
- base technique: `holyshit-mode-cf-wp-origin-bypass-recipe-control-path-chain-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **api** · auth **service** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

`origin_ip_exposed -> cf_waf_bypassed -> direct_origin_wp_admin -> admin_credential_access ->
wp-admin -> plugin/theme RCE -> full control`. The blocker on this target: native auth enforced
on all data endpoints (orders/customers/payment-gateway secrets need a session), maintenance is
vhost-level, so the remaining levers are (a) a known-CVE plugin exploit landing WAF-less against
the exact inventory, or (b) finding the admin password via sibling-domain/backup/source-mining.

## Probe adjustment (api × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
