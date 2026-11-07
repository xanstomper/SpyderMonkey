# Route-map mining (the big win) — kubernetes / high-priv

- source canon: `holyshit-mode/case-apimart-newapi-fork.md`
- base technique: `holyshit-mode-case-apimart-newapi-fork-route-map-mining-the-.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **kubernetes** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

The fork has dozens of custom routes invisible to endpoint guessing: `/api/user/reset_by_code`,
`/api/user/login/email/code`, `/api/web/runtime-key`, `/api/web/token/batch`, `/api/admin-auth`,
`/api/user/free-trial/usage`, `/api/user/promo-discount/preview`, `/api/user/membership`,
`/api/user/{stripe,paypal,nowpayments,antom}/pay`, `/api/messages/tickets/*`, `/api/region-access`.

Method: fetch every `src="/_next/static/chunks/*.js"` from ALL page variants (homepage, /console,
/pricing — each page loads different chunks), then regex `["\'](/api/[A-Za-z0-9_/.-]{2,80})["\']`.
Endpoint guessing alone found ~8 routes; chunk mining found 40+.

## Probe adjustment (kubernetes × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
