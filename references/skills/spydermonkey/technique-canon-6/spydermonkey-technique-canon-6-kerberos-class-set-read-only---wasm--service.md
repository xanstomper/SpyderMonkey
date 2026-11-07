# Kerberos class set (read-only enum) — wasm / service

- source canon: `spydermonkey/technique-canon-6.md`
- base technique: `spydermonkey-technique-canon-6-kerberos-class-set-read-only-.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **wasm** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

AS-REP-roastable accounts, kerberoastable SPNs, unconstrained-delegation CONFIG exposure — all ENUMERABLE read-only (canon-III); the crack/capture stays the no-gain wall. Decisive test: enum output naming the accounts — the list is the finding.

## Probe adjustment (wasm × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
