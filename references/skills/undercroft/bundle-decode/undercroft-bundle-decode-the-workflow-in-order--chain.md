# The workflow (in order) — chain composition

- source canon: `undercroft/bundle-decode.md`
- base technique: `undercroft-bundle-decode-the-workflow-in-order.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

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

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
