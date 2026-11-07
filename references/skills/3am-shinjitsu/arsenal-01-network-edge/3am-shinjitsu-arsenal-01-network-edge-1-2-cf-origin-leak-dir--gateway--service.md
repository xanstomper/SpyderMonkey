# 1.2 CF-origin leak → direct-origin WAF bypass (score 90, T≈3min) — THE first move — gateway / service

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-2-cf-origin-leak-dir.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **gateway** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: api/front-door tier — routing and authn decisions here are the differential
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

- DECISIVE: `dig +short <target> TXT @1.1.1.1` → grep `v=spf1 ip4:<ip>`
- VERIFY: python `http.client.HTTPSConnection(<ip>, context=ssl._create_unverified_context())`,
  `Host:`/SNI = `<target>`. Real app HTML (not CF interstitial) = WAF bypassed entirely.
- ALSO: `dig AAAA` — IPv6 often un-CDN'd (shadow surface); check DMARC `rua`/hosting MX headers.
- FP: SPF `include:` chains — resolve the IP in the include, not the include name.
- NEXT: full route map direct-to-origin; re-run ghost-route sweep origin-side (CDN may mask).

## Probe adjustment (gateway × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
