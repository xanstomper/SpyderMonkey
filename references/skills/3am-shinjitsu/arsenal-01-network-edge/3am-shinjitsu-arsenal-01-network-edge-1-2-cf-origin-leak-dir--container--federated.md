# 1.2 CF-origin leak → direct-origin WAF bypass (score 90, T≈3min) — THE first move — container / federated

- source canon: `3am-shinjitsu/arsenal-01-network-edge.md`
- base technique: `3am-shinjitsu-arsenal-01-network-edge-1-2-cf-origin-leak-dir.md`
- bindings: **WSTG-INFO** · **CWE-200** · **ATT&CK T1592**
- context: **container** · auth **federated** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

- DECISIVE: `dig +short <target> TXT @1.1.1.1` → grep `v=spf1 ip4:<ip>`
- VERIFY: python `http.client.HTTPSConnection(<ip>, context=ssl._create_unverified_context())`,
  `Host:`/SNI = `<target>`. Real app HTML (not CF interstitial) = WAF bypassed entirely.
- ALSO: `dig AAAA` — IPv6 often un-CDN'd (shadow surface); check DMARC `rua`/hosting MX headers.
- FP: SPF `include:` chains — resolve the IP in the include, not the include name.
- NEXT: full route map direct-to-origin; re-run ghost-route sweep origin-side (CDN may mask).

## Probe adjustment (container × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
