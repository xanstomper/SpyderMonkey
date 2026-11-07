# 8. Cross-brand (sibling-domain) drift — host / unauth

- source canon: `holyshit-mode/engineio-socketio-testing.md`
- base technique: `holyshit-mode-engineio-socketio-testing-8-cross-brand-siblin.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **host** · auth **unauth** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: era-stack banner mapping (kaisha cve) before any rung
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

- Sister brands on the same stack (same error envelopes, CSP, cookies, CDN IPs): diff RPC method tables, namespace sets, endpoint literals, and gate behavior across brands. Older deployments expose different (usually smaller) surfaces and reveal which gates are new.
- Read the namespace init packet's `serverHost` — pods named `<brand>-rcc-slave-*` identify the INFRA OWNER and prove the fleet relationship at the socket level (a sister brand serving your sockets = same operator; their CSP cross-brand collectors corroborate).
- When the origin brand is geo-blocked from your vantage, its accessible sister brand usually runs the SAME shared data plane — the sister is the working vantage; probing the geo-walled brand's socket/API directly is wasted calls.

## Probe adjustment (host × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
