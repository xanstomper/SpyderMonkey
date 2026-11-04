# WAF path-class exemption map (works from a fully-blocked box) — chain composition

- source canon: `3am-shinjitsu/edge-gate-recon.md`
- base technique: `3am-shinjitsu-edge-gate-recon-waf-path-class-exemption-map-w.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

- A zone-wide deny is rarely path-uniform. Per host, probe a fixed exemption battery and
  classify by BODY, not status: small-body 403 with JSON/`{}`/backend envelope = ORIGIN
  answered (edge exempted the path); the multi-KB WAF HTML page = edge-blocked.
  Battery: `/_next/static/chunks/nonexist.js` (expect 404-origin), `/health`, `/healthz`,
  `/socket.io/?EIO=4&transport=polling`, `/robots.txt`, `/favicon.ico`, `/cdn-cgi/trace`.
- Exemption classes differ PER HOST on the same zone — run the battery per host, not once.
  A static plane exempt on the apex is often exempt on sibling app hosts too: chunk lists
  from anywhere (see arsenal-02 §2.4 wayback trick) → direct chunk fetches from the box.
- CF `error code: 504` body with `server-timing: cfEdge;dur=<n>,cfOrigin;dur=<n>` = the
  ORIGIN POOL errored/timed out (unhealthy backend), not a gate — ledger as dead surface,
  do not spend bypass attempts on it.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
