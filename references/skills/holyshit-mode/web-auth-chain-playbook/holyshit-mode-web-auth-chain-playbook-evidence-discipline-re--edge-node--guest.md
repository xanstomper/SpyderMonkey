# Evidence discipline (repeat offenders this session) — edge-node / guest

- source canon: `holyshit-mode/web-auth-chain-playbook.md`
- base technique: `holyshit-mode-web-auth-chain-playbook-evidence-discipline-re.md`
- bindings: **WSTG-SESS-01** · **CWE-347** · **ATT&CK T1552**
- context: **edge-node** · auth **guest** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- Retract inflated findings when the full response disproves them (mass-assignment case).
- Hypothesis ≠ confirmed: Discord renders identical HTML for valid/invalid redirect_uri
  (error only after JS exec) — server-side curl cannot distinguish; keep such chains
  as hypothesis until a real browser session proves them.
- Decode JWT payloads (`cut -d. -f2 | base64 -d`) to enumerate claims the backend may
  mistakenly trust, but test the actual gate before claiming escalation.

## Probe adjustment (edge-node × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
