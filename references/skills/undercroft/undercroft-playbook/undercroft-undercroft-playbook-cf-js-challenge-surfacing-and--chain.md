# CF JS-challenge surfacing and session-bound IDOR classification — chain composition

- source canon: `undercroft/undercroft-playbook.md`
- base technique: `undercroft-undercroft-playbook-cf-js-challenge-surfacing-and.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- When curl/CLI probes on a target hit a ~162-byte Cloudflare JS-challenge shell
  (every asset returns the same placeholder), do NOT hand-write puppeteer scripts on
the VM first — a real browser passes the challenge automatically. Use `browser_exec`
to load the SPA, then **navigate directly to candidate API endpoints**; the browser
renders the raw JSON response in the body. This is the fastest route to the real
server API surface on a JS-challenge-gated estate, and it ALSO reveals true HTTP
status + auth responses (401 vs 200 vs "Oops, ...gone") that SPA shell-200s mask.
  - Capture the ORIGINAL live API calls from `performance.getEntriesByType('resource')`
  after the SPA loads — the real endpoint catalogue (auth, balance, payment-methods,
  games, contests) is in the traffic, not guessable from subdomain fuzzing.
  - Probe async fetches reliably by storing to a `window.__probe` global from an IIFE,
  then reading it back in a SEPARATE `js()` call — inline async/await through the
  CDP evaluate shim silently returns the function/`{}` instead of the awaited value.
- PITFALL: classifying IDOR. When you inject a real target user-id into a user-scoped
  endpoint (`?userId=<cid>` or `/user/<uid>/`) and it ALWAYS returns the same
  session-bound **guest** object (`userId:0`, empty wallet, `4001 refresh`), that is
  NOT an IDOR — the endpoint ignores the spoofed param and binds to the session
  cookie. The finding is the *absence* of cross-user access, plus any PII the
  unauth endpoint leaks. Do not register a guessed-IDOR with a guest-object reply as
  CONFIRMED; register the clean result as EXHAUSTED with the exact test, and bank
  any unauth data disclosure (e.g. a public leaderboard leaking real user ids +
  balances + currency) as the real finding. The only way past a session-bound wall
  is an authenticated lifecycle (register a throwaway account and test the
  OAuth/session/privilege logic server-side) — park that as the next decisive test,
  never claim a server-side breach that wasn't proven.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
