# Pitfalls — chain composition

- source canon: `3am-shinjitsu/api-schema-mining.md`
- base technique: `3am-shinjitsu-api-schema-mining-pitfalls.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- A doc page TITLE is a display name; the real route lives inside the OpenAPI JSON
  (operationId/slug ≠ path, e.g. a page named "Get Listed Items" has path
  `/trading/...`). Never guess paths from page names — read the JSON.
- Docs SPAs return an empty shell (`<title>Found. Redirecting...</title>`, ~32-byte body)
  to plain curl — the `.md` endpoints are the reliable entry, not the HTML pages.
- crt.sh rate-limits with an HTML page (starts `[BEGIN_HEADERS]`) instead of JSON — catch
  the parse error and back off; never treat that HTML as a live result.
- A "blocked" response from a docs `/api/*` path proves nothing about the API itself — it
  is the same WAF surface; classify it with the differential ladder before concluding.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
