# Common WebSocket Auth Patterns to Discover — chain composition

- source canon: `holyshit-mode/websocket-auth-testing.md`
- base technique: `holyshit-mode-websocket-auth-testing-common-websocket-auth-p.md`
- chain role: **pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream**

## Chain roles

- pivot — this BRIDGES a chain: an entry finding upstream plus this pivot plus a final downstream

## Pairing rule

chain detect pairs same-origin findings (the `_origin()` key: scheme + netloc). This technique composes when a sibling finding shares that origin and the pattern's two legs match. Never invent a chain: both legs need their own baseline→attack→diff proof first.

## Composition

Mine the JS bundle for the auth flow. Search for the `WebSocket` constructor and the
first `send()` call. Typical patterns:

1. **Token in first frame** (most common):
   ```js
   this.socket = new WebSocket(socketUrl);
   this.socket.onopen = () => {
     this.send({type: "authenticate", token: r.token});
   };
   ```
   → Auth lives in the **token source** (usually `POST /api/.../session`), not the WS itself.

2. **Token as query param**:
   ```js
   new WebSocket(`wss://target/socket?token=${token}`)
   ```
   → Test: does the server validate the token, or accept any string? Does the token expire?

3. **Cookie-based** (invisible in upgrade headers):
   ```js
   new WebSocket(socketUrl);  # cookies auto-sent
   ```
   → Test: does an unauthenticated session get a working socket?

4. **Signed URL with expiry**:
   ```js
   new WebSocket(signedUrl)  # server signs the URL with HMAC + expiry
   ```
   → Test: replay, expiry bypass, HMAC key extraction.

## Walls

- a chain is a SEVERITY judgment over proven findings — never new execution
- every leg keeps its own ledger row and its own evidence
