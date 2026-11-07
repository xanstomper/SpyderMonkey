# STUDY MODE — T−10 (before first contact, when a CVE or prior teardown matches the stack) — chain composition

- source canon: `3am-shinjitsu/arsenal-index.md`
- base technique: `3am-shinjitsu-arsenal-index-study-mode-t-10-before-first-con.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
