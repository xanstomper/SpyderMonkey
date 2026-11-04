# Order of operations — chain composition

- source canon: `holyshit-mode/client-bundle-source-study.md`
- base technique: `holyshit-mode-client-bundle-source-study-order-of-operations.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

1. **Inventory.** Fetch index.html → asset list; fetch the entry chunk + every listed
   chunk. Every fetch needs the full spoof stack (UA, Accept, Accept-Language, sec-ch-ua,
   Sec-Fetch-*, Referer, --compressed) AND `-w "%{http_code} %{size_download}\n"` — a
   silent empty download is the #1 false-negative source. Pace 3-5s on WAF'd targets;
   a CF managed-challenge body is binary/turnstile — bail before re-probing.
2. **APIConfig / env chunks FIRST.** Grep for `APIConfig-*.js` and `env-*.js`: the whole
   environment map ships there — per-hostname blocks of `{token, auth, oAuth, websocket,
   gamesocket}` including dev/staging/canary hosts and preview-host regexes. Every
   hardcoded internal host is a probe target: DNS check, then gate classification
   (CF Access login page has title "Sign in · Cloudflare Access"; Netlify 401 = password
   gate; Netlify "Not Found - Request ID" + Server:Netlify = deleted deploy). The env
   chunk also inventories every VITE_* key — score each by what it authenticates
   (Contentful delivery token = semi-public; provider widget keys = semi-public by
   design; a minted API key = finding).
3. **Endpoint call sites.** Regexes that work, in order:
   - quoted absolute paths: `["'\`](/[a-zA-Z0-9_\-/?.=&${}.:]{1,160})["'\`]`
   - relative template-literal paths WITHOUT leading slash (common wrapper pattern):
     `[\x27\x60]([a-zA-Z][a-zA-Z0-9_/.-]{1,90})[\x27\x60]` filtered by route vocabulary
     (`user/`, `games/`, `auth/`, `betradar/`, `config/`, `tickets/`, ...). Most quoted
     strings are i18n keys — filter HARD or the list is 1000+ noise entries.
   - fetch/axios call sites: `fetch\(\s*["'\`]([^"'\`]{1,200})["'\`]` plus absolute-URL
     in-call-site regexes (they leak admin/dev hosts the DNS enum misses).
4. **Lazy chunks.** Grep the routes/entry chunk for `assets/<name>.js` references
   (webpack `__vite__mapDeps`, import maps) and fetch every referenced chunk missing from
   your set. The login/auth chunk is usually lazy and holds the signIn logic; a secret
   sweep is incomplete without it AND the entry chunk itself.
5. **Socket vocabulary.** emit/on/join event names — filter CSS-in-JS noise (reject
   strings with spaces; keep known prefixes, `user:`, `game:`, `internal:`, custom
   subscription events).
6. **Privilege branches.** `user.id === N` hardcodes; numeric user-class enums (VIP
   ladder) and loginTypes enums = internal vocabulary for mass-assignment payloads;
   `isInternal`-style flags may be domain vocabulary (sportsbook internal MARKETS), not
   privilege — check the field's type before rating.
7. **Import resolution (critical step).** For every call of interest, resolve the
   imported helper to its defining chunk, its export-map alias (`export{T as A, C as P}`),
   and the function body. Cookie readers, URLSearchParams readers, and localStorage
   readers are indistinguishable at the call site; the carrier determines the exploit.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
