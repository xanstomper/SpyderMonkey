# Evidence discipline (repeat offenders this session) — api / high-priv

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-evidence-discipline-re.md`
- bindings: **WSTG-SESS-01** · **CWE-347** · **ATT&CK T1552**
- context: **api** · auth **high-priv** · chain role **pivot**

## Context

- platform: strike the JSON body + query string; content-type and parameter placement change the probe shape
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

- Retract inflated findings when the full response disproves them (mass-assignment case).
- Hypothesis ≠ confirmed: Discord renders identical HTML for valid/invalid redirect_uri
  (error only after JS exec) — server-side curl cannot distinguish; keep such chains
  as hypothesis until a real browser session proves them.
- Decode JWT payloads (`cut -d. -f2 | base64 -d`) to enumerate claims the backend may
  mistakenly trust, but test the actual gate before claiming escalation.

## Probe adjustment (api × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
