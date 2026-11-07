# 6. Outcome-derivation test

- source canon: `holyshit-mode/provably-fair-verification.md`
- bindings: **WSTG-BUSL-01** · **CWE-681** · **ATT&CK T1565**
- generated: 2026-11-07

## Route

- probes: `nmap-script-default`, `httpx`, `whatweb`, `webanalyze`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

Apply the standard hash→multiplier formula (bustabit-style: first 52 bits of the hash
→ house-edge curve) to captured rounds and compare to observed crash points. Mismatch
= the operator uses their own curve — locate it in the client math chunk (grep the
pooled bundle for the game's math/config module). Not a finding alone, but full public
verification requires the exact derivation to be documented.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
