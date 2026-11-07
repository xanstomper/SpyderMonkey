# STUDY MODE — T−10 (before first contact, when a CVE or prior teardown matches the stack) — edge-node / high-priv

- source canon: `3am-shinjitsu/arsenal-index.md`
- base technique: `3am-shinjitsu-arsenal-index-study-mode-t-10-before-first-con.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **edge-node** · auth **high-priv** · chain role **pivot**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: cdn/origin edge — cache key and origin-pull trust are the class surface
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

Prepared exploitation is the only minutes-class lever. If the era-stack fingerprint hits a
known-CVE class, run the engine BEFORE the scan:
1. `python3 scripts/exploit-intel.py teardown <CVE|keyword>` → five-gene teardown JSON
2. Gene → vector translation (engine §3 CWE table) chooses the battery section
3. Δ against observed stack (engine §5) → decisive test definition
4. `register --target <T> --teardown <file>` → lands in campaign state; run at `[E]` priority
5. No known CVE? `synthesize/derive` against the observed flaw-families × trust-seams
   (vector-synthesis-matrix.md; queue into `exploit_intel.synthesis_queue[]`)

Engine: `references/exploit-intelligence-engine.md` · Runner: `scripts/exploit-intel.py`
Synthesis battery: `references/vector-synthesis-matrix.md` (36 pairs + §R remainder rule)

## Probe adjustment (edge-node × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
