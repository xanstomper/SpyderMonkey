# 2026-11-02 round-5 FINAL: server gate verified — engagement closed — chain composition

- source canon: `holyshit-mode/case-duelbits-com.md`
- base technique: `holyshit-mode-case-duelbits-com-2026-11-02-round-5-final-ser.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
