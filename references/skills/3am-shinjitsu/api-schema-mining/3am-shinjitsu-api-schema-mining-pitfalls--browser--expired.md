# Pitfalls — browser / expired

- source canon: `3am-shinjitsu/api-schema-mining.md`
- base technique: `3am-shinjitsu-api-schema-mining-pitfalls.md`
- bindings: **MASTG-RES** · **CWE-288** · **ATT&CK T1557**
- context: **browser** · auth **expired** · chain role **pivot**

## Route

- probes: `nmap-slowloris-check`, `curl`
- chains: `web`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: the CLIENT is the boundary — same-origin, extension, and postMessage trust are the probe shape
- auth state: the credential/session has lapsed — the class probes reuse, reactivation, and the no-revoke gap

## The technique

- A doc page TITLE is a display name; the real route lives inside the OpenAPI JSON
  (operationId/slug ≠ path, e.g. a page named "Get Listed Items" has path
  `/trading/...`). Never guess paths from page names — read the JSON.
- Docs SPAs return an empty shell (`<title>Found. Redirecting...</title>`, ~32-byte body)
  to plain curl — the `.md` endpoints are the reliable entry, not the HTML pages.
- crt.sh rate-limits with an HTML page (starts `[BEGIN_HEADERS]`) instead of JSON — catch
  the parse error and back off; never treat that HTML as a live result.
- A "blocked" response from a docs `/api/*` path proves nothing about the API itself — it
  is the same WAF surface; classify it with the differential ladder before concluding.

## Probe adjustment (browser × expired)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
