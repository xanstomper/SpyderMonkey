# Common WebSocket Auth Patterns to Discover

- source canon: `holyshit-mode/websocket-auth-testing.md`
- bindings: **WSTG-BUSL-06** · **CWE-294** · **ATT&CK T1550**
- generated: 2026-11-04

## The technique

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

## Family use

- decisive-test shape lives in the source canon
- walls: validation-only · NO-GAIN · documented-class adaptation only
