# Re-engagement probe recipe (reusable for any baselined hardened target) — cloud / federated

- source canon: `holyshit-mode/case-talknova-hardened.md`
- base technique: `holyshit-mode-case-talknova-hardened-re-engagement-probe-rec.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **cloud** · auth **federated** · chain role **pivot**

## Route

- probes: `sqlmap`, `nosqlmap`, `tplmap`, `commix`, `crlfuzz`, `dotdotpwn`, `nmap-http-sqli`, `nmap-shellshock`
- chains: `fuzz`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: control-plane exposure — read-only, crown the class
- auth state: identity rides an external IdP (OAuth/OIDC/SAML/SSO): the differential is the TOKEN — audience, issuer, redirect_uri, scope downgrades, code/state reuse, and the exchange at the resource server; the local session may be fine while the trust boundary is not

## The technique

1. **Diff the live bundle hash** against the prior case file. Same hash = same code; new hash = redeploy, re-run full probe ladder.
2. **Fetch ALL code-split chunks.** The main bundle only holds the route table; page components are lazy-loaded. Find chunks via `grep -oE '"\./[A-Za-z0-9_-]+\.js"' app.js`, then fetch each and mine for `fetch("..."` calls.
3. **Ghost-route sweep on every discovered path.** Only `application/json` responses are real; `text/html` = SPA fallback ghost. This instantly kills false positives.
4. **Authz matrix on new surface.** For every new endpoint, test: GET unauth, POST unauth, PATCH/DELETE unauth, IDOR by numeric ID, mass assignment with extra fields.
5. **Rate-limit probe EARLY on login endpoints.** If the limiter is aggressive, you'll lock yourself out before injection tests — do SQLi/NoSQLi probes first, or accept the lockout as a negative finding.
6. **Where the wall is, say it.** Pre-auth surface exhausted → state the exact next test and the credential required. Do not probe spam past the wall.

## Probe adjustment (cloud × federated)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
