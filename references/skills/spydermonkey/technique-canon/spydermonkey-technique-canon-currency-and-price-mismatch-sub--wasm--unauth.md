# Currency and price-mismatch substitution — wasm / unauth

- source canon: `spydermonkey/technique-canon.md`
- base technique: `spydermonkey-technique-canon-currency-and-price-mismatch-sub.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- context: **wasm** · auth **unauth** · chain role **final**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

A client-supplied currency code (or price object) re-priced by the server at a stale rate is a rounding/repricing seam. Decisive test: switch currency mid-checkout and diff the converted line prices against the live FX the page displays — persistent mismatch = the finding.

## Probe adjustment (wasm × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- the impact leg — shukaku prices what this rung reaches
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
