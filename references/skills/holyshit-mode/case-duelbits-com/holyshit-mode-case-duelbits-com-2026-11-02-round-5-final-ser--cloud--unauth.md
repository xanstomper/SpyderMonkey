# 2026-11-02 round-5 FINAL: server gate verified — engagement closed — cloud / unauth

- source canon: `holyshit-mode/case-duelbits-com.md`
- base technique: `holyshit-mode-case-duelbits-com-2026-11-02-round-5-final-ser.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- context: **cloud** · auth **unauth** · chain role **pivot**

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: no credential material — the classic differential applies as-is; absent auth = the authn-bypass class

## The technique

**The decisive test came back NEGATIVE.** Operator planted the `state` cookie
(`{"isAdmin":true,"authRole":"Sponsor","accountLevel":8,"verified":true,"zzzz":1}`),
signed out, logged back in with MetaMask: **profile = Normal. No key applied.**

Verdict: the state-cookie trust is real client code (signIn spreads truthy keys from
cookie `state`), the dangling Netlify preview wildcards are real ops debt, but the server
DTO discards unknown keys on `/auth/web3` — the escalation chain ends at the wire. This is
the third consecutive target (gratisfy, gonka, duelbits) where injected claims persist to
the server and are ignored: the "does any backend authorize on injected claims?" gate is
now a 3/3 negative across the framework.

Engagement closeout (2026-11-02):
- 23 classes ledgered; zero compromise-class findings on the live web surface.
- Top standing findings: (1) breach history — two private-key compromises (Feb-2024
  $4.6M, Sep-2026 $7M), no post-mortem, signing-key management broken twice [80/85];
  (2) unvalidated anon scope mint (`/auth/token?scope=X`), inert on HTTP across all 6 sub
  variants [45]; (3) unauth cross-user bet/leaderboard feeds with internal UUIDs [52];
  (4) PF verified CORRECT incl. the active-round seed==hash display bug [30]; (5) multi-env
  CMS delivery-token access + prod-pulls-RC [55]; (6) header_state proxy-topology echo
  [25]; (7) state-cookie client-side trust + dangling preview wildcards — hardening.
- Verified negatives: every internal env (CF Access), both preview families (dead DNS),
  OAuth plane (hardcoded starters, no google state = login-CSRF untested-by-consent),
  socket rooms, minted-JWT consumers, signature replay (untestable — region wall 500s
  even valid signatures), state injection (server DTO strips).
- Console kit preserved for any future clean-vantage re-engagement (web3 replay/binding,
  Google consent login-CSRF proof).

## Probe adjustment (cloud × unauth)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
