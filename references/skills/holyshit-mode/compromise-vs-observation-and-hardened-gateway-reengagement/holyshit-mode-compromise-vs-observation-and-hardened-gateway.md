# 1. Re-verify the prior "holy shits" are patched FIRST (findings decay hourly)

- source canon: `holyshit-mode/compromise-vs-observation-and-hardened-gateway-reengagement.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## The technique

- **Shared-buffer cross-user disclosure / context poisoning patch check = PTOK-drift oracle:**
  fire 3+ identical 1-word requests spaced ~3s apart, read `usage.prompt_tokens`. Constant
  (e.g. 6) = stateless/patched. DRIFTING/growing = shared global buffer re-emerged = the
  highest-value re-find. Do this before anything else; the ledger `negative` rows may predate
  a redeploy that brought the vuln back.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
