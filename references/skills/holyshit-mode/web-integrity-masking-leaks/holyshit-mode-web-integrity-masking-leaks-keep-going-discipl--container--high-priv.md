# Keep-going discipline on a mapped target — container / high-priv

- source canon: `holyshit-mode/web-integrity-masking-leaks.md`
- base technique: `holyshit-mode-web-integrity-masking-leaks-keep-going-discipl.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **container** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

When the operator keeps demanding more: re-audit for genuinely UNTESTED classes
(other protocol versions, parameter fuzz on legacy PHP apps, CL.TE smuggling on
CDN-to-origin stacks, every panel endpoint with the minted token), test them
fresh, and present the completed vector matrix as the deliverable. Never
re-fire a verified-negative wall to manufacture progress, and never upgrade a
mint-flaw to "access" to satisfy the demand.

## Probe adjustment (container × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
