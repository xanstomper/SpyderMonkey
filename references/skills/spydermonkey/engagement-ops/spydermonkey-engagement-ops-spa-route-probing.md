# SPA route probing

- source canon: `spydermonkey/engagement-ops.md`
- bindings: **WSTG-SESS** · **CWE-384** · **ATT&CK T1550**
- generated: 2026-11-06

## Route

- probes: `nmap`, `masscan`, `naabu`, `zmap`, `nc`, `fping`, `nmap-allports`
- chains: `net`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## The technique

When a target uses SPA routing (all unknown paths return the same HTML shell), there are two approaches to distinguish real API endpoints from the SPA fallback:

1. **`page.evaluate()` with `fetch()`**: First `page.goto()` the main page and wait 10s+ for any JS challenge to resolve. Then use `fetch()` inside `page.evaluate()`. If it returns `{error:"r is not defined"}` or undefined, the page still has a JS challenge interceptor. Pass the challenge by waiting longer or clicking challenge elements.
2. **`page.goto()` + `document.body.innerText`**: Navigate to each path directly and extract body text. A real JSON endpoint will show its content; the SPA shell will show the same boilerplate (nav, login, footer) on every path.

**Key distinction**: SPA shell = text/html with identical HTML across all paths (usually ~10KB). Real JSON endpoint = application/json with unique per-path content.

**Puppeteer probe-script traps**: Page has no `removeListener`/`listeners` methods (they were on old EventEmitter-style APIs) — use `page.off(event, handler)` or, simplest for per-variant loops, leave the handlers attached and tag results with the variant label; detaching per iteration throws `TypeError: page.removeListener is not a function` and kills the whole run after the first variant. Never attach a fresh `request`/`websocket` listener per loop iteration without an `off()` — the array grows and results interleave across variants. **Puppeteer 22 CDP**: use `page.createCDPSession()` (NOT `page.target.createCDPSession()` — that was the pre-v22 shape and throws `TypeError`). To capture which WebSocket URLs a page opens, hook `Network.webSocketCreated` on the session (register it BEFORE `page.goto`); `page.on('websocket')` is unreliable for capturing socket URLs on some versions — the CDP network event is the dependable capture. `Network.webSocketFrameSent/Received` report binary payloads base64-encoded — decode with `Buffer.from(payload,'base64')`. **In `page.evaluate` there is no Node `Buffer`** — decode binary frames with browser-native `Uint8Array` and `b.toString(16).padStart(2,'0')` for hex, or `String.fromCharCode(...bytes)` for ASCII; a `ReferenceError: Buffer is not defined` inside evaluate is a browser-context scoping bug (yours), not a target or CF issue.

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
