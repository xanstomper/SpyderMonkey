# The workflow (in order) — azure / high-priv

- source canon: `undercroft/bundle-decode.md`
- base technique: `undercroft-bundle-decode-the-workflow-in-order.md`
- bindings: **WSTG-ATHN** · **CWE-287** · **ATT&CK T1111**
- context: **azure** · auth **high-priv** · chain role **pivot**

## Context

- platform: identity surface — read-only enumeration (shukaku hunt semantics)
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

## The technique

1. **Pull the entry pages** — sitemap.xml lists them; fetch with a browser UA
   (some edges serve different content to default curl UAs).
2. **Harvest chunk names**: `grep -ohE '/_astro/[A-Za-z0-9._-]+\.js'` across every
   downloaded page, then fetch each chunk from the origin.
3. **Follow the import graph one hop**: island components import shared clients
   (`*-client`, store, api modules) by relative path — fetch those too. The typed
   API client is usually the largest app chunk.
4. **Extract route contracts**: typed clients (oRPC-style) reference routes as
   `v.public.group.route.$get/$post`. Grep both forms:
   - dotted: `\.(public|auth)\.[a-z0-9-]+(\.[a-z0-9-]+)*\.\$(get|post|put|patch|delete)`
   - bracket: `public\["[a-z0-9-]+"\]`
   This yields the full endpoint tree including write endpoints.
5. **Decode the string table**: minified bundles hide strings behind `o(NNN)` index
   lookups. Find the big array literal
   (`=\s*\[(?:"[^"\\]{0,120}",){20,}`), parse the strings out — every path
   fragment, verb, `:param` placeholder, and backend host appears there.
6. **Read the CSP meta tag as an infra map**: `connect-src` lists websocket hosts
   (`wss://…`), realtime vendors (Pusher), direct storage (R2/S3), payment
   processors (Stripe); `worker-src`/`frame-src` list service workers and embeds.
   One grep maps the whole backend topology without touching the network.
7. **Reconstruct URLs from the client's own builder**: search the bundle for
   `join("/")` and the proxy `get`/`apply` handler. Typical shape: base +
   `/` + path segments joined, `$verb` popped as the HTTP method, `:param`
   placeholders substituted from call args. Probe GET routes read-only first.

## Probe adjustment (azure × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
