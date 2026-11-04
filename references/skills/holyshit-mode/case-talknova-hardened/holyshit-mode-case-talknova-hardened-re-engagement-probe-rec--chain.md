# Re-engagement probe recipe (reusable for any baselined hardened target) — chain composition

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-re-engagement-probe-rec.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. **Diff the live bundle hash** against the prior case file. Same hash = same code; new hash = redeploy, re-run full probe ladder.
2. **Fetch ALL code-split chunks.** The main bundle only holds the route table; page components are lazy-loaded. Find chunks via `grep -oE '"\./[A-Za-z0-9_-]+\.js"' app.js`, then fetch each and mine for `fetch("..."` calls.
3. **Ghost-route sweep on every discovered path.** Only `application/json` responses are real; `text/html` = SPA fallback ghost. This instantly kills false positives.
4. **Authz matrix on new surface.** For every new endpoint, test: GET unauth, POST unauth, PATCH/DELETE unauth, IDOR by numeric ID, mass assignment with extra fields.
5. **Rate-limit probe EARLY on login endpoints.** If the limiter is aggressive, you'll lock yourself out before injection tests — do SQLi/NoSQLi probes first, or accept the lockout as a negative finding.
6. **Where the wall is, say it.** Pre-auth surface exhausted → state the exact next test and the credential required. Do not probe spam past the wall.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
