# 5.3 Client-only gates + ID backdoors (score 80)

- source canon: `3am-shinjitsu/arsenal-05-client-side.md`
- bindings: **WSTG-BUSL** · **CWE-200** · **ATT&CK T1005**
- generated: 2026-11-04

## The technique

- GREP every chunk: `user.id === <numeric literal>`, `is_admin`, `switchTab`, `can_*`,
  `window.hide*Gate` — dev backdoors bypassing UI role checks.
- Cross-file consistency law: map EVERY module's check independently — the backdoor may grant
  provider admin in one chunk while giveaway creation stays blocked in another. The
  inconsistency IS the true attack surface.
- EXPLOITABILITY GATE: does the backing API ALSO trust the client flag, or does the endpoint
  independently validate? Client-only bypass without API validation = needs-API-confirmation.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
