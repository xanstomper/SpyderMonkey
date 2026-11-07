# How to use (90-second protocol) — mesh / service

- source canon: `3am-shinjitsu/vector-synthesis-matrix.md`
- base technique: `3am-shinjitsu-vector-synthesis-matrix-how-to-use-90-second-p.md`
- bindings: **WSTG-CRYPTO-04** · **CWE-329** · **ATT&CK T1573**
- context: **mesh** · auth **service** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: service-mesh sidecar surface — own mesh, read-only mTLS posture
- auth state: a daemon/listener identity — the probe targets what the service can see and invoke, not what a human session can

## The technique

1. Note the target's **flaw families** (from era-stack, framework signatures, design
   reading — §9 ladder rungs 1–2) and **trust seams** (observed trust boundaries).
2. Cross them against the matrix rows: matching row → score §14 → run the decisive
   one-liner. Unlisted pairs → apply the remainder rule (§R) to derive the probe.
3. Every run goes to `exploit_intel.synthesis_queue[]`; every negative is ledgered with
   its exact test (anti-loop canon).

## Probe adjustment (mesh × service)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
