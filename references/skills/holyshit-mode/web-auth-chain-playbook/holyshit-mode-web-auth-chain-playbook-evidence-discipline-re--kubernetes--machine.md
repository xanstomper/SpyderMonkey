# Evidence discipline (repeat offenders this session) — kubernetes / machine

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-evidence-discipline-re.md`
- bindings: **WSTG-SESS-01** · **CWE-347** · **ATT&CK T1552**
- context: **kubernetes** · auth **machine** · chain role **pivot**

## Context

- platform: RBAC/service-account surface — read-only enumeration, crown the exposure
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

- Retract inflated findings when the full response disproves them (mass-assignment case).
- Hypothesis ≠ confirmed: Discord renders identical HTML for valid/invalid redirect_uri
  (error only after JS exec) — server-side curl cannot distinguish; keep such chains
  as hypothesis until a real browser session proves them.
- Decode JWT payloads (`cut -d. -f2 | base64 -d`) to enumerate claims the backend may
  mistakenly trust, but test the actual gate before claiming escalation.

## Probe adjustment (kubernetes × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
