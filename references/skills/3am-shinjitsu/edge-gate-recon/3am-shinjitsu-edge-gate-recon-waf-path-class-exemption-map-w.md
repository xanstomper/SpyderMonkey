# WAF path-class exemption map (works from a fully-blocked box)

- source canon: `3am-shinjitsu/edge-gate-recon.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
