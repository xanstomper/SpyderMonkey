# Command injection via double-quote/pipe variants — cloud / high-priv

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-command-injection-via-double-qu.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **cloud** · auth **high-priv** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

The documented class vocabulary (backtick, $( ), newline, %0a) applied ONE variant per request. Decisive test: an out-of-band marker (DNS to your registered domain) beats response-diff for blind injection — the marker arrival is the proof.

## Probe adjustment (cloud × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
