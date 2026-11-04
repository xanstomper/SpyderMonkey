# Re-engagement probe recipe (reusable for any baselined hardened target)

- source canon: `holyshit-mode/case-talknova-hardened.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- generated: 2026-11-04

## The technique

1. **Diff the live bundle hash** against the prior case file. Same hash = same code; new hash = redeploy, re-run full probe ladder.
2. **Fetch ALL code-split chunks.** The main bundle only holds the route table; page components are lazy-loaded. Find chunks via `grep -oE '"\./[A-Za-z0-9_-]+\.js"' app.js`, then fetch each and mine for `fetch("..."` calls.
3. **Ghost-route sweep on every discovered path.** Only `application/json` responses are real; `text/html` = SPA fallback ghost. This instantly kills false positives.
4. **Authz matrix on new surface.** For every new endpoint, test: GET unauth, POST unauth, PATCH/DELETE unauth, IDOR by numeric ID, mass assignment with extra fields.
5. **Rate-limit probe EARLY on login endpoints.** If the limiter is aggressive, you'll lock yourself out before injection tests — do SQLi/NoSQLi probes first, or accept the lockout as a negative finding.
6. **Where the wall is, say it.** Pre-auth surface exhausted → state the exact next test and the credential required. Do not probe spam past the wall.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
