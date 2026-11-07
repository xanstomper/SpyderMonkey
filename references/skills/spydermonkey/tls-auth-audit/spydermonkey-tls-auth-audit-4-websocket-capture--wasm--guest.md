# 4. WebSocket capture — wasm / guest

- source canon: `spydermonkey/tls-auth-audit.md`
- base technique: `spydermonkey-tls-auth-audit-4-websocket-capture.md`
- bindings: **WSTG-BUSL-08** · **CWE-841** · **ATT&CK T1574**
- context: **wasm** · auth **guest** · chain role **pivot**

## Route

- probes: `httpx`, `nuclei-tokens`, `arjun`, `kiterunner`
- chains: `recon`
- gate: every probe runs through the shared scope authority (rc=1 out of estate); the 3-gate differential turns output into a finding

## Context

- platform: sandbox internals — memory/import surface, own compiled artifact only
- auth state: a filter/WAF tier fronts the target: expect canonicalization and signature matching on the raw request — the probe vocabulary's encodings (double-encode, unicode, backslash, case-split) exist exactly for this tier; the differential must clear the filter WITHOUT tripping it, or the finding is a WAF flag, not a class confirmation. Low-and-slow: one variant per request, never a burst.

## The technique

- `page.on('websocket')` only fires for main-world sockets AND only on pages
  that actually open one (chat/game pages, not the landing page); sockets inside
  blob workers escape it. Prefer hooking: `evaluateOnNewDocument` patching
  `window.WebSocket` to log open/send/receive. ArrayBuffer frames print as
  `[object ArrayBuffer]` — that means binary protobuf framing (custom parser),
  not an error.
- A raw `new WebSocket()` from page context without the client's handshake
  params closes 1006. Do NOT hand-build the connect URL — copy it verbatim from
  the hook log (transport params, device-fingerprint and timestamp query params
  included).
- Socket auth may be device-fingerprint + timestamp query params only — no user
  identity. On a public feed/chat socket that is an AUTHN finding (visitor
  sessions ride production sockets).
- The SPA socket opens LAZILY and INTERMITTENTLY: one sequence (landing → chat → game, 10-20s waits) opened it; later repeats of subsets (landing → game, landing → chat alone) opened nothing. On frames: 0, retry the full sequence with long waits before concluding no socket exists.
- `page.goto` to a new route KILLS an open socket and may not reopen it. To exercise a room on a different SPA route (e.g. personal-bets), open the socket on its home page first, then navigate IN-APP: `history.pushState` + `dispatchEvent(new PopStateEvent('popstate'))`, capturing frames across the change.
- The client bundle rarely exposes the socket instance (`window.io` absent — verify with an Object.keys scan). To emit, open a SECOND WebSocket from page context with the connect URL copied verbatim from the hook log; with a custom parser (binary protobuf) events are not socket.io text frames (`42[...]`) — decoding requires the bundle's proto schema.
- Room/event names for personal data with CLIENT-SIDE identity predicates
  (`accept: r.userId === e`) = hypothesis of a server-side enforcement gap.
  Binary protobuf framing usually blocks black-box proof — register as
  hypothesis with the code excerpt as evidence; do not claim CONFIRMED.

## Probe adjustment (wasm × guest)

1. baseline first: the request/session with NOTHING changed
2. attack: the documented class probe, adjusted per context above
3. diff: measurable only — status/length/body — or it is not a finding

## Chain roles

- combines with a prior finding — chain detect pairs same-origin findings
- pairs-with: see `skilltree-index.md` for the sibling techniques

## Walls

- validation-only · NO-GAIN · documented-class adaptation only
- in-scope only: the scope authority refuses everything else (rc=1)
