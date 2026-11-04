# STUDY MODE — T−10 (before first contact, when a CVE or prior teardown matches the stack)

- source canon: `3am-shinjitsu/arsenal-index.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
