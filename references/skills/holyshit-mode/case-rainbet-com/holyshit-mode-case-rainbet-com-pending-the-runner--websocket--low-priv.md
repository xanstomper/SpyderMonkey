# Pending (the runner) — websocket / low-priv

- source canon: `holyshit-mode/case-rainbet-com.md`
- base technique: `holyshit-mode-case-rainbet-com-pending-the-runner.md`
- bindings: **WSTG-SESS** · **CWE-287** · **ATT&CK T1528**
- context: **websocket** · auth **low-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: state carries across frames — the replay/state-bypass classes apply frame-to-frame
- auth state: hold ONE low-priv principal; swap object ids/roles upward only (idor/authz classes)

## The technique

**CLOSED** — superseded by the ceiling verdict above. The session-dependent tests
(stel_token fixation verdict, wallet/vault/seeds surface, x-public-id socket join) remain
documented as the unlock list for a non-blocked vantage or an operator session.

## Probe adjustment (websocket × low-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
