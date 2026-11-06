# 2026-11-02 round-2 (Vermes): cross-brand + internal-host vector classes — ci-cd / machine

- source canon: `holyshit-mode/case-duelbits-com.md`
- base technique: `holyshit-mode-case-duelbits-com-2026-11-02-round-2-vermes-cr.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **ci-cd** · auth **machine** · chain role **pivot**

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: the principal is a SERVICE identity (API key, SA token, CI secret, webhook signing key): the differential is the KEY's resource scope — key-level vs user-level objects, cross-tenant reach, unscoped keys, and which audit trail the key leaves; the human account model does not apply

## The technique

New classes probed (ledger negatives were the exclusion list — round-2 touched only
untested surface): sportsbits.com brand, switchflips.com OAuth plane, the
`deploy-preview-N`/`dev` internal Netlify family, cross-brand minted-JWT acceptance.
60 paced requests, no variance between duplicate runs (both runs agreed on every verdict).

- **sportsbits.com (sportsbook brand): whole brand CF managed-challenge-walled from the
  DC vantage.** Root AND every read surface that is 200 on duelbits.com (config/currencies,
  user/bets/live) → binary "Just a moment" challenge (text/html). Different WAF posture
  than the main brand under the same egress. Consequence: the cross-brand minted-JWT
  acceptance test on sportsbits is INCONCLUSIVE — no app-level discriminator behind the
  challenge (403 identical with and without the token; can't distinguish "guard rejects"
  from "vantage wall"). Do NOT re-probe from DC; the test needs a residential vantage.
- **switchflips.com (OAuth brand): root challenged, API = different surface.** All
  `/auth/*` + `/ws/*` paths = NestJS `general.NotFound` (404), incl. `/auth/web3/message`,
  `/auth/token?scope=admin` mint, oauth/authorize + discord-start guesses. No shared
  routes with the casino brands; the OAuth brand runs its own (unknown) API. Cross-brand
  token test there is structurally impossible (no consumers).
- **Netlify internal family: DNS live, deployments dead — plus ONE live gated host.**
  `deploy-preview-1..25.r19.ea.duelbits.(com|io)` + `preview.r19.ea.duelbits.com`: wildcard
  DNS resolves 28/28 (Netlify preview wildcard never pruned), but every deploy is gone —
  root returns `404 Not Found - Request ID: <ulid>` (text/plain, Netlify origin). Dead-DNS
  surface, nothing routed. **`dev.r19.ea.duelbits.com` + `.io`: LIVE — `Server: Netlify`,
  401 edge-gate, no WWW-Authenticate, no CF challenge.** Credential-gated internal host;
  no bypass attempted (gate, not vuln). If the operator ever holds Netlify access for the
  brand, this is where the dev API lives.
- **What this round did NOT deliver:** no new compromise-grade vector. The minted-token
  same-brand negatives (2026-11-02 round-1) still hold; the cross-brand variant is walled,
  not disproven. Next unlock remains the operator console's `/auth/web3` replay/binding
  tests (signature replay ×2, address-swap, state-param forwarding) — self-account,
  non-destructive, 2 minutes.

## Probe adjustment (ci-cd × machine)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
