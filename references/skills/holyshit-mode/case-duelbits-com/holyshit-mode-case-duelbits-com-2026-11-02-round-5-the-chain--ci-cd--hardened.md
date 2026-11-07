# 2026-11-02 round-5: THE CHAIN CORRECTED — cookie `state`, not URL param — ci-cd / hardened

- source canon: `holyshit-mode/case-duelbits-com.md`
- base technique: `holyshit-mode-case-duelbits-com-2026-11-02-round-5-the-chain.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **ci-cd** · auth **hardened** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: pipeline config/runner surface — secrets and lateral movement ride the runners
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

**Correction (honesty first): the URL-param carrier was a misread.** The web3 signIn reads
`document.cookie['state']` — the `r` helper in web3-sign-in is `C as P` from
startup-small-1-DQYGbmJw.js, a **document.cookie reader** (not a URL param getter). The
`?state=` URL param is mirrored server-side into the *query_state* cookie, but the client
reads the cookie literally named `state` — so the operator's `?state=` test shipped an
empty `state = {}` and nothing stuck (matching the observed "didn't escalate" exactly).

Verified facts:
- `signIn()`: `r('state')` → cookie; `JSON.parse` → `Xb` (pure passthrough, no key filter)
  → **truthy-key spread** into BOTH the query string and POST body `{address, signature,
  ...state}`.
- **No client code ever writes cookie `state`** (grep of all 420 chunks: zero setter call
  sites with `state`; the only `document.cookie` write in the bundle is a generic setter
  with no `state` callers). It must come from the server or an attacker.
- No tested endpoint returns `Set-Cookie: state=...` (only `header_state` + `query_state`,
  both unread by the auth path).

**The real attack architecture (new finding):**
1. The signIn trusts a cookie-named `state` and spreads its keys into the auth request.
2. Any cookie-injection primitive on `*.duelbits.com` becomes an account-class-escalation
   injection: Set-Cookie `state={"isAdmin":true,"authRole":"Sponsor","accountLevel":8,
   "verified":true}; Domain=.duelbits.com; Path=/` from any subdomain-hosted page is
   honored by the main origin (domain-suffix rule).
3. **Candidate platform: the dangling Netlify preview wildcards.** `deploy-preview-N`
   `.r19.ea`/`.ea.duelbits.com` all resolve to Netlify edge IPs with deployments deleted
   (404 Not-Found-Request-ID). If claimable on a fresh Netlify account (verification
   commonly passes when DNS already points at Netlify), a one-line-state attack page is
   trivial: victim clicks → cookie planted → victim's next wallet login ships the
   attacker's keys to `/auth/web3`.
4. Remaining unverified gates: (a) Netlify claimability (infra takeover — operator's
   call, NOT executed), (b) server-side acceptance of the keys (one console test below).

**Decisive self-account console test (60s):** on duelbits.com, open DevTools console →
`document.cookie='state={"isAdmin":true,"authRole":"Sponsor","accountLevel":8,"verified":true,"zzzz":1};path=/'`
→ sign out → wallet login (MetaMask) → check profile. State stuck = server applies keys =
the cookie-tossing chain is a full account-class escalation path on a $190M/yr casino,
exploitable with one link + a dangling subdomain. State clean = DTO strips keys, chain
ends at the wire (and the subdomain dangle stays a hygiene hardening note).

## Probe adjustment (ci-cd × hardened)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
