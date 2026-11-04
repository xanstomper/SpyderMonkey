# WAF path-class exemption map (works from a fully-blocked box) — container / high-priv

- source canon: `3am-shinjitsu/edge-gate-recon.md`
- base technique: `3am-shinjitsu-edge-gate-recon-waf-path-class-exemption-map-w.md`
- bindings: **WSTG-CONF-04** · **CWE-530** · **ATT&CK T1552**
- context: **container** · auth **high-priv** · chain role **pivot**

## Context

- platform: namespace/capability surface — read-only inventory, no escape execution
- auth state: the baseline IS the privileged session; test downgrade paths (mass-assign, state-bypass)

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

## Probe adjustment (container × high-priv)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
