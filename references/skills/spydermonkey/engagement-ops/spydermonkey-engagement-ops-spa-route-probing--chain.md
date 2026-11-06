# SPA route probing — chain composition

- source canon: `spydermonkey/engagement-ops.md`
- base technique: `spydermonkey-engagement-ops-spa-route-probing.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

When a target uses SPA routing (all unknown paths return the same HTML shell), there are two approaches to distinguish real API endpoints from the SPA fallback:

1. **`page.evaluate()` with `fetch()`**: First `page.goto()` the main page and wait 10s+ for any JS challenge to resolve. Then use `fetch()` inside `page.evaluate()`. If it returns `{error:"r is not defined"}` or undefined, the page still has a JS challenge interceptor. Pass the challenge by waiting longer or clicking challenge elements.
2. **`page.goto()` + `document.body.innerText`**: Navigate to each path directly and extract body text. A real JSON endpoint will show its content; the SPA shell will show the same boilerplate (nav, login, footer) on every path.

**Key distinction**: SPA shell = text/html with identical HTML across all paths (usually ~10KB). Real JSON endpoint = application/json with unique per-path content.

**Puppeteer probe-script traps**: Page has no `removeListener`/`listeners` methods (they were on old EventEmitter-style APIs) — use `page.off(event, handler)` or, simplest for per-variant loops, leave the handlers attached and tag results with the variant label; detaching per iteration throws `TypeError: page.removeListener is not a function` and kills the whole run after the first variant. Never attach a fresh `request`/`websocket` listener per loop iteration without an `off()` — the array grows and results interleave across variants. **Puppeteer 22 CDP**: use `page.createCDPSession()` (NOT `page.target.createCDPSession()` — that was the pre-v22 shape and throws `TypeError`). To capture which WebSocket URLs a page opens, hook `Network.webSocketCreated` on the session (register it BEFORE `page.goto`); `page.on('websocket')` is unreliable for capturing socket URLs on some versions — the CDP network event is the dependable capture. `Network.webSocketFrameSent/Received` report binary payloads base64-encoded — decode with `Buffer.from(payload,'base64')`. **In `page.evaluate` there is no Node `Buffer`** — decode binary frames with browser-native `Uint8Array` and `b.toString(16).padStart(2,'0')` for hex, or `String.fromCharCode(...bytes)` for ASCII; a `ReferenceError: Buffer is not defined` inside evaluate is a browser-context scoping bug (yours), not a target or CF issue.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
