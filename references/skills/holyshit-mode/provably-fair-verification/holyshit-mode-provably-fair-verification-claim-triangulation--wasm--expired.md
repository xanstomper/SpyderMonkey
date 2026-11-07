# Claim-triangulation vs extortion narratives — wasm / expired

- source canon: `holyshit-mode/provably-fair-verification.md`
- base technique: `holyshit-mode-provably-fair-verification-claim-triangulation.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **wasm** · auth **expired** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

Separate an extorter's WIRE-TESTABLE claims (PF structure, outcome timing, hash chain)
from CREDENTIAL-HELD claims (DB reads, "predicted outcomes before finish" — which their
own wording may attribute to staff/DB read access). Test the wire claims live and publish
the reproducible result; attribute the rest to the already-documented credential
compromise. An extorter's headline claim that FAILS to reproduce publicly is still their
primer for the next drop — the rebuttal package (two consecutive hashes + one sha256
call, plus the honest caveats: forced-path capability, own-curve derivation, authed-UI
channel) is the deliverable that blunts it before publication.

## Probe adjustment (wasm × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
