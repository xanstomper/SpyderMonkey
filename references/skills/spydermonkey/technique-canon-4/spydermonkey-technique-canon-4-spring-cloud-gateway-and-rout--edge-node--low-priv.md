# Spring Cloud Gateway and routing-injection classes — edge-node / low-priv

- source canon: `spydermonkey/technique-canon-4.md`
- base technique: `spydermonkey-technique-canon-4-spring-cloud-gateway-and-rout.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- context: **edge-node** · auth **low-priv** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

Documented actuator-driven route injection is REPORTED as the mechanism writeup; decisive test is the config-diff endpoint's presence, not the executed reroute.

## Probe adjustment (edge-node × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
