# NoSQL operator injection ($ne, $regex) — mesh / unauth

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-nosql-operator-injection-ne-reg.md`
- bindings: **WSTG-INPV** · **CWE-74** · **ATT&CK T1190**
- context: **mesh** · auth **unauth** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

JSON body operators accepted server-side ({"pass":{"$ne":""}}). Decisive test: {"$ne":null} on the login body of YOUR test account — a 200 without the password = the class.

## Probe adjustment (mesh × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
