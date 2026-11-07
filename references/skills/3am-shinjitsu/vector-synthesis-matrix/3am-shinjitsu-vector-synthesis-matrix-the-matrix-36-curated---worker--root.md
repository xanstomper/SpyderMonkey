# The matrix — 36 curated high-yield pairs — worker / root

- source canon: `3am-shinjitsu/vector-synthesis-matrix.md`
- base technique: `3am-shinjitsu-vector-synthesis-matrix-the-matrix-36-curated-.md`
- bindings: **WSTG-ATHZ-04** · **CWE-639** · **ATT&CK T1068**
- context: **worker** · auth **root** · chain role **pivot**

## Route

- probes: `nmap-smtp-commands`, `nmap-smtp-enum-users`, `swaks`, `dig-mx`, `dig-txt`
- chains: `mail-full`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: edge/background runtime — the check runs where the caller has no visible context
- auth state: the highest local principal — confirm the class from the top down (downgrade/view-as tests, no-gain reads are the crown)

## The technique

| Flaw | Seam | Synthesized probe (decisive one-liner) | Confirmed-when | ★ Proven-class correlate |
|---|---|---|---|---|
| 1 | B | Mirror the client gate server-side: fire the UI-blocked action directly at the API | 200/JSON on an action the UI forbids | hardcoded-ID backdoors (DirectRouter, g***REDACTED***) |
| 1 | F | Callback error taxonomy: exchange-before-validation — drive the callback with forged state+code | error differs from auth-order baseline | OAuth state-binding ladder (talknova) |
| 2 | C | Mass-assignment signup: inject privilege keys in `data`, read them back in the verified JWT | keys persist into `user_metadata` | g***REDACTED***/g***REDACTED***/d***REDACTED*** triple-confirmed |
| 2 | F | State-cookie carrier: plant `{isAdmin, authRole}` fields into the OAuth state cookie | server echoes them into profile | d***REDACTED*** state-carrier |
| 2 | E | Anon socket-token mint: mint WS identity from public metadata, join with token-in-query | frames stream for an identity you never authenticated | duel.com anon socket |
| 3 | D | Object/array-where-string on limiter-keyed fields: `{"key":["a","b"]}`, `1e3` numeric coercion | counting diverges per parse | a***REDACTED*** 422-decoy / coercion oracles |
| 3 | C | Grant-type coercion on token endpoint: password/refresh/id_token confusion matrix | a grant path skips a check | GoTrue token chains |
| 3 | G | 22P02/PGRST-err type-oracle: wrong-typed filter on every column guess | schema/type leaks via error codes | g***REDACTED*** PostgREST oracles |
| 4 | A | Dual-stack split pools: repeat limiter test over IPv6 shadow surface | different budget than IPv4 | Volt Typhoon shadow-surface class |
| 4 | C | Account-vs-IP keying: alternate identities vs one IP, one identity vs many IPs | limiter binds the wrong axis | talknova lockout analysis |
| 4 | J | Unthrottled CPU primitive: burst the tokenizer/count endpoint with big bodies | zero 429, latency scales with body | a***REDACTED*** count_tokens |
| 5 | C | Pre-gate token mint: hit the mint with every privilege scope the client vocab names | any-scope signature accepted | casino any-scope mints |
| 5 | F | redirect_uri forwarding: authorize URL with attacker URI, watch the 302 Location | URI forwarded verbatim | g***REDACTED*** GoTrue (HOLY SHIT) |
| 5 | E | Handshake≠auth: full frame exchange after a clean 101 | rejection only arrives on frame 2+ | CDN WS passthrough canon |
| 6 | H | Sister-brand IDOR: cross-brand numeric/ID reuse against the shared backend | brand B rows served to brand A identity | g***REDACTED*** family ladder |
| 6 | C | Public-id oracle: profile/bet-feed public_ids → deeper per-ID endpoints | unauth per-user rows | rainbet/duel financial chains |
| 6 | G | RLS-vs-function trust split: call the edge function with a non-privileged session | function enforces less than the DB | g***REDACTED*** edge-function |
| 7 | A | Cookie-toss gadget: any param written as a domain cookie by a media/attrib page | cookie lands on the main domain scope | rainbet media.* toss |
| 7 | A | Origin-side ghost re-sweep: routes the CDN masks, re-run the route map direct-to-origin | origin-only routes appear | CF-origin bypass canon |
| 7 | B | Cache-keys-on-cookie: vary cache key inputs vs authed content | authed content served to no-auth fetch | cache poisoning class |
| 8 | H | Wildcard-preview cookie scope: dangling preview hosts share the parent cookie domain | cookie readable/castable via the twin | d***REDACTED*** Netlify wildcard |
| 8 | F | Session fixation via URL param carrier the app mirrors into cookie | param sets the session | fixation canon |
| 8 | C | SameSite-vs-CORS verdict: raw Set-Cookie flags read before rating reflected CORS | Lax+HttpOnly downgrades the class | l***REDACTED*** re-test |
| 9 | A | CL.TE differential at the edge: one timing-only probe, ambiguity = stop | behavior splits between layers | smuggling class |
| 9 | I | Charset/content-type sniff on upload/parse endpoints | parser honors declared charset over validation | XXE/charset canon |
| 9 | F | Open-redirect + token delivery: returnTo/next on flows that carry secrets | Location leaves the origin with secrets | OAuth chain canon |
| 10 | C | Bundle RNG entropy oracle: `Math.random` in the handoff/auth code path | code generator client-side, no CSPRNG | g***REDACTED*** handoff |
| 10 | C | JWT confusion battery: alg-none, anon-key-as-secret, header jwk injection | any variant verifies | SupaBomb (all-negative = layered) |
| 10 | E | EIO sid reuse: engine.io sid across reconnects/users | sid accepted for another session | engine.io sid canon |
| 11 | H | Error-envelope diffing across sister brands: identical envelopes = shared backend | verbatim error from two hosts | g***REDACTED*** envelope diff |
| 11 | C | Forgot-password/resend mail-bomb: state-changers missing rate limits | 36 rapid 200s, zero 429 | a***REDACTED*** reset pump |
| 11 | D | 405/403/404 taxonomy route-map: pair status+content-type across all methods | a route exists that the UI never names | 405-matrix canon |
| 12 | C | PTOK drift oracle: 3× identical 1-word requests, read `usage.prompt_tokens` | drifting/growing = shared server state | obsidian-y |
| 12 | C | Client system-role honored: send a system role the gateway adopts | system turns appear in the trace | obsidian-y data plane |
| 12 | J | Model-substitution oracle: request a hidden model-name variant, read `served_by` | substitute model serves the call | obsidian-y served_by |
| 12 | E | Cross-user context poisoning write: plant directive via shared buffer | directive reappears in another caller's trace | obsidian-y (score 95) |

## Probe adjustment (worker × root)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
