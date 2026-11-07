# Lessons learned this session

- source canon: `holyshit-mode/case-directrouter-pages-dev.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- generated: 2026-11-04

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

1. **Public-endpoint PII sweep belongs in the FIRST round of probes.** The
   `/api/leaderboard/invites` HIGH-severity finding was found by sweeping
   `/api/leaderboard/*`, `/api/health`, `/api/catalog`, `/api/version` BEFORE probing
   any auth-gated endpoint. This is now codified as Recon Efficiency check #9.
2. **Junk-Bearer 200 on `/v1/models` is NOT a finding.** Public model lists are standard
   for OpenAI-compatible routers. Test `/v1/chat/completions` with the same junk Bearer
   before reporting; if chat-completions returns 401, the auth model is correct.
3. **D1 type-error oracle** is a backend-fingerprint + input-validation bug. The 5/5min
   rate limiter prevents chaining into a user enum, but the error message alone
   fingerprints the stack (Cloudflare D1) and confirms input isn't type-validated.
4. **OAuth start URL is a recon goldmine even without completion.** `client_id`,
   `redirect_uri`, `scope`, `state` generation behavior are all there, recoverable in
   one 302 follow. The 4 attributes alone often yield 2-3 findings on their own
   (open-redirect, scope-inflation, CSRF state prediction).
5. **Do NOT self-bootstrap credentials.** When the wall is OAuth/SSO, the correct move
   is to ask the operator for a token, Bearer, or authorized test account. Bootstrapping
   a real Discord/Google account via disposable email + automation is account fraud,
   not pentesting, regardless of how technically trivial it is. The operator's "no u
   dont" is the right answer — the doctrine's "gifted key is a finding, not a license"
   applies symmetrically: a self-bootstrapped key is also not a license.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
