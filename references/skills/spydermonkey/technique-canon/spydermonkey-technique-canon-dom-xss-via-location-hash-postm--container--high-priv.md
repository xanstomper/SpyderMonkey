# DOM XSS via location.hash / postMessage — container / high-priv

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-dom-xss-via-location-hash-postm.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- context: **container** · auth **high-priv** · chain role **pivot**

## Route

- probes: `dalfox`, `xsstrike`, `xsser`
- chains: `web`, `api`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

hash-borne sinks and postMessage handlers without origin checks. Decisive test: postMessage from YOUR page to the in-scope window — handler executes with your payload; the alert/echo in YOUR browser session is the proof (self-XSS framing stays hypothesis unless it crosses principals).

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
