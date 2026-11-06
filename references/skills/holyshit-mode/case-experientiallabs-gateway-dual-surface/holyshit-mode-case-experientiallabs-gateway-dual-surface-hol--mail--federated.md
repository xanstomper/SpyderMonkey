# holyleadger chain-splitter gotcha — mail / federated

- source canon: `holyshit-mode/case-experientiallabs-gateway-dual-surface.md`
- base technique: `holyshit-mode-case-experientiallabs-gateway-dual-surface-hol.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **mail** · auth **federated** · chain role **pivot**

## Context

- platform: spf/dkim/dmarc record surface — spoofing and spoofability live in the record math
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

`chain <jewel> "A→B→C:confirmed"` splits steps on the unicode `→` via
`steps_status.rpartition(":")`. If the arg arrives with the arrow mangled or with no valid
`:status` suffix, the chain records `steps:[""]` (1 empty step) — appears to "work" (rc 0)
but is empty. Reliable workaround: write `data["chains"]` directly into the ledger JSON, or
pass the chain string through Python (not a shell that may mangle `→`). Don't burn time on
the CLI quirk mid-engagement; set the chain by hand in the JSON.

## Probe adjustment (mail × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
